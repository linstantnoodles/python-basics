# Numeric Operations 

Looking just at integers and floats, you can have operations like: 

int op int 
float op float 
int op float 
float op int 

I won't cover all operations but the most common are the operation can be: addition, subtraction, multiplication, division, exponentiation. 

> Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the "narrower" type is widened to that of the other, where plain integer is narrower than long integer is narrower than floating point is narrower than complex.

https://docs.python.org/2.4/lib/typesnumeric.html

Lets unpack that with examples

addition 

>>> 5+5
10
>>> 5.0 + 5.0
10.0
>>> 5 + 5.0
10.0
>>> 5.0 + 5
10.0

So in the case of float + int. Since float is wider, the int becomes a float and hence the final answer is a float. This is true for all five operations for all version of python.

One difference between python 2.x and 3.x is division between two integers.

python 2.x
>>> 10 / 5
2

python 3.x 
>>> 10 / 5
2.0

So in python 3.x, `/` is float division instead of integer division. To do integer division, use `//` in python3 (also true in Python 2).