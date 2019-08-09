# name bindings, values, and types

x = 7 
y = x 
x = 11

What's the value of `y`? 

A) 7
B) 11 
C) None 
D) Um wut? You cannot reassign a name

Answer: 7

Explanation: 

y does not reference x - it references the integer object 7 directly. When we reassign x to 11, we're making it reference the new number. 
What's not happening is value copying - we are not copying 7 to y. While that can explain this behavior, it's not what's happening. 
One way to look at this is that when we assign variables to other variables, we're not creating pointer of pointers. A name does not reference another name in python - they always reference the values directly. 

What this means is that all assignment statements happen independently from each other. This is by design.

All names in python point to values. When `x` is reassigned the value `11`, it points to the value `11` while `y` is still pointing to `7`. 

Common question: are variables in python just like C pointers? The short answer is ...kind of, but no. For a longer, better answer check out the explanation here: 

https://qr.ae/TWvjiB

if True: 
	1 + 1
else:
	1 + 'not a number'

What's the value of this expression? 

Since the bad operation is never executed by the python interpreter, this program will execute without error! Since python does not associate types with values until runtime, type errors are only caught when expressions are evaluated. 

if True: 
	1 + 'not a number'
else:
	1 + 1

what's the output of this function? 

>>> if True: 
...     1 + 'not a number'
... else:
...     1 + 1
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Now that we're actually executing the line where we're performing an unsupported mix-type operation, the type error is thrown.


x = [1, 2, 3]
y = x 
x.append(4)

What's the value of y? 

x is a mutable object and x.append mutates the existing list by adding 4 to the end of the list. Since both names point to the same object, any changes to that object will be reflected when accessing it through either name. 



x = 7
y = x
print(y is x)
x += 1
print(y is x)  

What are the values of the two print statements (in order)?

A) True, True
B) False, False
C) True, False
D) False, True 

It's True false because the names initially reference the same object 7, but unlike lists integers are immutable. Python creates a new integer object and updates the name binding of x to reference the new integer 8 (7 + 1). This behavior is true for all immutables in python which includes floats, strings, and tuples. 

ideas: rebinding vs mutating 

numbers  = [1, 1, 2, 3, 5]
for x in numbers:
	x = x * x 

Once the loop completes, what's the value of x? What's the value of numbers? 

A) None and [1, 1, 2, 3, 5] 
B) 5 and [1, 1, 2, 3, 5]
C) None and [1, 1, 4, 9, 25]
D) 5 and [1, 1, 4, 9, 25]

Python reassigns x over and over again until the loop terminates so it will preserve the value of the last number in the loop. The original list remains unchanged because integers are immutable. x * x creates a new integer object (rather than mutating the existing one) and the name x is updated to reference it. 

If, however, we were dealing with mutable elements: 

>>> numbers  = [[1], [2], [3]]
>>> for x in numbers:
...     x.append('sup')
... 
>>> numbers
[[1, 'sup'], [2, 'sup'], [3, 'sup']]
>>> x
[3, 'sup']
>>> 

In this case, we mutate the element and so we get the list with the changes. x much like before is bound to the last value that got computed and assigned. This is true across all name assignments. Whether or not the original object changes depends on whether or not you're performing a mutation on the value itself. Names only point to these objects the only way for operations using a different name to reflect in the other the value itself must be mutated. Otherise, new objects are created and the names will just end up referencing different objects. 


ideas: names have no types associated with them 

def foo(x):
	x.append(7)

what happens ? 

def foo(x):
	x = x + [1]

which one of the following is a name-binding?

import x 
def foo():
	pass 
class B():	
	pass 
for x in some_list:
	pass 
x = 5

all of the above 

These are all examples of name-bindings in python. Every introduction of an identifier introduces a new name into memory that points to an object. 

x is bound to a module object. foo is bound to a function. B is bound to a class object. x is bound to an element retrieved from some_list. and x is bound to a the integer object 5. 


# duck typing 

class AirConditioner
	def start():
		pass 


class Car:
	def start():
		pass 

x = AirConditioner 
x.start()
x = Car() 
x.start() 

what's printed out? 

  class Lamp {
    boolean isOn;
    void turnOn() {
      System.out.println("Turning on lamp");
    }
  }

  class Computer { 
    void turnOn() { 
      System.out.println("Turning on computer");
    }
  }

  class Example {
  public static void main(String[] args) {
      Lamp x = new Lamp();
      x.turnOn();
      x = new Computer();
      x.turnOn();
    }
  }

  Main.java:18: error: incompatible types: Computer cannot be converted to Lamp
      x = new Computer();


what's the min and maximum value of an int on a 32 bit machine??
a) numbers between -2147483648 and 2147483647
b) no defined maximum - the precision is arbitrary depending on available memory 
c) 99999999999999999999999

what's the min and max float values on a 64 bit machine? 
a) 1.7976931348623157e+308 min=2.2250738585072014e-308
b) 9.9999999999999999e+10
c) no defined maximum! - the precision is arbitrary depending on memory 

the follow will be printed 

what's 5.0 + 5.0? 
what's 5 + 5?
what's 
5.0 + 5 
5 + 5.0 
5 * 5.0
5 * 5 
5.0 * 5 


5 /2 = ? 

2
3
2.5
2.0


# equality 

comparisons between values are done on the following

identity only
identity and value 
identity and type 
identity, value, or type 

misconception 

[] == []


class A():
	pass
class B():
	pass 

what is A() == B()? 

>>> class A():
...     pass
... 
>>> A() == A()
False
>>> class A():
...     def __eq__(self, obj):
...             return True
... 
>>> A() == A()
True
>>> 


## map equality 

tell me results of 

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

## lexicographic ordering 

tell me results of 

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

## numerics 

tell me result of 


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


# sets 

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

# none 

None == None 

which of the following is NOT considered a sequence? 

check all that are sequences 

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

dictionary 
set 
generator 



