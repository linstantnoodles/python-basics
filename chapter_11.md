# Execution Context and Name Resolution

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

Python uses dynamic name resolution, which means it attempts to find the entity associated with a name in the current execution context at runtime. Context is constructed at runtime using python [namespace]() objects, which are dictionaries of name-binding pairs.

There are three levels of namespaces:

* Local (function or class) namespace
* Global (module) namespace
* Built-in namespace

When python starts executing a module, it immediately constructs the built-in namespace. This namespace contains all of pythons built-in name-bindings. For example, the function `len` is in the built-in namespace - you can call it from any module. 

The variables you declare at the module level become part of the module namespace when they're encountered. 

Finally, the variables you declare locally become part of the local namespace when they're encountered in a function or class. 

### Function namespace
There are two ways local variables end up in a functions local namespace - either through declaration in the function body:

```python
def foo():
    greeting = "hello"
    return greeting 
```

Or through a parameter: 

```python
def foo(greeting):
    return greeting
```

### How name resolution works with namespaces

Name resolution works inside-out. It starts with the current namespace at a given point of execution and looks up the name. If it exists, the entity associated with that name is returned. If it does not exist, it looks up the enclosing namespace.

Here's the exact order: 

1. Local function namespace
2. Enclosing function namespace - starting with the nearest
3. Global (module) namespace
4. Built-in namespace

So when you have two name-bindings with the same name in different namespaces, the nearest one will be used. In other words, the name-binding in the nearest namespace shadows the other one. 

Here's a walk through of name resolution in action:

```python
class A():
    a = 'local class var a'
    b = 'local class var b'
    def fn(self):
        a = 'local function var a'
        c = 'local function var b'
        def nested_fn(a, b):
            print("Function nested_fn[a: {}, b: {}, c: {}]".format(a, b, c))
        # print("Function fn[b: {}]".format(b)) <- This will NOT work. The local class namespace 
        # is not part of the lookup chain.
        print("Function fn[a: {}, c:{}]".format(a, c))
        nested_fn(13, 15)
    print("class A[a: {}, b: {}]".format(a, b))
```

When executed in the interpreter: 

```bash
>>> class A[a: local class var a, b: local class var b]
>>> instance_a = A()
>>> instance_a.fn()
Function fn[a: local function var a, c:local function var b]
Function nested_fn[a: 13, b: 15, c: local function var b]
```

The body of the class is parsed first and the variables `a` and `b` which are mapped to `local class var a` and `local class var b` end up in the local class namespace. Then function is parsed (but not executed). Finally, the print statement at the end of the body of the class prints out the local class variables.

Next we create an instance of the class and invoke the function `fn`. It creates its own local variables `a` and `c`, and we see those printed right before our invocation of the `nested`.

Finally during the execution of `fn` we also invoke `nested_fn` with two parameters: `13` and `15`. Those get bound to it's own local variables `a` and `b`. Since `a` is bound locally, it prints `13` rather than `local function var a` which is defined by its enclosing function (shadowing in action).

During the execution of `nested_fn` we also see the value of `c` printed which turns out to be the value that was defined in the enclosing function. As name resolution rules dictate, if a name is not found in the current namespace (in this case, that's `nested_fn`'s namespace), then it looks at the nearest enclosing functions namespace (which is `fn`) where `c` is defined.
        