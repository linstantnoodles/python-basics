# Booleans

Booleans are subtypes of integers in Python

```bash
>>> True.__class__.__base__
<type 'int'>
```

Pythons capitalized booleans always trips me up. True is `True` and False is `False`. If you're coming from languages with lowercased booleans, then get used to seeing this _alot_. 

```bash
>>> true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> True
True
>>> 
```

## Logical Operators 

The three logical operators commonly supported in programming languages are: 

```
AND 
OR 
NOT
```

I've mostly learned those operators as `&&`, `||`, and `!` in other languages. 

In Python, they are `and`, `or`, and `not`, which are syntactically the same as their natural language equivalent! 

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