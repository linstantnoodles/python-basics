# Comprehensions

I think comprehensions are one of the most elegant and powerful (though often abused as well) language constructs ever created. It's a concise way of creating new built-in containers from existing iterables. Those containers are either lists, sets, or dictionaries.

Note: an iterable is any object that returns an iterator. In python, that includes any built-in container type object.

Most people including myself are familiar with list comprehensions since that's probably the most commonly use comprehension.

The general grammar for any comprehension is:

```python
for ANY_ARBITRARY_EXPRESSION in ANY_ITERABLE OPTIONAL_COMPARISON OPTIONAL_COMPREHENSION
```

Now lets look at concrete examples of specific comprehensions to get a better grip on how it works:

## List comprehensions

Here's an example where we create a new list containing the squares of all the elements in the original list:

```bash
>>> numbers = [1, 2, 3]
>>> [i * i for i in numbers]
[1, 4, 9]
```

Now lets add a condition that will only perform the expression `i * i` for the odd numbers:

```bash
>>> [i * i for i in numbers if i % 2 == 1]
[1, 9]
```

As you can see, `i` obtained from the `for` expression is visible both in `ANY_ARBITRARY_EXPRESSION` and `OPTIONAL_COMPARISON`.

We can even expand the complexity of each of the component parts. 

For example, lets use a list comprehension to create a list used in another list comprehension!


```bash
>>> [x * x for x in [i * i for i in numbers]]
[1, 16, 81]
```

Or we can use a list comprehension as our arbitrary expression so we get a list of lists.

```bash
>>> [[i for i in range(3)] for i in numbers]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

And we can also go nuts and do both!

```bash
>>> [[i for i in range(3)] for i in [i * i for i in numbers]]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

So far, we've only looked at examples of comprehensions that include the expression, the condition, and the optional comparison part of the grammar. 

Here's one where we continue an existing list comprehension with _another_ list comprehension. Basically, this is adding inner loops.

```bash
>>> numbers = [1, 2, 3]
>>> [i * j for i in numbers for j in numbers]
[1, 2, 3, 2, 4, 6, 3, 6, 9]
```

This is equivalent to the following:

```bash
>>> result = []
>>> for i in numbers:
...     for j in numbers:
...             result.append(i * j)
...
>>> result
[1, 2, 3, 2, 4, 6, 3, 6, 9]
```

 The nested comprehensions we saw earlier still used a single loop in the parent comprehension. In the comprehension above, there are two loops. You also extend it to having even more loops! However, having multiple loops in the comprehension isn't very common and from my experience it makes your code a lot less readable.

## Dictionary comprehensions

The syntax for dictionary comprehensions is very similar to list comprehensions. Rather than creating new list objects, we're creating new dictionaries.

```bash
>>> {i:i*i for i in numbers}
{1: 1, 2: 4, 3: 9}
```

Like list comprehensions, nested loops are supported:

```bash
>>> {i*j:i*i for i in numbers for j in numbers}
{1: 1, 2: 4, 3: 9, 4: 4, 6: 9, 9: 9}
```

Again, here's the equivalent without comprehensions

```bash
>>> result = {}
>>> for i in numbers:
...     for j in numbers:
...             result[i*j] = i *i
...
>>> result
{1: 1, 2: 4, 3: 9, 4: 4, 6: 9, 9: 9}
```

## Set comprehensions

Keep the braces, but drop the colon `:` and you now have a set comprehension!

```bash
>>> {i for i in numbers}
{1, 2, 3}
```

```bash
>>> {i*j for i in numbers for j in numbers}
{1, 2, 3, 4, 6, 9}
```

# Um, this is cool but can't we just use map or filter for creating new lists?

There's nothing wrong with that, but lets compare a simple example using both approaches side to side and get a feel for the differences.

Using map to get squares:

```bash
>>> list(map(lambda x: x * x, numbers))
[1, 4, 9]
```

Using list comprehensions:

```bash
>>> [i * i for i in numbers]
[1, 4, 9]
```

Using filter to get all evens:

```bash
>>> list(filter(lambda x: x % 2 == 0, numbers))
[2]
```

With comprehensions:

```bash
>>> [i for i in numbers if i % 2 == 0]
[2]
```

Using map and filter to get squares of evens: 

```bash
>>> list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
[4]
```

With comprehensions: 

```bash
>>> [i * i for i in numbers if i % 2 == 0]
[4]
```


In scenarios similar to the examples above, I prefer comprehensions because:

* I don't need to make an extra call to convert the map or filter object into a list.
* It's simpler (no need to introduce a lambda expression for the operation) and more concise.
* We can perform _both_ filter and map using the same list comprehension. Whereas if we used map and filter we would have to filter first, then map.


Sources: 

https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions