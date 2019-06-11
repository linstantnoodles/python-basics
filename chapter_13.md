# Comprehensions 

I think comprehensions are one of the most powerful language constructs ever created.

The basic grammar for a comprehension is:

for <expression> in <iterable> <condition> (optional)

This is equivalent to the functional paradigms map and select (or filter) since our expression does not modify the existing list and instead creates an entirely new list.

squaring every integer 



numbers = [1, 2, 3]


result = map(lambda x: x * x, numbers)
squared = list(result)


result = []
for i in numbers: 
	result.append(i * i)
return result

[i * i for i in numbers]

If you want to perform filtering without doing any transformation of each element, just provide a condition: 

[i for i in numbers if i % 2 == 0]

If you want to do both (not straightforward in a map or filter function which are more specialized), you can! 

[i * i for i in numbers if i % 2 == 0]

note: this should def. come after the iterator chapter. 

and before the generator chapter