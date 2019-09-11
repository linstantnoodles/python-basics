# names reference values

```python
x = 7
y = x
x = 11
```

What's the final value of `y`?

Answer: names reference values. Assignments update reference to new object.


```python
x = [1, 2, 3]
y = x
x = {}
```

What's the final value of `y`?

Answer: same as above.

# mutable vs immutable objects

```python
x = 7
y = x
x += 1
```

Is x the same object as y? What are their values?

Answer: No. They start out referencing the same thing. The operation didn't mutate the existing object, it created a new one (because integers are immutable).

```python
x = (1, 2)
y = x
x += (3,)
```

Is x the same object as y? What are their values?

Answer: Tuples are immutable. Same idea.

```python
x = 'hello'
y = x
x += ' world'
print(x)
print(y is x)
```

Is x the same object as y? What are their values?

Answer: Strings are immutable. Same idea.

```python
x = []
y = x
x += [1, 2]
```

Is x the same object as y? What are their values?

Answer: They are the same value!

https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists?noredirect=1&lq=1

```python
x = []
y = x
x.append(5)
```

Is x the same object as y? What are their values?

Answer: Same as above! It's a mutation.

# dynamic type checking

```python
def foo(x):
  if x:
      return 1 + 1
  return 1 + 'NaN' # Unsupported mix-type operation
```

What's the output of `foo(True)`?

Answer: 2. Yes we have a bad type operation but type errors only get caught when executed.

# syntax error vs type errors

```python
def foo(x):
  if x:
      return 1 + 1
  return hello world 5
```

What's the output of `foo(True)`?

Answer: It's not 2! Our program actually crashes and throws a syntax error. Syntax errors are caught at _parse_ time.

# operator precedence

## only arithmetic

`3 * 4 - 4` equals what?

Answer: 8. Multiplication has higher precedence than subtraction. The order of operations of mathematics is true here.

## comparison < arithmetic

`3 * 5 == 5 * 3` equals what?

Answer: True! Arithmetic always happens before comparisons are done. This is equivalent to (3 * 5) == (5 * 3).

## multiple comparison operators

`5 < 6 == True` equals what?

Answer: False! You might have guessed that maybe perhaps comparison operaters since they all have equal precedence are left associative. In fact, what this expands to is an _and_  logical expression:  `5 < 6 and 6 == True`. Since the logical operators (and, or, not) are all lower in precedence than the relational operators, what we get is `(5 < 6) and (6 == True)` which is definitely false!

`5 < 6 == 6` equals what?

Answer: Since this is 5 < 6 and 6 == 6, that's True.

`3 * 5 == 5 * 3 < 5` equals what?

Answer: This expands into 15 == 15 and 15 < 5 which is False. Walking through each evaluation (I use parenthesis to show which expressions are evaluated first):

```
(3 * 5) == (5 * 3) < 5
(15) == (15 < 5)
(15 == 15) and (15 < 5)
True and False
False
```

## multiple logical / boolean operators

```python
x = 0 and 0 or 1
y = 1 or 0 and 0
```

What's the value of x and y?

Source: https://stackoverflow.com/questions/16679272/priority-of-the-logical-statements-not-and-or-in-pythonhttps://news.ycombinator.com/

# truthiness and falsiness

```python
Class EmptyClass:
	pass

if 0 or 0.0 or [] or {} or "" or range(0) or EmptyClass():
	print('Sup')
```

Will `Sup` be printed?

https://docs.python.org/3/library/stdtypes.html#truth-value-testing

Answer: Yes! Because all instances of objects are truthy - everything else on the list is false. There are two ways to make a class act false: define a __bool__ method that returns false or a __len__ method that returns 0.

# functions

## lambdas

```python
my_fn = lambda x: a = x
my_fn(5)
```

Is this a valid program?

Answer: No because lambda functions cannot contain assignment statements (or ANY statements for that matter such as if / for / while).


```python
(lambda x, y=5: x * y)(5)
```

Prints out what?

Answer: This immediately invoked lambda prints out 25. It binds 5 to the first argument and multiplies it by `y`.

## parameter packing, unpacking

```python
def foo(**args):
	 print(args)

foo(1, 2, 3)
```

Answer: This will throw an error because double asterisk is meant to unpack dictionaries

```python
def foo(**x):
    print(x)

def bar(x):
    print('{a},{b},{c}'.format(**x))

```

What does `foo(a=1,b=2,c=3)` print? What about `bar({'a': 1, 'b': 2, 'c': 3})`?

Answer: when you use ** in the paramter, it it packs it into a dictionary. When you use it as an argument, it unpacks it into positional arguments.

## unpacking in general

```python
'{}{}'.format(*[1, 2, 3, 4, 5])
```

What does this print?

Answer: 12. Since it unpacks the list into arguments, the first two will be 1 and 2.

```python
a = {'x': 5}
b = {
  **a,
  'y': 10
}
```

What's the value of `b`?

https://www.python.org/dev/peps/pep-0448/

Answer: the value of `b` is ...

```python
{
  'x': 5,
  'y': 10
}
```

## arg evaluation once

```python
def append_to(element, to=[]):
    to.append(element)
    return to
```

If I call `append_to(1)` 3 times, what's the return value of the final call to `append_to`?

Answer: The return value will be `[1, 1, 1]`. When a function is defined, the paramters are evaluated _once_. That means `to` is bound to the object `[]` throughout its lifetime. So every mutation of the original list object will be persisted across calls.

## parameter order

```
def foo(c):
	print(c)

def bar(name=5):
	print(name)

def star(name=5, c):
	print(name)

foo(1)
bar()
star()
```

What gets printed?

Answer: 1, 5, and and error because you can't have positional arguments come after named.

# dictionary comparisons

What do each of the following three expressions evaluate to?

1. `{} == {}`
2. `{'a': 1} > {}`
3. `{} < {}`

Answer: True, Error, Error. Comparisons operators are not supported for dictionaries. The `==` operator evalutes to true if the key and values of the dictionary are equal. It performs a deep comparison.

# mixed numeric operations

```python
a = 5 * 2
b = 5 / 2
c = 5.0 * 2.0
d = 5.0 * 2
e = 5.0 / 2
```

What are the values of a,b,c,e, and e?

Answer: 10, 2.5, 10.0, 10.0, 2.5. Maybe you're suprised that 5 / 2 is a float, well in python 3 it performs float division by default. Second point is that when you mix float and integer, it's always float (narrower value expands to wider? )

# sequence comparisons

```python
a = 'alan' < 'alba'
b = 'alan' < 'alan'
c = [1, 2, 3] < [3, 2, 1]
d = [99, 2, 3] < [3, 2, 1]
e = [1, 2, 3] == [1, 2, 3]
```

Which expressions are True?

Answer: a, c, and e. Python uses lexicographic comparison on lists. So it compares first of each, then second of both, etc.

# scope

## Assignments always go to local scope

```python
name = 'Joe'
def foo():
	name = 'Bob'
	return name

print(foo())
print(name)
```

What gets printed?

Answer: 'Bob' and 'Joe'. Assignments always go to the local scope, regardless of whether or not there's the same name in an enclosing scope. So the local namespace gets a new binding.


```python
numbers = [1, 2, 3]
def foo():
  numbers += [5]
  print(numbers)
```

What does `foo()` print?

Answer: There will be an `UnboundLocalError` because assignments expect the name to be in local scope. `+=` contains an assignment, so `numbers` is expected to exist locally.

https://docs.python.org/3/faq/programming.html

> If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.

## function is smallest possible name space creating block

```python
def foo():
  if True:
    a = 5
  print(a)
```

What does this print?

Answer: 5. `a` is visible to the entire function. `if` does not create a new namespace.

## name resolution

```python
name = 'Bob'
def foo():
	def nested_foo():
		return name
	return nested_foo()
```

What's the value of `foo()`?

Answer: `Bob`. The lookup is local, nearest enclosing function, then global.

```python
def fn():
    a = 'a'
    b = 'b'
    def nested_fn(a, b, c):
       print('{}, {}, {}'.format(a, b, c))
    nested_fn(7, 11, 'c')
fn()
```

What gets printed?

Answer: 7, 11, 'c'. The local parameters mask the ones in the enclosing function.


```python

```

## class attr in hierachy

```python
class A:
  x = 12

class B(A):
  pass
```

What's the value of `B.x`?

Answer: `12`. It will look up `x` in class `B` and since it can't find it, it will look for it in the parent.

## Method resolution

```python
class A:
  def save(self):
    print('Hello!')

class B(A):
  pass
```

What's printed by `B().save()`?

Answer: `Hello!` gets printed. It will look up the instance method on the parent class.

## multiple inheritance: depth first

```python
class A():
  def save(self):
    print('A.save')

class B(A):
  pass

class C():
  def save(self):
    print('C.save')

class D(B, C):
  pass
```

What gets printed by invoking `D().save()`?

Answer: `A.save`. 

## diamond inheritance

```python
class A:
  def save(self):
    print('A.save')

class B(A):
  pass

class C(A):
  def save(self):
    print('C.save')

class D(B, C):
  pass
```

What gets printed by `D().save()`? 

Answer: `C.save`. Did that suprise you? If we were to follow the depth first rule, we should have seen `A.save` printed. In reality, python will look up the name in more specialized (less general, more concrete) parent first if they both share the same ancestor.

## diamond special case

```python
class A(object):
  def save(self):
    print('A.save')

class B(A):
  def save(self):
    print('B.save')

class C(A):
  def save(self):
    print('C.save')

class D(B, C):
  pass

class E(C, B):
  pass

class F(D, E):
  pass
```

What gets printed by `F().save()`?

Answer: This program will actually return an error at parse time.

```python
TypeError: Cannot create a consistent method resolution
order (MRO) for bases B, C
```

Python has a method resolution order algorithm that detects ambiguity in the inheritance chain. In this case, D comes before E so we expect to look up D first. But should we look at B first or C first? There's order disagreement between `D` and `E`. Previously, this was allowed but it leads to inconsistent behavior (sometimes a method in C gets called first, other times it's a method in B). Now, inconsistency in order is no longer allowed.

Resources:

https://python-history.blogspot.com/2010/06/method-resolution-order.html
https://en.wikipedia.org/wiki/Monotonic_function
https://www.python.org/download/releases/2.3/mro/

## class attrs are shared with instances

```python
class A:
  x = 1

class B(A):
  pass 

class C(A):
  pass

print("{}, {}".format(B.x, C.x))
A.x = 12 
print("{}, {}".format(B.x, C.x))
```

What gets printed?

Answer: 

>>> print("{}, {}".format(B.x, C.x))
1, 1
>>> A.x = 12 
>>> print("{}, {}".format(B.x, C.x))
12, 12

# iterators vs iterables

Given the following objects:

```
a = [1, 2, 3]
b = iter(1, 2, 3) 
c = {} 
d = range(5) 
e = [x for x in [1, 2, 3]]
f = (x for x in [1, 2, 3])
```

Which ones are strictly iterators?
Which ones are strictly iterables? 
Which ones are both iterators and iterables? 

Answer: a, c, d, and e are strictly iterables. b and f are both iterators and iterables.  All iterators are iterables, but not all iterables are iterators. There are no objects that are strictly iterators. All the built-in iterators are _also_ iterables in python (because you can call `__iter__` on them!).

What happens if you evaluate `next([1, 2, 3])`?

Answer: You get a type error because the list object is not an iterator!

# function closures

```python
def foo():
  x = 5
  def bar(y):
    return y + x
  return bar
```

What's the value of `foo()(5)`?

Answer: 10! The return value of `foo` is the closure. It has references to non-local variables (free variables). The `y` is the free variable.

```python
def foo():
  x = 5
  def bar(y):
    x += y
  bar(10)
  print(x)
```

What's wrong with this program? If we wanted `print(x)` to output `15`, what change in `bar` will be required? 

Answer: The `nonlocal` keyword will be required. See https://www.python.org/dev/peps/pep-3104/.

# generators

```python
def foo():
  yield 1
  yield 2
```

What gets returned by `foo()`?

# classes

```python
class Foo:
  print('This is foo class')
  def bar(self):
  	print('This is bar method')
```

What gets printed when I run this file?

Answer: 'This is foo class' will get printed because the body of the function is evaluated at runtime.

```python
class Foo:
	print(Foo)
```

What gets printed in this program? 

Answer: Nothing - you get a name error because `Foo` is not yet defined. The class only exists after the entire body has been parsed (hence anything inside the body that attempts to refer to the class during parse time will fail).

# Others

```python
def foo(bar=[]):
  bar.append("baz")
  return bar

foo()
foo()
foo()
```

What's the result of the final call to `foo` above? 

Answer: ['baz', 'baz', 'baz']. Parameter are evaluated once during function creation - not on every invocation.

https://docs.python-guide.org/writing/gotchas/

## Exception handling

```
try:
  x = [1, 2, 3]
  x[3] + 'NaN'
except TypeError, IndexError:
  pass
```

What happens when this is executed?

Answer: A syntax error gets thrown. You need to wrap the exceptions in a parenthesis (a tuple).

# Decorators

```python
def like_a_boss_decorator(fn):
  def wrapper(*args, **kwargs):
    return "{}, like a boss".format(fn(*args, **kwargs))
  return wrapper  

@like_a_boss_decorator
def action():
  return "Eating"
```

What is the value of `action()`?

Answer: `Eating, like a boss`. The function is decorated by the wrapper which calls it with the extra text. Like a boss.

# Imports 

Which of the following performs a relative import?

```python
import bob
from bathroom import bob 
from .bathroom import bob 
```

Answer: only the last one (containing leading dot) is a relative import. The first two perform absolute imports. While `import bob` will attempt to find the module `bob` using the absolute import lookup process, `from bathroom import bob` will attempt to find the package `bathroom` first using the same process. 

# Process

1. Send a link for payment 
2. Receieve assessment with instructions 
3. Once assessment complete, option to book / schedule a session

- what would i want the session to look like? i would want it tailored to my weaknesses. That means for each area, there should be exercises that Im provided with to ensure that I actually improve / elevate my skills. 
4. Hour 1: Go through answers. Hour 2: Wild card?


Or 

1. Start assessment right away. Go through it live. 