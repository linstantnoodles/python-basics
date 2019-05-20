Here's a python implementation of the fizz buzz program (https://en.wikipedia.org/wiki/Fizz_buzz)

```
def fizzbuzz(n): 
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0: 
            print("FizzBuzz")
        elif i % 3 == 0: 
            print("Fizz")
        elif i % 5 == 0: 
            print("Buzz")
        else: 
            print(i)
```

This example introduces a bunch of concepts. 

* Functions
* Iterating through a range using built-in `range` function
* If / Else if / Else conditional statements 
* Comparison operators 
* Printing

Basic types 

* Numeric

There's plain integers, long integers, floats, and complex integers. We'll cover the first three.

Plain integers are signed and have a fixed precision (number of digits) and it depends on your platform (32 bit / 64 bit). On a 32 bit machine, they represent numbers between -2147483648 and 2147483647. When you need to represent a number that's greater or smaller than the limits of a plain integer, Python automatically converts it to a long integer which has unlimited precision. 

Floats 

TBD

### Other notes

What is the difference between precision and scale? 

https://stackoverflow.com/questions/5689369/what-is-the-difference-between-precision-and-scale

What are the maximum and minimum possible values for an int? 

* https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints

Why is the maximum integer one less than the value after the sign for negative integers?

https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html
 



* Boolean 
* Sequences - List, Tuple 
* Containers - Dictionary, Set
* String


# integers 

1, 2, 5 int