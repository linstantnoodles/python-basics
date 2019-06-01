# Ordered containers (sequences)

Sequences are a category of data types that share two common storage characteristics: 

1. Ordered 
2. Supports membership testing (is this element a member of this sequence?)
2. Members are index addressable (give me the 5th index of this sequence)

Here's a list of built-in types that share those characteristics and an example of retrieving a member from a value of that type using index addressing: 

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

`range` actually computes numbers lazily (so `range(10)` doesn't create 10 numbers in memory upfront). Nevertheless, python lets you address elements via indexes and perform membership testing on it so it's still consistent with the interface of sequences. 

## Writing your own custom sequences 

In python3, abstract classes (https://docs.python.org/3/library/abc.html#module-abc) were introduced and one of them was the `collections.abc.Sequence` abstract class (https://docs.python.org/3/library/stdtypes.html#typesseq). You can create your own sequences by inheriting from this abstract class.

Here's an example using an abstract class to enforce a protcol:

```python
from abc import ABC, abstractmethod

class MyCar(ABC):
	@abstractmethod
	def speed(self):
		pass 

class MyTesla(MyCar):
	def speed(self):
		return 60
```

If `MyTesla` did not implement a concrete `speed` method, attempting to instantiate it would result in a type error:

```python
TypeError: Can't instantiate abstract class MyTesla with abstract methods speed
```

## Readings 

https://treyhunner.com/2018/02/python-range-is-not-an-iterator/
