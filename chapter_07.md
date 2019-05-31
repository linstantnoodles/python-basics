# Unordered Containers / maps and sets 

Hash maps in python are also known as `dictionaries`.

They're constructed like so: 

{
	"key": "value"
}

## Dictionary operations

Since dictionaries are mutable, keys can hav etheir values reassigned, deleted, etc.

where "key" is the value that gets hashed into a hash table / dictionary.

Set "literals" can be constructed using the same curly braces we use to define dictionaries. The difference is that you don't include key/value pairs - just individual elements.

{1, 2, 3}

Notice the absence of the `:` token since we're not defining key-value associations.

## Set operations

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

