# Questions

## Question 1

```python
x = 7 
y = x 
x = 11
```
What's the final value of `y`? Why?

## Question 2

```python
def foo(x):
  if x: 
      return 1 + 1
  return 1 + 'NaN' # Unsupported mix-type operation
```
What's the output of `foo(True)`?

## Question 3 

```python
numbers  = [1, 1, 2, 3, 5]
for x in numbers:
    x = x * x 
```
Once the loop terminates, what's the value of `x`? What's the value of `numbers`? 

## Question 4

Which one of the following creates name-bindings?

```python
# A
import x
# B
from x import y
# C
def foo(): 
    pass
# D
class Boo():  
    pass 
# E
for x in some_list:
    pass
# F
x = 5
```

## Question 5 

```python
a = 5 * 2
b = 5 / 2
c = 5.0 * 2.0
d = 5.0 * 2 
e = 5.0 / 2
```
What's the value of a, b, c, d, and e? 

## Question 6

What do each of the following three expressions evaluate to?
1. `{} == {}` 
2. `{'a': 1} > {}`
3. `{} < {}`

## Question 7 

```python
class A():
    pass
```

What is the value of `A() == A()`?

## Question 8 

```python
class Lamp
    def turn_on():
        print("Turning on the Lamp") 
class Computer:
    def turn_on():
  print("Turning on the Computer")
  
x = Lamp() 
x.turn_on()
x = Computer() 
x.turn_on() 
```

Will this program run without any errors? Why or why not?

## Question 9 

What's the minimum and maximum value of an integer on a 32 bit machine?

A)  -2147483648 and 2147483647
B) No defined maximum. The precision is arbitrary and is limited by memory available
C) -9999999999999999999 and 9999999999999999999

## Question 10 
```python
x = 7
y = x
print(y is x)
x += 1
print(y is x)  
```
What are the values of the two print statements?

# Explanations
# Questions

## Question 1

```python
x = 7 
y = x 
x = 11
```
What's the final value of `y`? 

## Question 2

```python
def foo(x):
  if x: 
      return 1 + 1
  return 1 + 'NaN'
```
What's the output of `foo(True)`?

## Question 3 

```python
numbers  = [1, 1, 2, 3, 5]
for x in numbers:
    x = x * x 
```
Once the loop terminates, what's the value of `x`? What's the value of `numbers`? 

## Question 4

Which one of the following creates name-bindings?
```python
# A
import x
# B
from x import y
# C
def foo(): 
    pass
# D
class Boo():  
    pass 
# E
for x in some_list:
    pass
# F
x = 5
```

## Question 5

```python
class Lamp
    def turn_on():
        print("Turning on the Lamp") 

class Computer:
    def turn_on():
  print("Turning on the Computer")
  
x = Lamp() 
x.turn_on()
x = Computer() 
x.turn_on() 
```

Will this program run without any errors? Why or why not?

# Explanations

## Question 1

The final value of y is 7.

One common misconception around the process of why this happens is that:

1. `x` is initially storing the value `7` 
2. `y = x` causes `7` to be copied to `y`.

Since the variables store separate copies of the integer, any further assignments to `x` will not affect the value of `y`. While it's generally true that variable assignments in python happen independently, how it happens is very different from above. 

What's really happening is: 

1. `x` is initially referencing the object `7`
2. `y = x` causes `y` to reference whatever `x` is refrencing, which is the object `7`
3. `x = 11` changes `x` to reference the object `11` 

The names in python exist separately from the values - they're more akin to C pointers (but not quite, as I'll explain below) rather than C variables (where the actual value is stored at the location of the variable). The names have no reference of each other - assigning variables to each other just makes it so that they reference the _same_ object. Since the names reference the objects directly, any updates to those references will happen independently. 

### Frequently asked questions: 

**Um, how do I know you're not bullshitting me? How do I know for sure values aren't being copied??**

Lets test the explanation using python itself...

The functions we'll be using are: 

id() (https://docs.python.org/3/library/functions.html#id)
sys.getrefcount() (https://docs.python.org/dev/library/sys.html#sys.getrefcount)

`id` is basically the address of the object. It will be unique for every object. When you call `id` on a name, it gets you the address of the object it's referencing (not the address of the name!). `getrefcount` will get the number of names referring to an object. I'm going to demonstrate how the refcount for an integer object changes as we add more assignments. 

```python
>>> import sys
>>> id(1)
10910400
>>> sys.getrefcount(1)
806
>>> x = 1
>>> id(x)
10910400
>>> sys.getrefcount(1)
807
>>> y = x
>>> id(y)
10910400
>>> sys.getrefcount(1)
808
>>> x = 2
>>> sys.getrefcount(1)
807
```

So as you can see, we're dealing with the same object throughout this experiment (as proven by the outputs of `id`). When we did `y = x`, the refcount went up by one (because `y` is now also pointing at our integer object `1`). Finally, the refcount gets decremented when we update `x` to reference `2` which is a different object.  

If `y = x` was merely copying values, there would be no change in the refcount. 

**Okay so what you're describing sounds a lot like pointers to me - are python variables basically C pointers?**

The short answer is ...kind of, but not really. For a longer, better answer check out this answer on quora: https://qr.ae/TWvjiB

If you know a bit of C, I wrote an example of something you can do with C pointers that you won't be able to do with python variables.

```c
int five = 5;
int seven = 7;
int *x = &five; 
int **y = &x;
x = &seven;
printf("%d\n", **y);
```

The result of the print statement is `7`. So changing one variable actually changed a different variable. Why? W

We declare `y `as a pointer to another pointer `x`. `y` gets its value by dereferencing the pointer `x` is pointing to. This means if we change what `x` points to, that also affects the pointer `y`. In Python, names do not refer to other names. They refer directly to values!

## Question 2 

The return value of `foo(True)` is `2`.

Python performs [dynamic type checking](https://en.wikipedia.org/wiki/Type_system#Dynamic_type_checking_and_runtime_type_information). What that means is that it associates type information with values at runtime. Put another way, it only cares about the type of a value when it tries to use it. Since the unsupported operation is never used, the function returns without error! 

Now lets execute the unsupported operations in the REPL and see what happens: 

```bash
>>> if True: 
...     1 + 'NaN'
... else:
...     1 + 1
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Now that we're actually executing the line where we're performing an unsupported mix-type operation, the type error is thrown.

### FAQ

**Does this mean I can type anything in regions of code that won't be executed?** 

Not quite - you can't run a program if it contains syntax errors even if you put them where they won't be executed. 

For example: 

This program is correct by pythons syntax: 

```python
if True:
    1 + 1
else:
    icandowhateveriwanthereright+=1
```

Even though `icandowhateveriwanthereright` might not be defined, it's a syntactically correct expression so this program will execute without error. 

On the other hand ... 

```python
if True:
    1 + 1
else:
    icandowhat   ++ everiwanthereright+=1
```

Will throw:

```
...
  icandowhat   ++ everiwanthereright+=1
SyntaxError: can't assign to operator
```

This temporal difference (when syntax errors are thrown vs type errors) is related to the compilation process. When we execute a program by calling `python some_program.py`, the errors (syntax or otherwise) feels instant but are results of a multi-step (but very fast) compilation process. Which part of that process an error is coming from is largely invisible to the user. 

Lets zoom into that process a bit.

Generally speaking, python compilation involves: 

1. Lexing (breaking up text into meaningful tokens)
2. Parsing (using grammar to organize tokens into an [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree))
3. Translation of AST into bytecode 
4. Bytecode execution

The parsing step is [where errors in program grammar is caught](https://docs.python.org/3/library/exceptions.html#SyntaxError). This makes sense, because if you have an invalid program, there's no point in executing it.

## Question 3

The final value of x is 25 and numbers remains unchanged [1, 1, 2, 3, 5]. The reason numbers remains unchanged is that at no point do we change the reference to integers in the list `numbers`. Our loop created a new name called `x`, and then for each expression `x = x * x` it bound that name to a new integer object (value of `x * x`)

Another way to think about it is that this is actually just another case of the following: 

```python
number = 5
x = number 
x = x * x
```

Does number change when we reassign x? No, it doesn't because x = x * x updates x to reference the new object 25. But that does nothing to change the fact that number is still referencing the object `5`. If you want to change `number`, you need to reassign it to something else! 

So if we want to actually change the integers in the list numbers, we have two options:

1. We update the references to integers within the _existing_ list.

```bash
>>> numbers = [1, 1, 2, 3, 5]
>>> for idx, x in enumerate(numbers): 
...     numbers[idx] = x * x 
... 
>>> numbers
[1, 1, 4, 9, 25]
```

2. We update the reference of `numbers` to a _new_ list.

```bash
>>> numbers = [1, 1, 2, 3, 5]
>>> numbers_squared = []
>>> for x in numbers:
...     numbers_squared.append(x * x)
... 
>>> numbers = numbers_squared
>>> numbers
[1, 1, 4, 9, 25]
```

Or more idiomatically, as a list comprehension:

```bash
>>> numbers = [1, 1, 2, 3, 5]
>>> numbers = [x * x for x in numbers]
>>> numbers
[1, 1, 4, 9, 25]
```

## Question 4

Which one of the following creates name-bindings?
```python
# A
import x
# B
from x import y
# C
def foo(): 
    pass
# D
class Boo():  
    pass 
# E
for x in some_list:
    pass
# F
x = 5
```

They all create name bindings! Every introduction of an identifier introduces a new name into memory that points to an object.

Ok lets go through each: 

`import x` binds the name `x` to a module object 
`from x import y` binds the name `y` to an object belonging to the module `x`
`def foo()` binds `foo` to an object function
`class Boo()` binds `Boo` to a class object 
`... for x in some_list...` binds `x` to objects in `some_list`
`x = 5` binds x to the integer object `5`

And like any name binding, they can be reassigned to any other value. 

Here's an example where I define a class object referenced by `A` and then update the reference to an integer:

```bash 
>>> class A():
...     pass
>>> A
<class '__main__.A'>
>>> A = 5
>>> A
5
```

## Question 5 

Both statements will be printed successfully! Why?

Firstly, names are not associated with types in Python - once you have a name, it can reference any other object. 

Secondly, python uses a [duck type system](https://en.wikipedia.org/wiki/Duck_typing). You can refer to an attribute on an object regardless of its type. Even if we had an object, say, `Dog` that did not have the `turn_on` method, the expression `Dog().turn_on` will still execute and Python will attempt to find the attribute (though we know in this case that it will fail).

Java, as an counter-example, uses a [nominal type system](https://en.wikipedia.org/wiki/Nominal_type_system). This means the variables are declared with types and trying to reassign a name to a different type will yield errors (because equivalence is based strictly on the name of the type declarations):

```java
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
```

Trying to compile this program raises:

```java
Main.java:18: error: incompatible types: Computer cannot be converted to Lamp
```