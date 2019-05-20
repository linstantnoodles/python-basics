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


