# Table of Contents

Numeric types and arithmetic operations
Ordered container (sequence) types and operations 
Unordered container types and operations
Operations - these can involve both numeric and container types 
Membership
Logical
Type checking
You probably shouldn’t (http://www.voidspace.org.uk/python/articles/duck_typing.shtml#id1) 
But you can check for instance with isinstanceof and type(x)
Common conversions / Casting 
String to numeric and reverse 
X to string 
Splitting a string into a list 


[Purpose](https://github.com/hillaryfraley/jobbriefings#purpose)

[Scope](https://github.com/hillaryfraley/jobbriefings#scope)

[Work Practice](https://github.com/hillaryfraley/jobbriefings#work-practice)

* [Daily Briefing](https://github.com/hillaryfraley/jobbriefings#daily-briefing)
     - [Daily Briefing Requirements](https://github.com/hillaryfraley/jobbriefings#daily-briefing-requirements)
     - [Daily Briefing Documentation](https://github.com/hillaryfraley/jobbriefings#daily-briefing-documentation)
* [Job Site Assessment](https://github.com/hillaryfraley/jobbriefings#job-site-assessment)
     - [Job Site Assessment Requirements](https://github.com/hillaryfraley/jobbriefings#job-site-assessment-requirements)
     - [Job Site Assessment Documentation](https://github.com/hillaryfraley/jobbriefings#job-site-assessment-documentation)
* [Job Briefing](https://github.com/hillaryfraley/jobbriefings#job-briefing)
     - [Job Briefing Requirements](https://github.com/hillaryfraley/jobbriefings#job-briefing-requirements)
     - [Job Briefing Documentation](https://github.com/hillaryfraley/jobbriefings#job-briefing-documentation)
* [Post-Job Briefing](https://github.com/hillaryfraley/jobbriefings#job-briefing)  
     - [Post-Job Briefing Requirements](https://github.com/hillaryfraley/jobbriefings#job-briefing-requirements)
     - [Post-Job Briefing Documentation](https://github.com/hillaryfraley/jobbriefings#job-briefing-documentation)


The purpose of this first section is to get you quickly up to speed and situated with just the most important things you need to know about Python built-in types. It's 80% of what you need to know about types to be pretty productive and have a starting point from which you can build more depth as you use the language.

It's broken down into three parts: 

1. Table of contents 
2. Speed guide
3. Quizzes and exercises  

Prerequisites: 

* You've written programs in python or other languages 
* You have Python 3 installed and know how to execute python files and use the interpreter

## Speed guide 

### Type system traits

3 keys things you should know about the type system:

1. Python is a dynamically type checked language; the values you define in your program are only associated with their types at runtime.

What this translates to in practice is:

A) You don't need to declare types upfront! 

Here's an example of an assignment statement where we bind the number `7` to the name `foo`

```bash
>>> foo = 7
>>> print(foo)
7
```

B) Type errors resulting from unsupported operations between values don't get thrown until that code is executed

Here's what happens when I try to add an integer to a string: 

```bash
>>> x = 15
>>> y = 'not a number'
>>> x + y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
]]['
']
```

2. Python is duck typed. Does it quack like a duck? Then go ahead and treat it like a duck.

You can ask an object to do X if it knows how to do X regardless of what type it's associated with during program execution. [Here's](https://en.wikipedia.org/wiki/Duck_typing) a great example.

Aside: [PEP-3107](https://www.python.org/dev/peps/pep-3107/) introduced type annotations that can allow third party tools to perform static analysis. 

3. No implicit type conversions (aka type coersion). Coercions got [removed in Python 3](https://docs.python.org/3/whatsnew/3.0.html?highlight=coerce#builtins) and that's good news!

### Built-in types 

Numeric types 

Lets go over the most common built-in numeric types: integers and floats. There are other ones like complex numbers but we're gonna ignore them here unless people demand that I cover them.

1. Integer

Integers have arbitrary [precision](https://en.wikipedia.org/wiki/Precision_(computer_science)). Have lots of memory on your machine? Fantastic, you can use gigantic numbers without having to reach for a separate BigInt class like those java people. 

In practice, you shouldn't run into limits.

2. Float 

Unlike integers, floats do not have arbitrary precision and there are pre-defined limits set by your machine. Floats are implemented using C doubles. [sys.float_info](https://docs.python.org/3/library/sys.html#sys.float_info) provides more details about the float type available on your platform.

Running this on my machine I get:

```
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```

max is the maximum float value and min is the minimum float value. If you exceed the maximum, you'll get an `infinity` "float" type. If you dip below the minimum, you'll get `-infinity`. While this is one of those good to knows, most of you _probably_ won't exceed either bounds in practice (I never have).

### Arithmetic operations

All the operations between like-numeric types produce what you would usually expect. 

2 + 1 = 3
3 * 5 = 15

int ARITHMETIC OPERATOR int produces and int

The only difference is division for integers. It results in a float. To do an integer division, use //.

Python also supports mixed arithmetic:

From [python docs](https://docs.python.org/2.4/lib/typesnumeric.html):
> Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the "narrower" type is widened to that of the other, where plain integer is narrower than long integer is narrower than floating point is narrower than complex.


Take addition for example: 

```bash
>>> 5+5
10
>>> 5.0 + 5.0
10.0
>>> 5 + 5.0
10.0
>>> 5.0 + 5
10.0
```

As you can see in the case of FLOAT + INTEGER. Since the float is wider, the int becomes a float and hence the final answer is a float. This is true for all five operations for all version of python.

python 3.x 
```bash
>>> 10 / 5
2.0
```

So in python 3.x, `/` is float division instead of integer division. To do integer division, use `//` in python3 (also true in Python 2).


Precedence of arithmetic operators follows the same [orders of operations in math](https://en.wikipedia.org/wiki/Order_of_operations).

1. exponents and roots
2. multiplication and division
3. addition and subtraction 

Here's an example illustrating the precedence rules at work: 

```bash
>>> 2 + 5 * 3**2 / 1
47
```

### Overriding precedence

As you would expect in most languages, any precedence rule can be overriden by wrapping expressions in parenthesis. This is true in math and it's also true in Python. So if we really wanted to perform the addition of `2 + 5` first, we would wrap it in parenthesis so it's `(2 + 5)`.


Arithmetic operators are also not the only operators in python subject to precedence rules. I won't cover them here but the python documentation has a quick reference [precedence table](https://docs.python.org/3/reference/expressions.html#operator-precedence).

# Boolean

Boolean are of their own type `bool` (introduced in [PEP-0285](https://www.python.org/dev/peps/pep-0285/) back in 2002) but are subclasses a integer so technically it's also a numeric type - you can look at it as just a special case numeric. I prefer calling it by its more specific type rather than calling it numeric because they're so different in their function in programs.

None 

This is a singleton type - this is pythons "NULL". You can't perform any operations with None.



Next step: come up with quizes for each subtopic + drills / exercises (if it makes sense). 

Types 
Certain languages, for example Clojure, Common Lisp, or Cython are dynamically type-checked by default, but allow programs to opt into static type checking by providing optional annotations. O

Type checking 

Scale vs precision 


arbitrary precision integers
What’s the precision of python integers? Unlimited. 
Integer division 
Float / int? Int / float? What do you get? 
Float operations mix with integer across all operators - what’s in common? 

From [python docs](https://docs.python.org/2.4/lib/typesnumeric.html):
> Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the "narrower" type is widened to that of the other, where plain integer is narrower than long integer is narrower than floating point is narrower than complex.

o integer division, use `//` in python3 (

Floats: 
Floats are implemented using C doubles. sys.float_info provides more details about the float type available on your platform. https://docs.python.org/3/library/sys.html#sys.float_info.

Running this on my machine I get:

```
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```

Order of operations? 

Precedence of arithmetic operators follows the same [orders of operations in math](https://en.wikipedia.org/wiki/Order_of_operations).

1. exponents and roots
2. multiplication and division
3. addition and subtraction

Here's an example illustrating the precedence rules at work:

```bash
>>> 2 + 5 * 3**2 / 1
47
```

Common container operations 

What makes a sequence a sequence 

1. Ordered
2. Supports membership testing (is this element a member of this sequence?)
2. Members are index addressable (give me the 5th index of this sequence)

Mylist[x]
Mylist[0:5]
Mylist + hilist and mylist * number
>>> 2 * [2]
[2, 2]
>>> [[1]] * 2
[[1], [1]]
>>> [{}] * 2
[{}, {}]
>>> [{'a': {'b': 2}}] * 2
[{'a': {'b': 2}}, {'a': {'b': 2}}]

Stack and queue operations: 
List.append
List.pop
https://www.geeksforgeeks.org/using-list-stack-queues-python/

Deleting a list:

Common dictionary operations

Map[key]

Common set operations
Common for all of them
Identity, relational, logical 
General precedence operator rules: Arithmetic operators are also not the only operators in python subject to precedence rules. See the docs for a the complete operator [precedence table](https://docs.python.org/3/reference/expressions.html#operator-precedence).

elements.insert
elements.remove

so we have two optios - either take away elements from the existing list or add
of course, we can also replace an existing element by setting via index:

elements[5] = 'something else '

since all container types are by definitions index addressable, they all support this same interface (confirm)

https://stackoverflow.com/questions/11277432/how-to-remove-a-key-from-a-python-dictionary

Sets 

## Set operations

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}