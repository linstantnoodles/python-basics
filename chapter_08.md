# Functions

The workhorse of computing. The almighty function. Now that we know how to write expressions using our built-in types, we can group them together and run them over and over by defining them in a function body.

def hello_world(): 
	return "hello world"

an introduction to functions introduces a couple of new concepts: 

1) indentation
2) scopes

## How to invoke functions

## Arguments

def fn(): 
    pass

assert fn() == None

def fn():
    return

assert fn() == None

def fn():
    return True

assert fn() == True

def fn(a):
    return a

assert fn(5) == 5

def fn(a, b):
    return a + b

assert fn(1, 2) == 3

def fn(a, b):
    return a if b else "Whatsup"

assert fn(1, True) == 1
assert fn(1, False) == "Whatsup"

def fn(a=False):
    return a

assert fn(5) == 5
assert fn(a=5) == 5
assert fn() == False

def fn(*args):
    return args 

assert fn(1, 2, 3) == (1, 2, 3)

def fn(a, *args):
    return (a, args)

assert fn(1, 2, 3, 4) == (1, (2, 3, 4))

def fn(*args, b=None):
    return b 

assert fn(1, 2, 3, b=5) == 5

def fn(**kwargs):
    return kwargs

assert fn(a=4, b=5) == {"a": 4, "b": 5}

def fn(a, **kwargs):
    return a + kwargs['b']

assert fn(5, b=12) == 17

def fn(x, *args, **kwargs):
    return kwargs

assert fn(1, 2, 3, a=4, b=5) == {"a": 4, "b": 5}

def fn(a):
    b = 12
    def nested_fn():
        return a + b
    return nested_fn()

assert fn(1) == 13

def fn(a):
    b = 12
    def nested_fn(a):
        return a + b
    return nested_fn(12)

assert fn(1) == 24

def fn():
    pass


# advanced

# this is valid 
class Fun:
    pass
def a(b: Fun) -> True: 
    return 5

# introduced in https://www.python.org/dev/peps/pep-3107/#id28

# Do they do anything? No - only made for reading: 

# > By itself, Python does not attach any particular meaning or significance to annotations. Left to its own, Python simply makes these expressions available as described in Accessing Function Annotations below.


# >>> a.__annotations__
# {'return': True}


# this is also new: tfpdef: NAME [':' test]

def a(b: "wow" = not True):
    return b


def a(b: "wow" = lambda x: x**2):
    return b

# nested functions

# Next, lets move into the nature of function bodies. 


# No compound statements allowed i.e: if: or other function definitions
def fn(): return 5
def fn(): a = 5; return a

def fn():
    a = 5
    return a

def fn():
    a = 5; b = a; c = 12
    k = (10 + 10)
    return a + b + c

def fn(x): a = 5; return "sup" if x > 5 else "nope"

# Can we self-invoke? No. At least not with function definition statements. Lambda definitions are fine though. 


(True)
(5 + 5 + 5)
(10 < 12)
(lambda x: x**2)(100)

# can you nest functions? Sure! Function bodies are considered compound statements, that can also contain statements which can be anything.

# Can lambdas have returns? No. They only take basic test expressions ... But they can invoke other lambdas!

(lambda x: (lambda y: y * 2)(x))(5)

# lets discuss return values!

def a():
    return 1, 2, 3


# lets talk about closures
# lets talk about nested function scopes 
# 