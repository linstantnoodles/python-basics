# Relational and Logical Operations

From [python doc](https://docs.python.org/2.0/ref/objects.html)

> Objects are Python's abstraction for data. All data in a Python program is represented by objects or by relations between objects.

## Relational (comparison) Operations

Python supports the following comparison operators:

* `==` (equal)
* `!==` (not equal)
* `<` (less than)
* `<=` (less than or equal)
* `>` (greater than)
* `>=` (greater than or equal)
* `is` (lol)

First of all, any comparison between anything requires a common unit of measure. Is thix apple less than that orange? Um, maybe. What's the unit? Are we talking about weight? mass? fiber content?

So before we can talk about comparisons, we have to talk about the objects we're comparing.

Python objects have three dimensions / units with which comparisons can be done:

* Identity
* Type
* Value

Object identity and type never change. Conversions such as `int('5')` create new objects. Object value can change. The types of objects whose values can change are *mutable* and the ones whose values cannot chane are *immutable*. For example, strings are immutable but many sequences such as lists are mutable.

Comparison on identity is easy. It's either the same object or it's not.

Comparison on type is also easy. It's either the same type or it's not.

Comparison on value is not so easy. What is the value of the integer `1`? (Not a trick question). Now, what's the value of our set `{1, 2, 3}`? Or a function? Or some custom object you created yourself?

Whether a comparison is done on identity, type, or value depends both on the comparison operator we're using and the objects we're comparing.

The default behavior for equality comparison (== and !=) is based on the identity of the objects. This is because all types inherit from the base object and the behavior of the equality operators for the base object is identity comparison. The equality operators are the only operators with default behavior. The behavior of all other comparison operators need to be implemented by different object types.

The `is` operator is a special case. It _always_ compares by identity and cannot be overriden.

### Numeric

All numeric comparisons (including equality comparison) are based on value.

```python
>>> a = 123
>>> b = 123
>>> a == b
True
>>> a < b
False
>>>
```

You can also compare different types of numerics, such as integers and floats.

```python
>>> 123.1 > 123
True
```

Outside of numeric types, comparisons across different types isn't supported. In python 3.x, you'll get an error if you attempt to compare different types. Python 2.x is more forgiving and _does_ return a value but the behavior (while consistent) is [not part of the language spec](https://stackoverflow.com/questions/3270680/how-does-python-2-compare-string-and-int-why-do-lists-compare-as-greater-than-n).

### Ordered containers (sequences)

Sequences use "lexicographical comparison", which is based on [lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order)

It's a general form of [alphabetical order](https://en.wikipedia.org/wiki/Alphabetical_order). In alphabetical ordering of words, the order of words is determined by the comparison of their individual letters based on their position in the english _alphabet_. This is the ordering you'll be familiar with if you've ever used an english dictionary.

For example, `alan` comes before `alba`. The first and second characters are equal but since the third letter a appears in the alphabet earlier than b, `alan` comes first.

Lexicographical comparison follows the same process, just in a more general form.

Why general? for one, it doesn't require that we only work with english letters. Maybe it's emojis and the "alphabet" (mathematically known as a totally ordered set) is the unicode codepoint that represents those emojis. Or maybe it's <your own made up type here> and the alphabet is <one you make up>.

Examples:

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

### Unordered containers (maps and sets)

Unordered collections do not follow lexigographical ordering (since there's no such thing as order for their members).

#### Maps (dictionary)

The only operations supported by maps are equality. Maps compare equal if and only if they have equal (key, value) pairs.

All order comparisons (<, >, <=, and >=) raise TypeError.

```bash
>>> {1, 2} == {2, 1}
True
>>> {} == {}
True
>>> {'a': 'b'} == {}
False
>>> {'a': 'b'} == {'a': 'b'}
True
>>> {'a': 'b'} == {'a': None}
False
>>> {} < {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'dict' and 'dict'
```

#### Sets

All comparison operators are actually subset and superset tests. `==` compares whether two sets are equal (same members, regardless of ordering because sets have no total ordering). `<` and `>` compares subset and superset, respectively.

Examples:

```bash
>>> {} == {}
True
>>> {1} < {5}
False
>>> {1} > {5}
False
>>> {1} < {1}
False
>>> {1} < {2, 1}
True
>>> {1} < {2, 1, 3}
True
>>> {1, 2} < {2, 1, 3}
True
>>> {1, 2, 3} < {2, 1, 3}
False
>>> {1, 2, 3, 5} < {2, 1, 3}
False
>>> {1, 2, 3, 5} > {2, 1, 3}
True
```

## Logical Operators

The three logical operators commonly supported in programming languages are:

* AND
* OR
* NOT

I've mostly learned those operators as `&&`, `||`, and `!` in other languages. In Python, they are `and`, `or`, and `not`, which are syntactically equal to their natural language counterparts.

```bash
>>> True and True
True
>>> True or True
True
>>> not True
False
>>> True and False
False
>>>
```

Even though I'm very accustomed to reading `&&`, I've grown to prefer pythons more verbose `and`.
