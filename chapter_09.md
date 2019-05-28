# Scopes

Up til now, every identifier we refer to is assumed to be available. 

There's 3 levels of scoping: 

module (global)
class 
function

name = "a"
print(name)
class TestClass:
    name = "class level name"

    def name(self):
        print(self)
        name = "fn name"
        def nested_fn():
            name = "nested fn name"
            print(name)
        nested_fn()
        return name 

def name():
    return "sup"

print("sup")

def hey():
    return name 

print(name)
print(hey())

print(TestClass().name) 
print (TestClass.name)

# important concept about class attributes

#  There are two kinds of valid attribute names, data attributes and methods.
#  When a non-data attribute of an instance is referenced, the instance’s class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: this is the method object. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.





mylist = [1, 2, 3]
for x in mylist:
    k = x

assert k == 3

if True:
    m = 12

a = 5
assert m == 12

def wer():
    return m 

assert wer() == 12

class MyObject:
    myprop = 'alan'

    def __init__(self):
        self.a = 12 

    @classmethod
    def hey(self):
        pass

assert MyObject.hey() == None
assert MyObject.myprop == 'alan'

instance_one = MyObject()
instance_two = MyObject()

assert instance_one.myprop == 'alan'
MyObject.myprop = 'heyalan'
# assert instance_one.myprop == 'alan' # this should fail

# interesting, the variable is accessible! Not the case in ruby. 
assert instance_one.myprop == 'heyalan'

# Class retains its value even when overwritten with instance
instance_one.myprop = 'newalan'
assert MyObject.myprop == 'heyalan'
# assert MyObject.a == None // raises exception b.c attribute doe snot exist
# assert MyObject().hey() == None // this raises exception

# > Both class and instance attributes are accessible through the notation
# “self.name”, and an instance attribute hides a class attribute with the same
# name when accessed in this way

# Real world usages of class attributes: https://github.com/2uinc/oars/blob/master/oars/models.py#L487

# Shadowing example

class TestShadow:
    a = 'default'

assert TestShadow.a == 'default'
assert TestShadow().a == 'default'

class TestShadow:
    a = 'default'

    def __init__(self):
        self.a = 'instance default'

assert TestShadow.a == 'default'
assert TestShadow().a == 'instance default'

# Note: this fails
# class TestScoping:
#     a = 'testing'

#     def hey(self):
#         return a 

# assert TestScoping().hey() == 'testing'

# Both local and global (since it's module level)
test_scoping_global = 'wow'

class TestScoping:
    def hey(self):
        # free variable
        return test_scoping_global 

assert TestScoping().hey() == 'wow'
# this can be an entire blog post: https://stackoverflow.com/questions/15374857/should-all-python-classes-extend-object

# Important point
# The scope of names defined in a class block is limited to the class block; it does not extend to the code blocks of methods – this includes comprehensions and generator expressions since they are implemented using a function scope. This means that the following will fail:

# class A:
#     a = 42
#     b = list(a + i for i in range(10))

# Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. 

# aka these are specific k v pairs and a chain of them make up the execution context or environment

namespace_a = 1
class TestNamespace:
    namespace_a = 2 

    def hey(self):
        return self.namespace_a

def test_namespace():
    namespace_a = 3
    return namespace_a 

assert namespace_a == 1
assert TestNamespace().hey() == 2
assert test_namespace() == 3

# key text:

A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

# in plain english, if a reference to the name tries to find it in THAT namespace in that part of the code, then that's the scope
# this is another way of saying "the regions where this binding can be accessed"

# wikipedia:  scope of a name binding – an association of a name to an entity, such as a variable – is the region of a computer program where the binding is valid: 

# Although scopes are determined statically , they are used dynamically. At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:

# statically, meaning it's lexically scoped. Where a name binding CAN be accessed when the program runs is determined by the source code layout of the program hence static
# now this is confusing. scopes do not have namespaces. A namespace has a scope. We really mean "context" here. 
    # the innermost scope, which is searched first, contains the local names
    # the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
    # the next-to-last scope contains the current module’s global names
    # the outermost scope (searched last) is the namespace containing built-in names

# so there's the local context which is just the function namespace. Then context of enclosing functions and their namespaces, then module level (note we jumped pass class)
# then finally the builtins

# iteration. Going through objects
# closures?
# lambda functions
# introspection
# debugging
# importing modules
# publishing packages
# installing 3rd party packages
# I/O
# digging into python itself
# next: extracting key concepts / propositions thus far
# key vs non key. or rather things worth looking up reference type knowlege vs foundational / structural knowledge. 