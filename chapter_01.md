# Integers

Python 2.x

Plain integers are signed and have a fixed precision (number of digits). The precision depends on your platform (32 bit / 64 bit). On a 32 bit machine, they represent numbers between -2147483648 and 2147483647. Long integers on the other hand have unlimited precision. When you need to represent a number that exceeds the limits of a plain integer, Python automatically converts it to a long integer which has unlimited precision. 

Python 3.x 

All integer types are long (https://www.python.org/dev/peps/pep-0237/), so there is no platform-dependent precision difference. 

integers can be created with with the `int` builtin function which takes either a number or a string or as a literal without a decimal point such as `5`.

### Readings

What is the difference between precision and scale? 
https://stackoverflow.com/questions/5689369/what-is-the-difference-between-precision-and-scale

What are the maximum and minimum possible values for an int? 
https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints

Why is the maximum integer one less than the value after the sign for negative integers?
https://www.cs.cornell.edu/~tomf/notes/cps104/twoscomp.html

### Quiz

What is the difference between precision and scale? 

How do you convert a string number into an integer? 

Which python version has fixed precision? 

