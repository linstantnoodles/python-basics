# Execution Context

Different sets of name-bindings may be visible at any given point during the lifetime of the program. This is known as the *execution context* or just *context* for short. A visible name-binding means that the specific entity bound to the name can be trieved by referencing at the name. 

For example: 

```python
taste = 10
def price(): 
    freshness = 5
    return taste * freshness 
```

At any point during the execution of `price`, the integer object `12` can be accessed by referencing `taste` and the integer object `5` can be accessed by referencing `freshness`. Therefore, the context of the program during the functions execution contains all the name-bindings we defined. As for scope, `taste` has global module scope while `freshness` has local function scope. 

If a name-binding defined at the function level has the same name as a name-binding defined at the module level, the module level binding will _not_ be visible. 

For example:

```python
taste = 10
def price(): 
    taste = 5
    freshness = 5
    return taste * freshness 
```

The result of `price` will be `25` instead of `50` because there's a locally defined `taste` variable. In other words, the association of `taste` to `10` is not in context during the execution of this function. 

This behavior is dictated by how this context is constructed during the lifetime of a program which is specified by pythons [name resolution](https://en.wikipedia.org/wiki/Name_resolution_(programming_languages)) rules.

## Name resolution

Python uses dynamic name resolution, which means it attempts to get the entity associated with a name at runtime.

In Python, _context_ is represented by namespaces. 

* Local namespace
* Module namespace
* Built-in namespace

You can think of these namespaces as being chained together. All the namespaces accessible at a given point is the context of a python program. 

The way name resolution works is: 

    # Local function namespace
    # Enclosing function namespace - starting with the nearest
    # Module namespace
    # Built-in name space

Lets bring the two concepts together. If we define a name-binding at the module level, it has module _scope_ because that name _can_ be accessed throughout the entire module. If we have a function defined within the module that references that variable, then during the functions _execution_ or _runtime_, that variable will be part of the functions _context_ (among potentially other name bindings). Once that variable is actually referenced, python performs name resolution in the current context by looking up a series of namespaces for the variable. First, local. Doesn't find it. Since there's no enclosing function, it looks in the module namespace and finds it!

> A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.
