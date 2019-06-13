# Comprehensions

I think comprehensions are one of the most elegant and powerful (though often abused as well) language constructs ever created. It's a concise way of creating new built-in containers from existing iterables. Those containers are either lists, sets, or dictionaries.

Most people including myself are familiar with list comprehensions since that's probably the most commonly use comprehension.

The general grammar for any comprehension is:

```python
for ANY_ARBITRARY_EXPRESSION in ANY_ITERABLE OPTIONAL_COMPARISON
```

Now lets look at concrete examples of specific comprehensions to get a better grip on how it works:

## List comprehensions

Here's an example where we create a new list containing the squares of all the elements in the original list:

>>> numbers = [1, 2, 3]
>>> [i * i for i in numbers]
[1, 4, 9]

Now lets add a condition that will only perform the expression for the odd numbers:

>>> [i * i for i in numbers if i % 2 == 1]
[1, 9]

As you can see, `i` obtained from the `for` expression is visible both in `ANY_ARBITRARY_EXPRESSION` and `OPTIONAL_COMPARISON`.

We can even expand the complexity of each of the component parts, such as using a list comprehension to create the iterable used in another list comprehension or using a list comprehension to create the arbitrary expression part.

>>> [x * x for x in [i * i for i in numbers]]
[1, 16, 81]

>>> [[i for i in range(3)] for i in numbers]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]


NEXT: show how youcan do continuations of fors.

This is equivalent to the functional paradigms map and select (or filter) since our expression does not modify the existing list and instead creates an entirely new list.

squaring every integer



numbers = [1, 2, 3]


result = map(lambda x: x * x, numbers)
squared = list(result)


result = []
for i in numbers:
	result.append(i * i)
return result

[i * i for i in numbers]

If you want to perform filtering without doing any transformation of each element, just provide a condition:

[i for i in numbers if i % 2 == 0]

If you want to do both (not straightforward in a map or filter function which are more specialized), you can!

[i * i for i in numbers if i % 2 == 0]

note: this should def. come after the iterator chapter.

and before the generator chapter

https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions