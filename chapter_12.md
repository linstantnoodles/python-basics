# Classes 

Python lets you construct your own custom objects as well using classes.


```python
	class Export(): 
		schedule = "Tuesday"
		def __init__(self):
			self.label = "test"
		def run(): 
			print("Running")
```

Classes are objects. There are two things you can do with class objects. 

The first is that you can define attributes on the class. These attributes are name-bindings local to the class that you can access via dot syntax. For example, the class object above has three attributes: `schedule`, `__init__`, and `run`.

If I access them via dot syntax in the interpreter, I get: 

```bash
>>> Export.schedule
'Tuesday'
>>> Export.__init__
<function Export.__init__ at 0x7fbf7876f7b8>
>>> Export.run
<function Export.run at 0x7fbf739c1f28>
```

The second thing is that you can invoke them the same way you invoke functions in python. 

```
>>> export = Export() 
>>> export
<__main__.Export object at 0x7fbf76afb7b8>
>>> 
```

Invoking a class object creates an **instance** of the class. An instance is an object of a specific class type. When dealing with most built-in types, you're usually specifying instance objects rather than class objects. 

For example, lets take a list type for example:

```bash
>>> my_list = [1, 2, 3]
>>> type(my_list)
<class 'list'>
```

Since every instance object has a reference to its class object via the attribute `__class__`, you _can_ access the class object if you need to. For built-in types though, that's not a common need.


## What do instance objects have when first created? 

Nothing. All instance objects are created empty. Now, you may see this: 

```bash
>>> class Foo():
...     a = 'hello'
... 
>>> foo_one = Foo()
>>> foo_two = Foo()
>>> foo_one.a
'hello'
>>> foo_two.a
'hello'
```

Since we can access the variable `a` defined in the class `Foo`, does that mean attributes are being copied onto the instance object? No.

Class attributes are shared with instances and accessed from **lookups** on the class object. To prove this, lets change `a` directly on the `Foo` class object and see what happens:

```bash
>>> Foo.a = 'good bye'
>>> foo_one.a
'good bye'
>>> foo_two.a
'good bye'
```

If attributes were being copied onto the instance objects, we should still see `hello` printed.

## Setting instance attributes

Now there is a way to initialize attributes on the instance object, which is through a function you define in the class object called `__init__`. If python sees this function during the instantiation process, it will invoke it with one argument: the empty instance object.

```bash
>>> class Foo():
...     def __init__(self):
...             print(self)
... 
>>> Foo()
<__main__.Foo object at 0x7fbf739bcda0>
<__main__.Foo object at 0x7fbf739bcda0>
```

The first printed result is from the return value of the invocation. The second one is from our print statement. They both refer to the instance object. Now, the parameter `self` is a convention - it's a positional argument that can take on any name. By the convention is to use the name `self` to refer to the instance object that's passed in.

Since this function has a reference to the instance object, it can define anything it wants on it!

```bash
>>> class Foo():
...     def __init__(self):
...             self.greet = 'hello'
... 
>>> foo = Foo()
>>> foo.greet
'hello'
>>> Foo.greet
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Foo' has no attribute 'greet'
```

As you see above, the attributes you define directly on the object itself is specific to that instance and does not exist on the class object.

In fact, _any_ function (unless they're decorated ... which we'll cover later) you define on the class level will be passed the instance object when invoked by an instance object.

```bash
>>> class Foo():
...     def __init__(self):
...             self.greet = 'hey'
...     def leave(self):
...             self.greet = 'bye'
... 
>>> foo = Foo()
>>> foo.greet
'hey'
>>> foo.leave()
>>> foo.greet
'bye'
>>> 
```

This way of interacting with the instance object through a function parameter is more explicit compared to other languages such as ruby where the language hides the reference to the instance object. 

For example, here's how you define an instance variable in a function in ruby:

```ruby
class A
	def foo()
		@instance = 'hey'
	end  
end 
```

There's no explicit reference to an instance object - all you need to do is prefix names with `@` and ruby will set it on the instance for you.

If you're used to implicitly setting instance attributes, then this python way might be a bit weird at first for you!