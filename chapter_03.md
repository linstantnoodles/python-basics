# Numeric Operations 

Looking just at integers and floats, you can have operations like: 

```
INTEGER ARITHMETIC_OPERATOR INTEGER 
FLOAT ARITHMETIC_OPERATOR FLOAT 
INTEGER ARITHMETIC_OPERATOR FLOAT 
FLOAT ARITHMETIC_OPERATOR INTEGER 
```

`ARITHMETIC_OPERATOR` is pretty standard and can be subtraction, addition, multiplication, division, exponentiation, and a few others. It's possible to use an arithmetic operator with two different types.

From [python docs](https://docs.python.org/2.4/lib/typesnumeric.html):
> Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the "narrower" type is widened to that of the other, where plain integer is narrower than long integer is narrower than floating point is narrower than complex.


Take addition for example: 

```bash
>>> 5+5
10
>>> 5.0 + 5.0
10.0
>>> 5 + 5.0
10.0
>>> 5.0 + 5
10.0
```

As you can see in the case of FLOAT + INTEGER. Since the float is wider, the int becomes a float and hence the final answer is a float. This is true for all five operations for all version of python.

One difference between python 2.x and 3.x is division between two integers.

python 2.x
```bash
>>> 10 / 5
2
```

python 3.x 
```bash
>>> 10 / 5
2.0
```

So in python 3.x, `/` is float division instead of integer division. To do integer division, use `//` in python3 (also true in Python 2).

## Precedence 

Precedence of arithmetic operators follows the same [orders of operations in math](https://en.wikipedia.org/wiki/Order_of_operations).

1. exponents and roots
2. multiplication and division
3. addition and subtraction 

Here's an example illustrating the precedence rules at work: 

```bash
>>> 2 + 5 * 3**2 / 1
47
```

Now lets follow these rules of precedence in evaluating this expression ourselves. If we do it right, we should get the same result.

Exponents are first, so `3**2` is 9. 

The exponentiation expression is sandwiched between multiplication and division, which have the same level of precedence, so it doesn't matter which we compute first but lets just go with multiplication. 

So `5 * 9` (9 is the result of `3**2`) is 45. 

Then applying the division `45 / 1` results in 45.

Finally, we apply addition which has the lowest precedence (`2 + 45`) and get 47.

### Overriding precedence

Any precedence rule can be overriden by wrapping expressions in parenthesis. This is true in math and it's also true in Python. So if we really wanted to perform the addition of `2 + 5` first, we would wrap it in parenthesis so it's `(2 + 5)`.


Arithmetic operators are also not the only operators in python subject to precedence rules. See the docs for a the complete operator [precedence table](https://docs.python.org/3/reference/expressions.html#operator-precedence).
