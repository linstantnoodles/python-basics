# Questions

## Question 1

```python
x = 7 
y = x 
x = 11
```
What's the final value of `y`? Why?

## Question 2

```python
def foo(x):
  if x: 
      return 1 + 1
  return 1 + 'NaN' # Unsupported mix-type operation
```
What's the output of `foo(True)`?

## Question 3 

```python
numbers  = [1, 1, 2, 3, 5]
for x in numbers:
    x = x * x 
```
Once the loop terminates, what's the value of `x`? What's the value of `numbers`? 

## Question 4

Which one of the following creates name-bindings?
```python
# A
import x
# B
from x import y
# C
def foo(): 
    pass
# D
class Boo():  
    pass 
# E
for x in some_list:
    pass
# F
x = 5
```

## Question 5 

```python
a = 5 * 2
b = 5 / 2
c = 5.0 * 2.0
d = 5.0 * 2 
e = 5.0 / 2
```
What's the value of a, b, c, d, and e? 

## Question 6

What do each of the following three expressions evaluate to?
1. `{} == {}` 
2. `{'a': 1} > {}`
3. `{} < {}`

## Question 7 

```python
class A():
    pass
```

What is the value of `A() == A()`?

## Question 8 

```python
class Lamp
    def turn_on():
        print("Turning on the Lamp") 
class Computer:
    def turn_on():
  print("Turning on the Computer")
  
x = Lamp() 
x.turn_on()
x = Computer() 
x.turn_on() 
```

Will this program run without any errors? Why or why not?

## Question 9 

What's the minimum and maximum value of an integer on a 32 bit machine?

A)  -2147483648 and 2147483647
B) No defined maximum. The precision is arbitrary and is limited by memory available
C) -9999999999999999999 and 9999999999999999999

## Question 10 
```python
x = 7
y = x
print(y is x)
x += 1
print(y is x)  
```
What are the values of the two print statements?

# Explanations
# Questions

## Question 1

```python
x = 7 
y = x 
x = 11
```
What's the final value of `y`? 

## Question 2

```python
def foo(x):
  if x: 
      return 1 + 1
  return 1 + 'NaN'
```
What's the output of `foo(True)`?

## Question 3 

```python
numbers  = [1, 1, 2, 3, 5]
for x in numbers:
    x = x * x 
```
Once the loop terminates, what's the value of `x`? What's the value of `numbers`? 

## Question 4

Which one of the following creates name-bindings?
```python
# A
import x
# B
from x import y
# C
def foo(): 
    pass
# D
class Boo():  
    pass 
# E
for x in some_list:
    pass
# F
x = 5
```

## Question 5 

```python
a = 5 * 2
b = 5 / 2
c = 5.0 * 2.0
d = 5.0 * 2 
e = 5.0 / 2
```
What's the value of a, b, c, d, and e? 

## Question 6

What do each of the following three expressions evaluate to?
1. `{} == {}` 
2. `{'a': 1} > {}`
3. `{} < {}`

## Question 7 

```python
class A():
    pass
```

What is the value of `A() == A()`?

## Question 8 

```python
class Lamp
    def turn_on():
        print("Turning on the Lamp") 
class Computer:
    def turn_on():
  print("Turning on the Computer")
  
x = Lamp() 
x.turn_on()
x = Computer() 
x.turn_on() 
```

Will this program run without any errors? Why or why not?

## Question 9 

What's the minimum and maximum value of an integer on a 32 bit machine?

A)  -2147483648 and 2147483647
B) No defined maximum. The precision is arbitrary and is limited by memory available
C) -9999999999999999999 and 9999999999999999999

## Question 10 
```python
x = 7
y = x
print(y is x)
x += 1
print(y is x)  
```
What are the values of the two print statements? 

# Explanations

## Question 1

The final value of y is 7.

One common misconception around the process of why this happens is that:

1. `x` is initially storing the value `7` 
2. `y = x` causes `7` to be copied to `y`.

Since the variables store separate copies of the integer, any further assignments to `x` will not affect the value of `y`. While it's generally true that variable assignments in python happen independently, how it happens is very different from above. 

What's really happening is: 

1. `x` is initially referencing the object `7`
2. `y = x` causes `y` to reference whatever `x` is refrencing, which is the object `7`
3. `x = 11` changes `x` to reference the object `11` 

The names in python exist separately from the values - they're more akin to C pointers (but not quite, as I'll explain below) rather than C variables (where the actual value is stored at the location of the variable). The names have no reference of each other - assigning variables to each other just makes it so that they reference the _same_ object. Since the names reference the objects directly, any updates to those references will happen independently. 

### Frequently asked questions: 

**Um, how do I know you're not bullshitting me? How do I know for sure values aren't being copied??**

Lets test the explanation using python itself...

The functions we'll be using are: 

id() (https://docs.python.org/3/library/functions.html#id)
sys.getrefcount() (https://docs.python.org/dev/library/sys.html#sys.getrefcount)

`id` is basically the address of the object. It will be unique for every object. When you call `id` on a name, it gets you the address of the object it's referencing (not the address of the name!). `getrefcount` will get the number of names referring to an object. I'm going to demonstrate how the refcount for an integer object changes as we add more assignments. 

```python
>>> import sys
>>> id(1)
10910400
>>> sys.getrefcount(1)
806
>>> x = 1
>>> id(x)
10910400
>>> sys.getrefcount(1)
807
>>> y = x
>>> id(y)
10910400
>>> sys.getrefcount(1)
808
>>> x = 2
>>> sys.getrefcount(1)
807
```

So as you can see, we're dealing with the same object throughout this experiment (as proven by the outputs of `id`). When we did `y = x`, the refcount went up by one (because `y` is now also pointing at our integer object `1`). Finally, the refcount gets decremented when we update `x` to reference `2` which is a different object.  

If `y = x` was merely copying values, there would be no change in the refcount. 

**Okay so what you're describing sounds a lot like pointers to me - are python variables basically C pointers?**

The short answer is ...kind of, but not really. For a longer, better answer check out this answer on quora: https://qr.ae/TWvjiB

## Question 2 

The return value of `foo(True)` is `2`.

Python performs [dynamic type checking](https://en.wikipedia.org/wiki/Type_system#Dynamic_type_checking_and_runtime_type_information). What that means is that it associates type information with values at runtime. Put another way, it only cares about the type of a value when it tries to use it. Since the unsupported operation is never used, the function returns without error! 

Now lets execute the unsupported operations in the REPL and see what happens: 

```bash
>>> if True: 
...     1 + 'NaN'
... else:
...     1 + 1
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Now that we're actually executing the line where we're performing an unsupported mix-type operation, the type error is thrown.

### FAQ

**Does this mean I can type anything in regions of code that won't be executed?** 

Not quite - you can't run a program if it contains syntax errors even if you put them where they won't be executed. For example: 

This program is correct by pythons syntax: 

```python
if True:
    1 + 1
else:
    icandowhateveriwanthereright+=1
```

Even though `icandowhateveriwanthereright` might not be defined, it's a syntactically correct expression so this program will execute without error. 

On the other hand ... 

```python
if True:
    1 + 1
else:
    icandowhat   ++ everiwanthereright+=1
```

Will throw:

```
...
  icandowhat   ++ everiwanthereright+=1
SyntaxError: can't assign to operator
```

One way to think about why syntax errors are thrown in the `else` but not type errors is in terms of the stages of compilation. 

Generally speaking, for any language source code there's a lexing step followed by the parsing step (where the tokens are used to form an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)) and then followed by the evaluation step. The parsing step is where errors in program grammar is caught. If you have a program without a valid structure, there's really no point in trying to evaluate it.

Note: I'm not familiar with whether python uses a single-pass, multi-pass compiler, or something else. So while I'm describing the lexing, parsing, and eval steps as though python uses a multi-pass compiler, let me know if that's not the case.

**Does't python know how to "byte-compile" files with extensions `.pyc`? Can it not report type errors during that process?**

Not really. The compiled files are generated _after_ the program is executed for optimization reasons and the type checking behavior during those steps are no different then when python is not generating those files. 