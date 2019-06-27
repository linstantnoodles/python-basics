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