# Scope

From [wikipedia](https://en.wikipedia.org/wiki/Scope_(computer_science)):

> In computer programming, the scope of a name binding – an association of a name to an entity, such as a variable – is the region of a computer program where the binding is valid: where the name can be used to refer to the entity.

I like this definition because it's clear and concise. However, it's an abstract, language-agnostic definition that tells us little as to what this means in the context of a real programming language. I'm going to try to ground our understanding of `scope` by defining it within the world of python.

In python, there are many ways to create name bindings.

In this case, we're associating the name `foo` with an entity of type string by using an assignment statement:

```python 
foo = "hello world"
```

Another way might be to define a function which binds the name `greet` to a function:

```python
def greet():
    return 'sup'
```

The scope of the `greet` name-binding in python depends on where it's defined in the source code. The precise definition of "where" depends on what regions of the source code can be a valid scope for some set of name-bindings. 

## Two-level scoping

In python, there are two regions within a single file that can represent the scope for a set of name-bindings:

Global
* The inside of a module (module scope)

Local
* The inside of a class (class scope)
* The inside of a function (function scope)

These two regions represent two levels of scope where the higher level scope covers a wider region. For example, name bindings defined at a local level (the narrower region) by default will not have global scope.

For example: 

```python
def foo():
    greeting = 'hey'
    print(greeting)
print(greeting) 
```

`greeting` has local, function scope. So it will not be accessible by the print statement outside the function.

### Module scope, class scope, function scope

#### Module scope

When we say that a name-binding has a global or module scope, we're saying that the name _can_ be used to refer to the entity it's bound to throughout the entire module. 

For example:

```python
available_everywhere = 'hey'
def foo():
    def bar():
        print(available_everywhere)
    bar()
```

The value of `available_everywhere` is accessible in the body of `bar`.


#### Function scope

Likewise, when a name-binding has function scope, it _can_ be used to refer to the entity it's bound to throughout the entire function.

For example:

```python
def foo()
    value = 'sup'
    print(value)
    def nested_foo():
        print(value)
    nested_foo() 
```

#### Class scope

I'm covering class scope last because it is a special case because  unlike module and function scopes which represent the entirety of the region, it excludes functions.

Here's what I mean:

```python
>>> class Foo(): 
...     age = 12
...     def greet(self):
...         print("Hi my age is {}".format(age))
...     print("Age: {}".format(age))
... 
Age: 12
>>> x = Foo()
>>> x.greet()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in greet
NameError: name 'age' is not defined
```

## Scope vs Context

Scope is a source-code concept. Even though defining it in the first place requires us to have knowledge of how the language binds names at run-time, when we specify the scope of a name-binding, we are not specifying whether the name-binding is actually visible during a point in the execution of the program.

Scoping rules lets us re-use identifiers in different regions in our program without [name collisions](https://en.wikipedia.org/wiki/Name_collision), but that also leads to [shadowing](https://en.wikipedia.org/wiki/Variable_shadowing).

For example: 

```python
>>> available_everywhere = "sup" 
>>> def wow(available_everywhere):
...     print(available_everywhere)
... 
>>> wow("hello world")
hello world
```

The name-binding `available_everywhere` and `"sup"` has module scope. It _can_ be accessed from anywhere, but as you can see when we invoke the function `wow`, even though we're referencing the same identifier, we're getting back a different result because the `available_everywhere` name with local scope is shadowing the one with module scope.

The difference in visible name-bindings at the function level during execution from the set of all visible name-bindings in the module level during execution can be referred to as differences in *context*. 

Unlike scope, context is a run-time concept (even though they're confusingly used interchangeably in programming vernacular). 

From [wikipedia](https://en.wikipedia.org/wiki/Scope_(computer_science)#Definition): 

> The term "scope" is also used to refer to the set of all entities that are visible or names that are valid within a portion of the program or at a given point in a program, which is more correctly referred to as context or environment.

In the python function `wow` in the example above, we can say that at any point in that functions execution, it's context includes the locally scoped `available_everywhere` (amongst many other hidden bindings which we'll cover later). 

In many ways, context and scope are two sides of the same coin. When we speak about scope, we're speaking about the _regions in code where a name-binding can be accessed_ at runtime based on where that name-binding is defined. When we speak about context, we're speaking about the _name-bindings that are accessible at runtime in a region of code_.
