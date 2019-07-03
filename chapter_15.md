# Imports

## What can be imported?

Any file ending in ".py" whose name is a [valid python identifier](https://docs.python.org/2.5/ref/identifiers.html) is importable.

An importable file isn't necessarily available to every python file to import. Put in more concrete terms, any piece of paper *can* be shipped if it's wrapped in an envelope and stamped - but it may not be possible to ship it to you specifically if you don't have an address.

In python, the set of importable files that can actually be imported by a program depends primarily on:

* How you start the python program (by program, i'm referring to any file containing python code)
* What import statement you use
* What environment variables exist

It's these rules that add complexity to the import system.

Note:

Sometimes you'll hear people refer to these importable python files (ending in `.py`) as "modules". Although "python file" and "module" are often used interchangeably, that usage is not accurate because not all python files can be modules. A module is a python object created in the python runtime that acts as an abstraction for the file in the file system. If that file is not named correctly, it can still executed by the python interpreter but cannot be instantiated into a module object during the import process.

## Import strategies

There's two main syntaxes for importing code in python.

1) import X
2) from X import Y

The first performs an absolute import. By absolute, we mean the location of the program does *not* matter. A program located in X using this statement will have access to the same set of files as a program located in Y using the same statement.

The second performs a relative import. That means the location of the program *does* matter. A program located in X using the relative import syntax will *not* have access to the same set of files as a program located in Y using the relative import syntax.

### Absolute imports (import X)

With absolute imports, the thing that stays the same for all files doing an absolute import is what set of files they have access to. So the most important thing to understand is how the import machinery in python _determines_ what that set is.

That process looks a bit like this:

1. Did we already import this (Is it in our module cache?) If so, do nothing! You already have it. If not, move on to the second check.
2. Is it a built-in module? If so, you can totally have it! If not ....
3. Is it located in any of the directories under `sys.path`? If so, you can have it! If not, sorry - we cannot import your file (python will raise an ImportError at this point)

Of the 3 steps, I find the last step more complex because the set of directories in `sys.path` is set based on a number of rules. So if you're wondering if a file can be imported, it's not enough to know that python will look it up in `sys.path` since that list is not static - you need to know exactly what's in that list.

The list of directories in `sys.path` is made up of (in exact order):

1. Current directory or directory of program

It all depends how you start the python program.

If you're calling it inline like this:

`python -c 'import sys; print(sys.path)'`

Then the value will be "" which represents the current directory.

If you're passing a script to the interpreter, then the value will be the directory of where that script is located.

So if you run `python hey/there/main.py`, then the value will be the absolute path to `hey/there`.

2. PYTHONPATH

The second value in the list will be the value of the `PYTHONPATH` environment variable if it exists.

`PYTHONPATH='/usr/whattheshit' python -c 'import sys; print(sys.path)'`

This will place `/usr/whattheshit` in front of the current directory value `''`.

Here's an example output using both inline execution and setting `PYTHONPATH`.

```bash
PYTHONPATH='/usr/whattheshit' python -c 'import sys; print(sys.path)'

['', '/usr/whattheshit', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/gtk-2.0']
```

You might be wondering what all that `/usr/*` stuff is at the end. That's the list of python installation related directories which make the the final leg of `sys.path`.

3. System python installation paths

This depends on where python is installed on your platform. This is where all of the core packages and files are located.

Here's a sample list on my linux machine:

```
[
	'/usr/lib/python2.7',
	'/usr/lib/python2.7/plat-x86_64-linux-gnu',
	'/usr/lib/python2.7/lib-tk',
	'/usr/lib/python2.7/lib-old',
	'/usr/lib/python2.7/lib-dynload',
	'/usr/local/lib/python2.7/dist-packages',
	'/usr/lib/python2.7/dist-packages',
	'/usr/lib/python2.7/dist-packages/gtk-2.0'
]
```

I rarely ever have to pay any attention to these paths. All you really have to know is that they're there.

All together, the default list is made up of `<CURRENT DIR OR DIR OF FILE> <PYTHON_PATH> <SYSTEM PATHS>`. Once `sys.path` is constructed based on the rules above, it remains the same throughout the lifetime of the program if unmodified.

## Did you just say ... unmodified?

Well that makes it sound like it can be modified (spoiler: it can). Updating `sys.path` in a program before importing is a common technique for getting access to what you need.

## Relative imports (from X import Y)

X will represent the import source. It either contain leading dots or no dots.

For example:

`from myproject.ausefulmodule import usefulfunction`

## With dots

According to the manual:

> One leading dot means the current package where the module making the import exists.
 Two dots means up one package level.
 Three dots is up two levels, etc.

"Packages" are also modules, with the exception that they mainly serve as a namespacing mechanism and do not need to point o an actual source file.

First, lets start with child directories aka packages that live in the same dir as your main. you can just import using dot notation.

`from .subchild import fork`



## Without dots

If you're using `from X` without dots, then X needs to be in same directory as the main module.

Note: the __main__ module is the entry point of the program.

## With dots

1. This is done by a module in a package. What a package is varies in python 2 and 3.
2. The package it's referring to CANNOT be the __main__ module.

# Notes for myself

Relative imports seems really attractive alternative to not having to update sys.path at runtime for child packages. On the other hand, I also like being able to rely mostly on one style of importing throughout a project.

Ok. so cool. now we know how to import things from a current directory or from a module that lives in the same dir as the main file. but we seldom have all of our source files in just one directory.

what if our module lives in a different dir?
	what if it lives in an ancestor dir?
	what if it lives in a child dir?

So the way python lets you put ur stupid modules into other places (directories) and still use them is through "packages". these are also modules, just more special b.c they are not actual files. they let use basically namespace modules with same names into multiple contexts.

First, lets start with child directories aka packages that live in the same dir as your main. you can just import using dot notation.

i.e

/main.py
/child
	/spoon.py

well main can do "import child.spoon". same result.

Now, how do the stuff you're importing know how to import their own shit?

/main.py
/child
	/spoon.py
	/subchild
		/fork.py

You might guess: well maybe the same rule applies there!

Actualy nope. so note that sys path will not drill into child directories FOR you. while the package could be found (and thus the child can also be found for spoon.py), that doesn't include the subchild.

Now if the act of importing spoon causes /child to be added to the sys.path, then doing "import subchild.fork" in spoon.py would work.

HOW THE FUCK DO WE GET AROUND THIS?

Option a: we can modify sys.path or get into the hooks. this is annoying because imagine having to do this for a complex tree... you need to specify ALL the paths upfront. yikes.

Option b: use relative imports. oh shit did u know this existed.

So option B gets us into the topic of RELATIVE imports. so we're not just using sys.path which is set in stone (unless modified) based on location of main. we can import shit RELATIVE to where the current module doing the importing IS (which is crucial for nested modules).

This works:

from .subchild import fork

Notice the fucking dot in front? The manual says it best honestly:

 One leading dot means the current package where the module making the import exists.
 Two dots means up one package level.
 Three dots is up two levels, etc.

Notice we have NO mention if sys.path. Not in there? doesn't fucking matter. that's why FROM is so dope.

OKAY. now what does this mean for PARENT imports? That's easy to answer now.

First, are you doing an absolute import? If so, sys.path is king. So if your child module is importing a parent, is that parent in sys.path? That's the question.

If you're NOT doing an absolute import, then are you during the right dots?

Ok so I just tried a dot and got this bullshit:

ValueError: attempted relative import beyond top-level package

So this happens if you try to do .. but .. refers to the very top level directory.
Even if you go ... - if you're trying to refer to a module in the top level, it will NOT work because dots need to be followed by a PACKAGE that lives in the top level.

Not to mention that: HEY, you do not fucking need absolutes because if it's at the top level, then you probably already have access to it via sys.path so just use an absolute import.