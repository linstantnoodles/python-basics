# Imports

# Why import? 

Why are books organized into chapters? 

Splitting a large program into multiple files is a really useful way of organizing your program so that it's easier to understand and change. The code in those files ultimately need to work together, and imports are a means of bringing together source code that live in different places. 

# What can be imported?

Any file ending in ".py" whose name is a [valid python identifier](https://docs.python.org/2.5/ref/identifiers.html) is importable.

An importable file isn't necessarily available to every python file to import. It's the same distinction between a physical good that *can* be shipped (it's in a shippable package) versus goods that can be shipped to *you*. 

While you might have a set of files in a project that all contain useful and importable code, the subset of files that can be imported by a program is dependent on a number of factors such as:

* How you start the python program
* What import statement you use
* Environment variables

If what a program can import did not depend on those factors, this whole business would be much less confusing.

Note:

Sometimes you'll hear people refer to these files as "modules". Although "python file" and "module" are often used interchangeably, that usage is not technically correct because not all python files can be modules. 

A module is the runtime representation of a source file. If that file is not named correctly, it can still executed by the python interpreter but cannot be instantiated into a module during the import process.

# Import strategies

There's two main syntaxes for importing code in python. 

1) import X  
2) from X import Y

The first performs an absolute import. That means the location of the program does *not* matter. A program located in X using this statement will have access to the same set of files as a program located in Y using the same statement. 

The second performs a relative import. That means the location of the program *does* matter. A program located in X using the relative import syntax will *not* have access to the same set of files as a program located in Y using the relative import syntax. 

# import X

With absolute imports, the thing that stays the same for all files doing an absolute import is what set of files they have access to. So the most important thing to understand is how the import machinery in python _determines_ what that set is.

That process looks a bit like this: 

1. Did we already import this? Is it in our module cache? If so, do nothing! You already have it. Otherwise, move on.
2. Is it a built-in module? If so, you can totally have it! Otherwise, move on.
3. Is it located in any of the directories under sys.path? If so, you can have it! Otherwise, sorry - we could not import your file.

Of the 3 steps, the last one is the most complex. 

sys.path is a list of directories. That list is made up of (in exact order):

## 1. Current directory or directory of program

Depends how you start the python program.

If you're calling it inline like this: 

`python -c 'import sys; print(sys.path)'`

Then the value will be "" which represents the current directory.

If you're passing a script to the interpreter, then the value will be the directory of where that script is located.

So if you run `python hey/there/main.py`, then the value will be the absolute path to `hey/there`.

## 2. PYTHONPATH

The second value in the list will be the value of PYTHONPATH if it exists.


`PYTHONPATH='/usr/fuckyou' python -c 'import sys; print(sys.path)'`

This will place PYTHONPTH in front of the current directory value `''`.

## 3. System python installation paths 

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

This path remains the same for *all* of the modules that come into existence once it's constructed, _unless_ it is modified at runtime!

Yes, you heard me - it's modifiable. Updating `sys.path` in a program before importing is a common technique for getting access to what you need.

# from X import Y

Now X can either contain leading dots or no dots.

## With dots

According to the manual: 

> One leading dot means the current package where the module making the import exists. 
 Two dots means up one package level. 
 Three dots is up two levels, etc.

`from .subchild import fork`

## Without dots

If you're using `from X` without dots, then X needs to be in same directory as the main module.

Note: the __main__ module is the entry point of the program.

## With dots

1. This is done by a module in a package. What a package is varies in python 2 and 3.
2. The package it's referring to CANNOT be the __main__ module.

# Notes for myself

Relative imports seems really attractive alternative to not having to update sys.path at runtime for child packages. On the other hand, I also like being able to rely mostly on one style of importing throughout a project. 


* import machinery. seriously - why can't I just import something relatively from a parent directory? it shouldn't be that hard. I want to stop blindly adding extra dots to fix my imports. 


* first, naming files. files named as valid python identifiers and ending in .py can be imported as "modules" by python. these modules are objects with their own namespace. so when u import file X, all the definitions in there are isolated in their own namespace (name of the identifer, or yo ucan name it yourself using alias)
* import statements are just regular python statements. so u can run them in two ways: either inline as command to an interpreter, or in a file. since question here is: how does it find what it needs? how do I make sure it CAN find what it needs? (that's the whole point, right? importing shit u need so you don't need to write ur own shit)
	* lets do inline first, so stuff like python -c 'import whatevershit'. first of all, if you try importing something that obviously doesnt exist, u will get ImportError: no module named BLAH. ok? pretty straight forward. if you now try to import any of the "built-in" aka batteries included shit, you'll get it. always. without fail. also pretty straight forward. the main challenge is getting crap you made into other crap u made right. right. ok. 
		* ok so first it looks at the name and then it says "is this a built in thing?". if so, here ya go. if not, it will start looking for ur shit in a bunch of locations in sys.path. what's sys.path? good question. 

## inline print
This is shit u see if you have PYTHONPATH env set


PYTHONPATH='/usr/fuckyou' python -c 'import sys; print(sys.path)'

['', '/usr/fuckyou', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/gtk-2.0']

see this motherfucking path in the first location? that's where it'll look first. the nit looks at a bunch of system locations pointing to your system python installation.

what the FUCK is the empty value? well that's referring to the current directory. don't believe me, see this fucking line from the documentation: 

>  path[0] is the empty string, which directs Python to search modules in the current directory first

in other words, if u try to run this inline command shit and ur like what the fuck bro I cna't get what I NEED RIGHT NOW FUCK U PYTHON. u need to chill and ask: 'is it in my current directory? nah? ok it located in any of the system paths? (prob not if u made the file). nah? ok so shut the fuck up'

key: all about the sys.paths

## Non-inline print 

PYTHONPATH='/usr/fuckyou' python main.py 

['/home/alin/code/master-python', '/usr/fuckyou', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/gtk-2.0']

So instead of empty dir as first, we got the dir containing the entry point module aka main module. its name is literally main. 


to summarize, here's how sys.paths is constructed from start to end 

-1. module cache (fuck I forgot about this)
0. built ins? 
1. empty dir (current dir) or path of main. depends how u invoke interpreter.
2. PYTHON PATH
3. system python installation paths 

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