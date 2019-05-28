# Operations 

## Numeric 
	
## Boolean / Logical 

## Comparison / relational

1 < 3 
5 > 2 

10.0 < 4
10 == 3 

what happens when we deal with non-numeric types? 

in python, comparison operators can accept mixed types. they compare the _value_ of objects. the value of numeric types is just their nuermic values. 

what is the _value_ of non-numeric types? such as strings? sequences in general? 

lets discuss strings 
what happens when you compare value sof two different types? 

first, types of comparison operators: <, > , <=, >=, ==, !==, is 
"a" < 5

> The default behavior for equality comparison (== and !=) is based on the identity of the objects. Hence, equality comparison of instances with the same identity results in equ

so all types inherit from object. and the default behavior that come with object are for two operators == and != and it's based not on value but identity. 

this can be overriden by specific types. all other comparison operators are implemented by specific types.

i.e for numeric types, == doesn't do identity, but value oruru

lets talk about these comparions for strings and sequences: 

1. strings 

> Strings (instances of str) compare lexicographically using the numerical Unicode code points (the result of the built-in function ord()) of their characters. [3]

strings are sequences in python. it's a sequence of characters. the way python handles comparison operators with sequences is to compare the individual elements, starting from the left. if the value of its component parts are equal, the sequences are equal. 

now, "component" parts can be all the same type, or different types. they can even be sequences themselves! 
if they are sequences themselves, those are compared the same way, recursively.

now, different sequence types are _never_ equal.

python2.x just returns false

>>> [] < {}
False

python3.x actually throws an error
>>> [] < {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'list' and 'dict'
>>> 

sequences follow what is known as a "lexicographical comparison". understanding the results of comparison requires understanding of what https://en.wikipedia.org/wiki/Lexicographical_order is. 

in a nutshell, it's a general form of https://en.wikipedia.org/wiki/Alphabetical_order. why general? in alphabetical ordering of words, the order of words is determined by the comparison of their individual letters based on their position in the _alphabet_.

alan 
alba 

alan comes before albino. because the first, second characters are equal but in the third letter a appears in the alphabet earlier than b! this is the ordering you'll be familiar with if you've ever used an english dictionary. 

now, "lexicographical" comparison follows the same idea, just in a more general form. Why general? for one, it doesn't require that we deal with letters only. Maybe it's emojis and the alphabet is the unicode codepoint that represents those emojis. Or maybe it's <your own made up type here> and the alphabet is <one you make up>.

while the type and alphabet associated with that type (mathemtically known as a totally ordered set, informally as an "alphabet") can vary, what's key about lexigographical comparison is the _process_ of comparison which remains the same - which is you determine the ordering between two types by comparing the elements that make up that type, one at a time from left to right - just like ordering words in a dictionary.

with strings, the characters aren't just limited to letters in the alphabet - they can be any unicode character and so the "alphabet" python uses is the unicode code point per character when applying lexigographic ordering.

2. sequences 

Lexicographical comparison between built-in collections works as follows:

1) equality 
    For two collections to compare equal, they must be of the same type, have the same length, and each pair of corresponding elements must compare equal (for example, [1,2] == (1,2) is false because the type is not the same).

2) less than or equal 

    Collections that support order comparison are ordered the same as their first unequal elements (for example, [1,2,x] <= [1,2,y] has the same value as x <= y). If a corresponding element does not exist, the shorter collection is ordered first (for example, [1,2] < [1,2,3] is true).

NOW, unordered collections do not follow lexigographical ordering (since there's no such thing as order for their members) so you need to know what kind of comparison they support.

3. mappings

Mappings (instances of dict) compare equal if and only if they have equal (key, value) pairs. Equality comparison of the keys and values enforces reflexivity.

Order comparisons (<, >, <=, and >=) raise TypeError.

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
>>> 
```

4. sets

Sets (instances of set or frozenset) can be compared within and across their types.

They define order comparison operators to mean subset and superset tests. Those relations do not define total orderings (for example, the two sets {1,2} and {2,3} are not equal, nor subsets of one another, nor supersets of one another). Accordingly, sets are not appropriate arguments for functions which depend on total ordering (for example, min(), max(), and sorted() produce undefined results given a list of sets as inputs).

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