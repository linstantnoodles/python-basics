# Ordered containers / Sequences

Sequences (or ordered containers) are a category of data types that share two common storage characteristics: 

1. Ordered 
2. Supports membership testing (is this element a member of this sequence?)
2. Members are index addressable (give me the 5th index of this sequence)

here's a _complete_ list of built-in types that share those characteristics and an example of retrieving a member from a value of that type using index addressing: 

* string 
```bash
>>> 'hello world'[1]
'e'
```

* list 
```bash
>>> ['h', 'e', 'l', 'l', 'o'][4]
'o'
```

* tuple 
```bash
>>> ('h', 'e')[0]
'h'
```

* bytearray
```bash
>>> bytearray('hello world', 'utf-8')[0]
104
```


* memory view (or buffer in Python 2.x)
```bash
>>> memoryview(b'abcdefg')[0]
97
```

* range
```bash
>>> range(5)[3]
3
```

While types like `list` and `tuple` may seem like obvious candidates for sequences, `range` and `string` might seem like suprises to you. For one, `range` actually computes numbers lazily (so `range(10)` doesn't create 10 numbers in memory upfront). Nevertheless, python lets you address elements via indexes and perform membership testing on both so they are consistent with the interface of sequences.

## Writing your own custom sequences 

In python3, abstract classes (https://docs.python.org/3/library/abc.html#module-abc) were introduced and one of them was the `collections.abc.Sequence` abstract class (https://docs.python.org/3/library/stdtypes.html#typesseq). You can create your own sequences by inheriting from this abstract class.

## Readings 

https://treyhunner.com/2018/02/python-range-is-not-an-iterator/