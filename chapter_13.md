# Comprehensions

Comprehensions are one of my favorite language constructs in Python and I always miss them when programming in other languages. It's a concise way of creating new built-in containers (lists, sets, and dictionaries) from existing iterables.

Here's an example where we create a new list containing the squares of all the elements in the original list:

```bash
>>> numbers = [1, 2, 3]
>>> [i * i for i in numbers]
[1, 4, 9]
```

The expression `[i * i for i in numbers]` is the list comprehension expression. It's called a "list comprehension" because we're creating a new list and python uses the word "comprehension" to mean "inclusion" (borrowed from [set theory](https://en.wikipedia.org/wiki/Set-builder_notation)).

While list comprehensions are probably the most commonly found in python code bases, there are also set and dictionary comprehensions which I'll cover later.

The grammar for a comprehension is:

```python
for ELEMENT_EXPRESSION in ITERABLE OPTIONAL_COMPARISON_EXPRESSION OPTIONAL_COMPREHENSION_EXPRESSION
```

This grammar applies to all three (list, set, dictionary) comprehensions. Lets start with the common one: list.

## List comprehensions

You've already seen the `for ELEMENT_EXPRESSION in ITERABLE` syntax used in the example above (it was `[i * i for i in numbers]` in case you forgot), but as you can see from the grammar we can also include an optional comparison expression.

So lets add a condition that will perform the expression `i * i` only if `i` is an odd number:

```bash
>>> [i * i for i in numbers if i % 2 == 1]
[1, 9]
```

As you can see, the value of `i` from the `for` expression is visible both in `ELEMENT_EXPRESSION` and `OPTIONAL_COMPARISON_EXPRESSION`. We can further expand the complexity of each of the component expressions.

For example, we know that the `for` expression in the comprehension expects an iterable right? Well, what does a list comprehension return? An iterable! So lets create a new list using a list comprehension that uses an interable created by another list comprehension!


```bash
>>> [x * x for x in [i * i for i in numbers]]
[1, 16, 81]
```

Or we can use a list comprehension for the `ELEMENT_EXPRESSION` part so we get a list of lists.

```bash
>>> [[i for i in range(3)] for i in numbers]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

And we can also go nuts and do both! (protip: do this if you want to really, really want to annoy other programmers)

```bash
>>> [[i for i in range(3)] for i in [i * i for i in numbers]]
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

So far, we've only looked at examples of comprehensions that include the expression, the condition, and the optional comparison part of the grammar.

Here's one where we continue an existing list comprehension with _another_ list comprehension. This is equivalent to adding an "inner loop" in the tradional procedural sense.

For example, lets say we have two lists and we want to create a new list that represents the cartisian product of both lists. To do this procedurally, we'll have two loops and then manually append the computed value to an list we initialize.

```bash
>>> result = []
>>> for i in A:
...     for j in B:
...             result.append((i, j))
...
>>> result
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

So we loop through A, and for each element in A we loop through B and create a ordered pair (represented by a `tuple`).

Well, there's a nicer way to do this with comprehensions:


```bash
>>> A = [1, 2]
>>> B = ['A', 'B']
>>> [(i, j) for i in A for j in B]
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

In the comprehension above, there are two loops. The outer loop iterates through `A` and the inner loop iterates through `B`. Note that this is very different from the nested comprehension (`[x * x for x in [i * i for i in numbers]]`) we covered earlier because in a nested comprehension, the two loops are part of separate, independent list comprehension expressions. In this example, one loop depends on the other within the same comprehension.

## Dictionary comprehensions

The syntax for dictionary comprehensions is very similar to list comprehensions. Rather than creating new list objects, we're creating new dictionaries.

Here's an example where we create a new dictionary from a list of numbers where we map the value of the number to its square:

```bash
>>> {i:i*i for i in numbers}
{1: 1, 2: 4, 3: 9}
```

Just like list comprehensions, nested loops are supported:

```bash
>>> {i*j:i*i for i in numbers for j in numbers}
{1: 1, 2: 4, 3: 9, 4: 4, 6: 9, 9: 9}
```

Again, here's the equivalent without comprehensions:

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

# Ummmm, can't we just use map or filter for creating new lists? This comprehension stuff doesn't seem necessary.

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


Hope that improves your understanding (and love) of comprehensions!

## Assessment

# lists

* create a new list with same values as old list
* create a new list by transforming each element
* create a new list based on some condition (filtering)
** single condition
** multiple conditions
* do the same with transformation
* do the transformation using an if/else statement
* do a transformation with two lists
** three?
** generate all combinations of elements in two lists
** do it with a condition for each loop?
** create a list of lists. i.e a matrix.
** create a matrix of matrices
** flattening a list of lists
** flattening a list of list of lists

concepts:
    - understanding the grammar
    - easier to write in terms of for loops and then convert into LC structure

next:

    write test cases, basically. give ppl instructions for downloading and then writing tests. TDD from the start.
    each failure will result in
https://stackoverflow.com/questions/2893569/show-me-some-cool-python-list-comprehensions
https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/
