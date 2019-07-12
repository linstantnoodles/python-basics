# Iterators

Iterators are super pervasive in python. They're pretty much everywhere.

Lets go over the iterator pattern first and then we'll discuss how python supports iterators.

The iterator pattern lets you access elements from a container in sequence without knowledge of its underlying implementation. The notion of a _container_ isn't tied to any specific storage mechanism. For example, the container can be an array. Or a linked list. Or a tree. It doesn't matter - the same interface is exposed for you to traverse the container.

Here's a common UML (Unified Modeling Language) diagram of the pattern: 

![iterator pattern uml](https://en.wikipedia.org/wiki/Iterator_pattern#/media/File:Iterator_UML_class_diagram.svg)

There's two parallel parent child hierachies: the aggregate and the iterator. The _concrete_ aggregate is usually a container that wraps the actual container and knows how to create an iterator through its method _iterator_.

The concrete iterator is an object that is responsible for traversal. For traversing array types, this often means maintaining state information like current index. In this UML diagram, the methods for traversal are next and hasNext. This is a common interface for _external_ iterators.

## Iterators in Python

https://docs.python.org/3/library/stdtypes.html#iterator-types


Python containers already know how to create iterators! You don't have to implement the iterator pattern yourself.

In Python, every built-in container acts as an _concreate aggregate_ and knows how to create an iterator. That method is called `__iter__`.

>>> [].__iter__()
<list_iterator object at 0x10d4a9828>

This returns a concrete list iterator, which has an interface `__iter__` and `__next__` for iteration. Python calls this the `iterator protocol` (not a fan of the name `protocol`, it's just an interface). iter returns the object itself and `__next__` retrieves the next element in the container.

In most cases, you'll never have to call next yourself because the python `for` expression actually invokes `__iter__` on the container and performs the traversal for you. In that sense, the iteration is internal!

```bash
>>> numbers = [1, 2, 3]
>>> for x in numbers:
...     print(x)
...
1
2
3
```

## Whats the difference between an iterable and an interator? 

    Iterables have a __iter__ method that instantiates a new iterator every time.

    Iterators implement a __next__ method that returns individual items, and a __iter__ method that returns self .

    Therefore, iterators are also iterable, but iterables are not iterators.

Luciano Ramalho, author of `Fluent Python`.

An iterable is any object that implements the `__iter__` method which returns an iterator. That includes any of the built-in container objects as well as generators.