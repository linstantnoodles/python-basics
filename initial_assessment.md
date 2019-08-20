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

# syntax error vs type errors

```python
def foo(x):
  if x: 
      return 1 + 'NaN'
  return hello world 5 # Unsupported mix-type operation
```

What's the output of `foo(True)`?

# operator precedence 

## comparison < arithmetic 

`3 * 5 == 5 * 3` equals what?

## multiple comparison operators

`5 < 6 == True` equals what?
`5 < 6 == 6` equals what? 
`3 * 5 == 5 * 3 < 5` equals what?

## multiple arithmetic operators

6 * 5 / 2

## multiple logical / boolean operators

True and False or True

# truthiness and falsiness

```python
Class EmptyClass:
	pass

if [] or {} or "" or range(0) or EmptyClass():
	print('Sup')
```

Will `Sup` get printed?

https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# functions

## lambdas 

```python
my_fn = lambda x: a = x
my_fn(5)
```

Is this a valid program?


```python
(lambda x, y=5: x * y)(5)
```

prints out what? 


## parameter unpacking 

```python
def foo(**args):
	print(args)

foo(1, 2, 3)
```

## arg evaluation once

```
def append_to(element, to=[]):
    to.append(element)
    return to
```


What gets printed? 

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


# dictionary comparisons 

What do each of the following three expressions evaluate to?

1. `{} == {}` 
2. `{'a': 1} > {}`
3. `{} < {}`

# mixed numeric operations

```python
a = 5 * 2
b = 5 / 2
c = 5.0 * 2.0
d = 5.0 * 2 
e = 5.0 / 2
```

# sequence comparisons 


```python
>>> 'alan' < 'alba'
True
>>> 'alan' < 'alan'
False
>>> [1, 2, 3] < [3, 2, 1]
True
>>> [99, 2, 3] < [3, 2, 1]
False
>>> [1, 2, 3] == [1, 2, 3]
True
>>>
```

Which expressions are True? 


# compiling process

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


```python
numbers = [1, 2, 3]
def foo():
  numbers += [5]
  print(numbers)
```

What does `foo()` print?

## function is smallest possible name space creating block

```python
def foo():
  if True:
    a = 5
  print(a)
```

What does this print?

## name resolution 

```python
name = 'Bob'
def foo():
	def nested_foo():
		return name
	return nested_foo()
```

What's the value of `foo()`?

```python
def fn():
    a = 'a'
    b = 'b'
    def nested_fn(a, b, c):
       print('{}, {}, {}'.format(a, b, c))
    nested_fn(7, 11, 'c')
fn()
```

what gets printed?

qq: add one about class attribute 

## Method resolution 


## class attr in hierachy 

class A:
  x = 12

class B(A):
  pass 

print(B.x)

What gets printed ?

## depth first 

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



## Instance method in hierarchy
class A:
  def save(self): 
    print(self)

class B(A):
  pass 

print(B().save())

What gets printed? 

## diamond inheritance 

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

print(D().save())

## diamond special case

class A:
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

print(F().save())

https://python-history.blogspot.com/2010/06/method-resolution-order.html
https://en.wikipedia.org/wiki/Monotonic_function
https://www.python.org/download/releases/2.3/mro/

## class attrs are shared with instances



# iterators 

[1, 2, 3] <- iterable
iter(1, 2, 3) <- iterator + iterable
{} <- iterable
range(5) <- iterable
[x for x in [1, 2, 3]] <- list iterable
(x for x in [1, 2, 3]) <- iterator + iterable


which of the following objects are iterators? which ones are iterables? 


wat does the following print 

next([1, 2, 3])

# function closures 

## updating a variable


def foo():
  x = 5
  def bar(y):
    return y + x
  return bar 

foo()(5) 

The return value of `foo` is the closure.


 while a closure is an instance of a function, a value, whose 

 > non-local variables have been bound either to values or to storage locations (depending on the language; see the lexical environment section below). 

>  if functions with free variables are first-class, then returning one creates a closure.


# first class functions (put with closures??)

TBD

# generators 

## generator function vs generator object (iterator)

```python
def foo():
  for i in range(1, 4):
    yield i 
```

>>> my_gen = foo()


```python
def foo(): 
  print('about to yield 1 ...')
  yield 1 
  print('about to yield 2 ...')
  yield 2 
  print('about to yield 3 ...')
  yield 3
```

my_gen = foo()
```


# decorators (TBD)

# classes 

```
class Foo:
  print('This is foo class')
  def bar(self):
  	print('This is bar method')
```

What gets printed when I run this file? 

```
class Foo:
	print(Foo)
```

What gets printed when I run this one?

# Others

```python
def foo(bar=[]):
  bar.append("baz")
  return bar
```

If I call foo 4 times, what is the rseult?g
https://docs.python-guide.org/writing/gotchas/



## exceptions (TBD)

>>> try:
...     l = ["a", "b"]
...     int(l[2])
... except ValueError, IndexError:  # To catch both exceptions, right?
...     pass
...
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: list index out of range





>>> def create_multipliers():
...     return [lambda x : i * x for i in range(5)]
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...

>>> def create_multipliers():
...     return [lambda x, i=i : i * x for i in range(5)]
...
>>> for multiplier in create_multipliers():
...     print multiplier(2)
...


# Imports TBD