# Classes 

Python lets you construct your own custom objects as well. 


```python
	class Export(): 
		schedule = "Tuesday"
		def __init__(self):
			self.label = "test"
		def run(): 
			print("Running")
```

All variables and functions defined in the body of the class have class-level scope. This means Export.schedule and Export.run will return values. Those values are not defined outside of the class.

Both of those are known as attribute references. Any object with a dot followed by a name is an attribute reference.

Python has no concept of privates so you can also assign to existing attributes or create entirely new ones.

Export.schedule = "Wednesday"
Export.duration = "5 hours"

* defining a class
* namespace / scope
* instances 
* self 
* inheritance 
* decorators 

Great tutorial: https://docs.python.org/2/tutorial/classes.html

https://docs.python.org/2/tutorial/classes.html#class-and-instance-variables

Variables defined at the class level 

when the constructor is called and a class is created 
I love instantiation of classes in python - it uses function invocation syntax (name followed by parenthesis). So there's two operations: either an attribute reference of using the name as invocation to create an instance (instantiation)

By default 

>>> class Empty():
...     pass
... 
>>> Empty()
<__main__.Empty object at 0x7efcbbe4f7b8>
>>> 

Now if you want the empty object initialized with some data, you can define a method called __init__. 
Whe npython sees this init method, it will invoke it after creating the empty object by passing it as the first argument to __init__. 

This behavior of passing the initialized object to a method is how methods operate on data in an instance. in other languages, there is no explicit reference to the object in the code as the language takes care of making sure operations you make within methods are done on the instance object. In python you need to explicitly use self if you want to define things on the instance specifically.


Example in ruby: 

class A
	def foo()
		@instance = 'hey'
	end  
end 

By prefixing identifiers with a symbol, we tell ruby that this needs to be defined on the instance. 

What does it mean t obe defined "on"? Are objects just maps? Yes and no. They are just a set of name binding pairs, but the different is that objects bridge the connection of those name binding pairs to the object itself. 

when you define an attribute on the class, you can access it thru the instnace.
when you define a method, the instance is passed to the method to be operated on / used / read from.
whe nyou define a special method init, the nstance is constructed with some initial data.
what's more, you can also "inherit" other names from other classes 

so sure, you can just make a dictionary with this attributes and it's probably sufficent if you're only dealin gwith data. But if you want the functions on that dictionary to operate on a shared object, you're basically trying to invent classes. 

