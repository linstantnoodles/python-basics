# names reference values 

```python
x = 7 
y = x 
x = 11
```

What's the final value of `y`?


```python
x = [1, 2, 3]
y = x 
x = {}
```

What's the final value of `y`?

# mutability 

```python
x = 7
y = x
print(y is x)
x += 1
print(y is x)  
```

What are the values of the two print statements? 

```python
x = (1, 2)
y = x 
x += (3,)

```

```python
x = 'hello'
y = x 
x += ' world'
print(x)
print(y is x)
```

```python
x = []
y = x 
x += [1, 2]
print(y)
print(x)
print(y is x)
```

```python
x = []
y = x 
x.append(5)
print(y)
print(x)
print(y is x)
```

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

## parameter unpacking 

```python
def foo(**args):
	print(args)

foo(1, 2, 3)
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


# iterators 

# function closures 

# first class functions

# generators 

# decorators

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

 def foo(bar=[]):        # bar is optional and defaults to [] if not specified
...    bar.append("baz")    # but this line could be problematic, as we'll see...
...    return bar




>>> class A(object):
...     x = 1
...
>>> class B(A):
...     pass
...
>>> class C(A):
...     pass
...
>>> print A.x, B.x, C.x
1 1 1

Makes sense.

>>> B.x = 2
>>> print A.x, B.x, C.x
1 2 1

Yup, again as expected.

>>> A.x = 3
>>> print A.x, B.x, C.x
3 2 3


## exceptions

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


- imports. when a file masks a module
- 