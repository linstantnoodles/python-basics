# Functions

## Subroutines, Functions, Purity

While many programming languages (such as python) use the word **function** from mathematics to represent [subroutines](https://en.wikipedia.org/wiki/Subroutine), they often do not share the properties of mathematical functions.

One definition of a mathematical function from wikipedia is: 

> A function is a process or a relation that associates each element x of a set X, the domain of the function, to a single element y of another set Y (possibly the same set)

Many exceptions to this abound in python functions. 

For example, here's a function definition that accepts an argument `x` and returns a different value each time.

```python
counter = 0
def greeting(x):
    global counter 
    y = counter + x 
    counter += 1 
    return y 
```

Now lets invoke it multiple times: 

```python
>>> greeting(0)
0
>>> greeting(0)
1
>>> greeting(0)
2
>>> greeting(0)
3
```

The same input `x` maps to multiple outputs `y` so it does not fit the definition of a mathematical function. Furthermore, there's no rules around what set `x` must belong to because python is a dynamically typed language. You can just as easily pass in a string like `greeting('sup')`, in which case an exception might be thrown and nothing is returned at all!

Even if we did have constraints around input, python still doesn't have [pure functions](https://en.wikipedia.org/wiki/Pure_function) because it allows its subroutines to reference global, mutable state.

Nevertheless, the programming world continues to use the word `function` to describe subroutines. Even though the word implies properties that subroutines do not have, I will use the word because that's in the official python spec. However, keep in mind that when we use the word `function`, what we really mean is *subroutine* or *impure function*.

## First class citizens

Python functions are [first class](https://en.wikipedia.org/wiki/First-class_function). They're objects that can be passed around as arguments just like any other object.

```python
def do_map(fn, elements):
    result = []
    for i in elements:
        result.append(fn(i))
    return result

def square(x):
    return x * x
```

Now lets invoke `do_map` by passing in `square`: 

```bash
>>> do_map(square, [2, 4])
[4, 16]
```

## Types of functions

There's two types of function you can create in python: compound functions and anonymous functions (lambdas). 

### Compound functions

Compound functions are the most common. Here's an example of one: 

```python
def greeting():
    a = 'hello '
    b = 'world'
    return a + b
```

The bodies of compound functions can contain any number or types of expressions or statements. Including other function definitions.

```python
def parent():
    def child():
        print("im the child")
    child()
    print("im the parent")
```

As you can see, a function doesn't necessarily need to return a value. However, it _does_ need to have something in the body. If you absolutely need a placeholder for the actual implementation (a common need for some TDD practitioners), just use the keyword `pass`. This will make the function to return `None`.

### Anonymous functions (lambdas)

These are less common, but very useful in situations where you want a single-use function. 

For example: 

```bash
>>> do_map(lambda x: x * x, [2, 4])
[4, 16]
```

You're allowed to bind lambda functions to names as well.

```bash
>>> square_function = lambda x: x * x
>>> do_map(square_function, [2, 4])
[4, 16]
```

Unlike compound functions, you're only allowed to have a single expression in the body of a lambda, and statements (such as assignment statements or control flow statements) are not permitted. 

```bash
>>> lambda x: a = x
  File "<stdin>", line 1
SyntaxError: can't assign to lambda
```

### Parameters

Compound functions support both positional parameters and named parameters. Lambda functions only support positional parameters.

#### Compound function parameters

**Positional** 

```bash
>>> def foo(a):
...     print(a)
... 
>>> foo(1)
1
>>> def foo_two(a, b):
...     print(a)
...     print(b)
... 
>>> foo_two(1, 2)
1
2
>>> 
```

**Named** 

```bash
>>> def foo(a=None):
...     print(a)
... 
>>> foo(1)
1
>>> foo()
None
>>> def foo_two(a=None, b=2):
...     print(a)
...     print(b)
... 
>>> foo_two(1, 3)
1
3
>>> foo_two()
None
2
```

**Both** 

```bash
>>> def foo(a, b, c=1, d=2):
...     print(a)
...     print(b)
...     print(c)
...     print(d)
... 
>>> foo('hello', 'world')
hello
world
1
2
>>> foo('hello', 'world', c=5, d=7)
hello
world
5
7
>>> 
```

**Parameter unpacking**

This is useful when you need to pass in a variable number of either positional arguments or keyword arguments. Prior to python 3.7 the [limit to the number of arguments](https://stackoverflow.com/questions/714475/what-is-a-maximum-number-of-arguments-in-a-python-function) was 255. 

Unpacking positional arguments: 

```bash
>>> def foo(*args):
...     print(args)
... 
>>> foo(1, 2, 3, 4)
(1, 2, 3, 4)
```

Unpacking keyword arguments:

```bash
>>> def foo(**kwargs):
...     print(kwargs)
... 
>>> foo(a=5, b=12)
{'a': 5, 'b': 12}
```

Unpacking both positional and keyword arguments: 

```bash
>>> def foo(*args, **kwargs):
...     print(args)
...     print(kwargs)
... 
>>> foo(1, 2, 3, a=4, b=5)
(1, 2, 3)
{'a': 4, 'b': 5}
>>> 
```

**Parameter ordering**

The only order requirements for paramters is that positional parameters must come before keyword parameters. This is what will happen if you attempt to define name arguments before positional ones: 

```python
>>> def foo(name=5, c):
...     print(name) 
... 
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```
