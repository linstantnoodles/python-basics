# Comprehensions

I think comprehensions are one of the most elegant and powerful (though often abused as well) language constructs ever created. It's a concise way of creating new built-in containers from existing iterables. Those containers are either lists, sets, or dictionaries.

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

Now lets add a condition that will only perform the expression for the odd numbers:

```bash
>>> [i * i for i in numbers if i % 2 == 1]
[1, 9]
```

As you can see, `i` obtained from the `for` expression is visible both in `ANY_ARBITRARY_EXPRESSION` and `OPTIONAL_COMPARISON`.

We can even expand the complexity of each of the component parts, such as using a list comprehension to create the iterable used in another list comprehension or using a list comprehension to create the arbitrary expression part.

```bash
>>> [x * x for x in [i * i for i in numbers]]
[1, 16, 81]
```

```bash
>>> [[i for i in range(3)] for i in numbers]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

So far, we've only looked at examples with the optional comparison. Here's one where we continue an existing list comprehension with _another_ list comprehension. I also call this adding more inner loops.

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

This is far less common and as you can see the readability of the comprehension is not great. Unlike the nested comprehensions we saw earlier which actually used two distinct list comprehension expressions where the parent one still had a single loop, this is a single list comprehension expression where there are two loops. Of course, you can extend it to have even more inner loops, but there's not much practicality to that.

## Dictionary comprehensions

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

KEep the braces, but drop the colon `:` and you now have a set comprehension!

```bash
>>> {i for i in numbers}
{1, 2, 3}
```

```bash
>>> {i*j for i in numbers for j in numbers}
{1, 2, 3, 4, 6, 9}
```

# Can't we just use map or filter?

Yes, but lets compare a simple example using both approaches side to side and get a feel for why one might be preferred. We'll be working with lists.

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

It ultimately comes down to taste. For me, comprehensions win because I don't need to make an extra call to convert the map or filter object into a list. Furthermore, it's just simpler (no need to introduce a lambda). Finally, we can perform _both_ filter and map using the same list comprehension. Whereas if we used map and filter we would have to filter first, then map.

https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions