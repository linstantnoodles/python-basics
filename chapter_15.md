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

### Absolute imports (import X or from X import Y where X does not contain dots)
.
With absolute imports, the thing that stays the same for all files doing an absolute import is what set of files they have access to. So the most important thing to understand is how the import machinery in python _determines_ what that set is.

That process looks a bit like this:

1. Did we already import this (Is it in our module cache?) If so, do nothing! You already have it. If not, move on to the second check. sys.modules.
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

```bash.
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

I rarely ever have to pay any attention to these system paths. All you really have to know is that they're there.

All together, the default list is made up of `<CURRENT DIR OR DIR OF FILE> <PYTHON_PATH> <SYSTEM PATHS>`. Once `sys.path` is constructed based on the rules above, it remains the same throughout the lifetime of the program if unmodified.

## Did you just say ... unmodified?

Well that makes it sound like it can be modified (spoiler: it can). Updating `sys.path` in a program before importing is a common technique for getting access to what you need.


TODO: example here            hy

## Relative imports (from X import Y where X contains does )

X will represent the import source. It either contain leading dots or no dots.

For example:

`from myproject.ausefulmodule import usefulfunction`

## With dots

According to the manual:

> One leading dot means the current package where the module making the import exists.
 Two dots means up one package level.
 Three dots is up two levels, etc.

"Packages" are also modules, with the exception that they mainly serve as a namespacing mechanism and do not need to point to an actual source file.

In python2, a directory is only a module if it contains an `__init__.py` file. In python 3, this file is optional.

Example: 

app/
	main.py
	volcanos/
		maunaloa.py

main.py 
```
from volcanos.maunaloa import location

print("You are in main.py")
print("The location of maunaloa is {}".format(location))
```

alin@alin-x1:~/code/python-import-testing$ python3 app/main.py 
this is mauna loa.py
You are in main.py
The location of maunaloa is Hawaii



alin@alin-x1:~/code/python-import-testing$ python app/main.py 
Traceback (most recent call last):
  File "app/main.py", line 1, in <module>
    from volcanos.maunaloa import location
ImportError: No module named volcanos.maunaloa

Now lets add an init.py

alin@alin-x1:~/code/python-import-testing$ touch app/volcanos/__init__.py
alin@alin-x1:~/code/python-import-testing$ python app/main.py
this is mauna loa.py
You are in main.py
The location of maunaloa is Hawaii
alin@alin-x1:~/code/python-import-testing$ 

<python 2 vs python 3> 

`from .subchild import fork`

1. This is done by a module in a package. What a package is varies in python 2 and 3.
2. The package it's referring to CANNOT be the __main__ module

The main module is the entry point file. Basically, the one you're executing. Here's what happens when you add a leading dot: 

from .volcanos.maunaloa import location

python3 main.py 
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from .volcanos.maunaloa import location
ModuleNotFoundError: No module named '__main__.volcanos'; '__main__' is not a package

But given this folder structure


app/
	main.py
	volcanos/
		maunaloa.py
		maunakea.py


from volcanos.maunaloa import location
print("You are in main.py")
print("The location of maunaloa is {}".format(location))

from .maunakea import height
print("this is mauna loa.py")
location = 'Hawaii'
print("Mauna loa is located in {}. It's next to mauna kea which has a height of {} feet".format(location, height))


print("this is maunakea.py")
height = 33000


alin@alin-x1:~/code/python-import-testing/app$ python3 main.py
this is maunakea.py
this is mauna loa.py
Mauna loa is located in Hawaii. It's next to mauna kea which has a height of 33000 feet
You are in main.py
The location of maunaloa is Hawaii 		

## Without dots

If you're using `from X` without dots, then X needs to be in same directory as the main module.

Note: the __main__ module is the entry point of the program.

Relative imports seems really attractive alternative to not having to update sys.path at runtime for child packages. On the other hand, I also like being able to rely mostly on one style of importing throughout a project.

## Running files as scripts 

sometimes we want code in a file to execute only if it's being used a script but not executed on import. there's a common conditonal that's used to apply script behavior to a python module. 

if __name__ == '__main__':
	print("do script things")
	https://stackoverflow.com/questions/419163/what-does-if-name-main-do


so when python creates a module it also sets a few built in secret variables. one of them is __name__ which is just the name of the module. lets see what this prints in our files 


this is maunakea.py
Module name: volcanos.maunakea
this is mauna loa.py
Mauna loa is located in Hawaii. It's next to mauna kea which has a height of 33000 feet
Module name: volcanos.maunaloa
You are in main.py
The location of maunaloa is Hawaii
Module name: __main__

as you can see by adding a print of the names to our files, you'll see that the module in the packages contain the full path. the entry point is always __main__. python users use this to their advantage in modules to execute code when the file is being run directly by python interpreter (as main).

## Common gotchas 

ValueError: attempted relative import beyond top-level package

https://docs.python.org/3.5/c-api/unicode.html#c.PyUnicode_FindChar

last_dot = PyUnicode_FindChar(package, '.', 0, last_dot, -1);

`package` is the name of the package. So lets say `volcanos.manuakea`. so if we look up, we will find index to be positive (8). if it's positive, then 

https://github.com/python/cpython/blob/762f93ff2efd6b7ef0177cad57939c0ab2002eac/Python/import.c#L1682

base = PyUnicode_Substring(package, 0, last_dot);

it gets the name of that base parent. 

if it can't find a dot, you'll get an error. the only way you can't find a dot is if the package name contains no dot. and the only package without a dot is the top level package. 


lets say we're in a module with name volcano.maunaloa 
from ..kiluea import height

One leading dot means the current package where the module making the import exists

current package where the module (volcano.maunaloa) exists is volcano! so that's a top level package. there are no more dots after that. 

there WOULD be if the directory containing our main.py was considered a package (but it isn't).

i.e app.volcano






ModuleNotFoundError: No module named '__main__.volcanos'; '__main__' is not a package






https://docs.python.org/3/reference/import.html#package-relative-imports


Absolute imports may use either the import <> or from <> import <> syntax, but relative imports may only use the second form; the reason for this is that:

import XXX.YYY.ZZZ

should expose XXX.YYY.ZZZ as a usable expression, but .moduleY is not a valid expression.

https://www.python.org/dev/peps/pep-0328/#rationale-for-absolute-imports


goood practice: 

user absolute imports. dont rely on relative. is not as explicit.

