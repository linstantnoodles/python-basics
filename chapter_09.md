# Scopes

From [wikipedia](https://en.wikipedia.org/wiki/Scope_(computer_science))

> In computer programming, the scope of a name binding – an association of a name to an entity, such as a variable – is the region of a computer program where the binding is valid: where the name can be used to refer to the entity.

I love this definition. However, it's fairly abstract as it's defining a concept that applies to all languages. Lets try to ground our understanding of `scope` using Python. 

In python, there are many ways to create name bindings. One common way is in using assignment statements. 

In this case, we're associating the name `foo` with an entity of type string.

```python 
foo = "hello world"
```

Another way might be to define a function which binds the name `greet` to a function.

```python
def greet():
    return 'sup'
```

The scope of the `greet` name-binding in python depends on where it's defined in the source code. This is also known as `lexical scope`. The precise definition of _where_ depends on what regions of the source code can be a valid scope for some set of name-bindings.

In python, there are three main regions that can represent the scope for a set of name-bindings.

* The inside of a module (module scope)
* The inside of a class (class scope)
* The inside of a function (function scope)

So when we say that a name-binding has module scope, we're saying that it _can_ be accessed throughout the entire module. If it has function scope, then it _can_ be accessed throughout the entire body of the function.

Class scope is a special case because unlike module and function scopes which represent the entirety of the region, it excludes functions.

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

Finally, I want to emphasize that scope is a source-code concept. Although defining it in the first place requires us to have knowledge of how the language binds names at run-time, when we specify the scope of a name-binding, we are _not_ specifying whether the name-binding is actually visible during a point in the execution of the program.

For example: 

```python
>>> available_everywhere = "sup" 
>>> def wow(available_everywhere):
...     print(available_everywhere)
... 
>>> wow("hello world")
hello world
```

The name-binding `available_everywhere` and `"sup"` has module scope. It _can_ be accessed from anywhere, but as you can see when we execute the function `wow`, even though we're referencing the same identifier, we're getting back a different result. 

This is because the set of all visible name-bindings in the function level is different from the set of all visible name-bindings in the module level. In other words, it has a different _context_. Unlike scope, context is a run-time concept. How a programming language chooses to retrieve values by identifiers in the context at any given point in the program depends on its _name resolution_ rules. 



