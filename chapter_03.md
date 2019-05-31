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