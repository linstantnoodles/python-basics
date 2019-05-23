# Floats 

Floats are implemented using C doubles. sys.float_info provides more details about the float type available on your platform. https://docs.python.org/3/library/sys.html#sys.float_info. 

Running this on my machine I get:

```
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```

max is the maximum float value and min is the minimum float value. 

radix ** max_exp will get you the value in max, so max_exp is the largest possible exponent for the radix (2). 

So given a radix of 2 and a max_exp of 1024, we can calculate the max (with 16 digits after the dot) to match the current max value. 

```
>>> from decimal import Decimal
>>> f"{Decimal(2**1024):.16E}"
'1.7976931348623159E+308'
```

Questions for myself: 

* How does division actually work at the machine level? 
* What is the role of the significand in representing a fractional number? 
* Why does a significand length of 53 mean a max of 16-17 decimal places? How are they related?
