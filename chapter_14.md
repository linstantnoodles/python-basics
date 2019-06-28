# Generators

Here's a definition of a function that returns a single value.

def foo(): 
	return 1

 When I run this program, we expect see the number 1 printed.

>>> foo()
1

Now if we replace the return keyword with the yield keyword, invoking the function returns an object of type generator.

def foo(): 
	return 1

>>> foo()
<generator object foo at 0x7f26280da0f8>

Now lets go over definitions:

1) Any function definition containing the yield keyword is a _generator function_.
2) Calling the generator function returns a _generator object_. 

Side note: _Both objects are loosely referred to colloquially as "generators" so you will need to use context to infer which one people mean._

## The generator object

The generator objects implements a __next__ method. Therefore, this object is an iterator! In python, calling __next__ is a way of retrieving values from an iterator. 

Here's an example of calling __next__ multiple times on this generator object.

>>> my_gen = foo()
>>> my_gen
<generator object foo at 0x7f26280da150>
>>> my_gen.__next__()
1
>>> my_gen.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

Each time we call __next__, the generator function executes the statements in the body. Just like a typical function call!

During execution, it either encounters a yield statement or it doesn't. 

If it encounters a yield statement, the value in from of yield becomes the return value of __next__. We can say that the value was yielded. Before the value is yielded, the state of the function is saved (to be resumed in the next (no pun intended) call to `__next__`)

If it does _not_ encounter a yield statement, a `StopIteration` error is raised to indicate that there are no values left to return.

Essentially, what we have here is a resumable function. It returns something once, and can return something else at another point in time.

Here's an example of returning more than one value from a generator:

def foo(): 
	print('about to yield 1 ...')
	yield 1 
	print('about to yield 2 ...')
	yield 2 
	print('about to yield 3 ...')
	yield 3

>>> my_gen = foo()
>>> my_gen.__next__()
about to yield 1 ...
1
>>> my_gen.__next__()
about to yield 2 ...
2
>>> my_gen.__next__()
about to yield 3 ...
3
>>> my_gen.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

We can also transform this to a loop to avoid having to define yield multiple times

```python
def foo():
	for i in range(1, 4):
		yield i 
```

>>> my_gen = foo()
>>> my_gen.__next__()
1
>>> my_gen.__next__()
2
>>> my_gen.__next__()
3
>>> my_gen.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


## Generators in practice

While calling __next__ repeatedly is a way to retrieve values from generator iterators, it's typically not used in real world code. If I wanted to print all values for this function, I’d have to either write __next__ N times or write a loop to call __next__.

I'm only using it to highlight this defining behavior: that you can retrieve values over different points in time during program execution from a generator function. This is different from the typical behavior of functions, which return values at one point in time during program execution.

In practice (which is to say in the real, professional world), generator iterators are often used in for loops just like any other iterator. For statements expect iterators and take care of repetedly calling __next__ and handling StopIteration errors.

So if we rewrote our statement to be a for loop, we'll see all numbers printed without having to worry about calling __next__ ourselves or handling the StopIteration error.

```python
>>> for i in foo():
...     print(i)
... 
1
2
3
```

In practice, it's sometimes hard to tell whether we're iterating through a container or a generator function unless you have the full context of the code. And I think that's great because as a client of a generator object, I really do not need to know whether it's a container or generator. The same benefits of abstraction of the iterator pattern extends to these generator objects and that's a good thing.

## Why use them? 

Generators are great for returning elements _lazily_. Lets consider a function that returns a number of fibonacci numbers. Lets say we have a client that wants to perform some type of transformation on fibnacci numbers (square them)


```python
def fib(count):
    results = []
    a, b = 0, 1
    for n in range(0, count):
        if n == 0: 
            results.append(a)
        elif n == 1:
            results.append(b)
        else:
            a, b = b, a + b 
            results.append(b)
    return results
```

>>> def fib(count):
...     results = []
...     a, b = 0, 1
...     for n in range(0, count):
...         if n == 0: 
...             results.append(a)
...         elif n == 1:
...             results.append(b)
...         else:
...             a, b = b, a + b 
...             results.append(b)
...     return results
... 
>>> 
>>> fib(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> 


So this function generates each fib, adds it to a list and returns. This looks good. But what if we have too many numbers to hold in memory? Or if we're not just dealing with a large list of numbers but custom objects that have much higher memory footprints? 

One approach without generators is to simply perform the operation as the numbers become available. This often involves putting the operation in the inner loop of whatever is generating the elements. For example 

for n in range(0, count):
	if n == 0:
		square(a)
	elif n == 1:
		square(b)
	else: 
		a, b = b, a + b 
		square(b)


While this may be fine for cases where the client only needs to operate based on that one input, things get messy when the operation needs to track state (free variables) from outside the function. perhaps it also wants to keep a running count or a list of what it's seen. 

def square(x):
	counter += 1
	return x * x

what you have then is an op passed into the producer that operates on some data in an outside context. this isn't wrong per se, but it's awkward and makes code hard to understand because we're forced to include all the state management in our callback that's passed to fib.

```python
def fib(count):
    a, b = 0, 1
    for n in range(0, count):
        if n == 0: 
            yield a
        elif n == 1:
            yield b 
        else:
            a, b = b, a + b 
            yield b
```

>>> def fib(count):
...     a, b = 0, 1
...     for n in range(0, count):
...         if n == 0: 
...             yield a
...         elif n == 1:
...             yield b 
...         else:
...             a, b = b, a + b 
...             yield b
... 
>>> fib(10)
<generator object fib at 0x7f4bd34e8eb8>
>>> results = fib(10)
>>> list(results)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> 

the call to list actually does the iteration for us and returns a list. of course this ends up taking same amount of memory as other one but this is mostly just to show you that the contents are same. you can trust me that the actual elements were retrieved lazily (meaning fib did not generate all of them upfront)

contrast this with this approach. 

not only do we get the benefits of just dealing with one element at a time, we don't need to pass in some function itno the producer and add more complexity to that level. we can deal with it in the outside context and performs w.e state changes we need.
            
