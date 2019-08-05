# List Comprehensions 

## Examination

An examination for every topic consists of tasks that (usually) gets progressively more complex. I say usually because the previous task may be exercising a completely different concept. If you're able to complete all of them pretty easily, then you probably understand the subject pretty well. 

What if I struggle or get it wrong? 

Take a look at the solution and the accompanying explanation. Each general topic will also have an accompanying chapter that provides a overview of the subject. I recommend using the overview as: a big picture view, to get a first pass, elementary view of the subject. 

The key will be to actually write code which only the examinations will provide. Tasks will offer concrete ways for you to exercise / experiment / explore concepts touch upon in the tutorial. It touches on edge cases and gives yo uopportunity to play around in your own environment and see what happens. It's this engagement with the concepts through coding where you'll be able to further cement your understanding. Reading is one thing, actually testing your understanding through real code is another.

Combine this with drills.

Drills are not designed to expose misconceptions or teach concepts. They're designed to do one thing: increase speed of execution. You may really understand list comprehensions and have an accurate mental model - but how quickly can you write one? do you still find yourself writing basic for loops first and manually converting them? (two step process that).

What are some drills you do in basketball? shooting free throws 1000 times? 

trait of a drill: repetition and FORM / technique. Now we don't have a physical form, but the way in which you THINK about using a language feature is a form. 

- x for x in something
- long expression for x in something for y in something if y in something and m i nsomething 


Write a list comprehension which takes a list of N integers and returns a new list containing their squares.

Example 1:
input: []
output: []
explanation:

Example 2: 
input: [1, 2, 3]
output: [2, 4, 9]
explanation:

Write a list comprehension which takes a list of N strings and returns a new list containing the length of each name.

Example 1:
input: ['Paul', 'John']
output: [3, 4]
explanation: 

Write a list comprehension which takes a list of N integers and for each integer, double it if it's an even number. Otherwise, triple it.

Example 1:
input: [1, 2, 3]
output: [3, 4, 9]


Write a list comprehension which takes a single integer N and returns a sequence of N numbers from 1 to N.

Example 1:
input: 3
output: [1, 2, 3]

Write a list comprehension that takes a list of N integers and return a list containing only the even ones.

Example 1:
input: [1, 2, 3, 4, 5]
output: [2, 4]

Write a list comprehension that takes a list of N integers and a returns a list of ones that are divisible by 3 or 5.

Example 1:
input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output: [3, 5, 6, 9, 10]

Extra: return the squares

Write a list comprehension that takes a list of N integers and returns a list containing the square of squares. Use _two_ comprehensions.

Example 1:
input: [1, 2, 3]
output: [1, 16, 81]

Write a list comprehension that takes a list of integers and returns a list of lists where each sublist contains the same number of stars (`*`) as integer value.

Example 1:
input: [1, 2, 1]
output: [[`*`], [`*`, `*`], [`*`]]

Write a list comprehension that takes two lists of integers A and B and returns a new list containing all possible pairs made with an element in A and an element in B.

Example 1:
input: 
arg1 = [1, 2]
arg2 = [3, 4]
output: 
[(1, 3), (1, 4), (2, 3), (2, 4)]

Extra: Exclude pairs where the first element of the pair is even.
arg1 = [1, 2]
arg2 = [3, 4]
output: 
[(1, 3), (1, 4)]

Write a list comprehension which takes a list of integers and returns a matrix (list of lists) which each list is that integer repeated K times.

Example 1:
arg1 = [1, 2, 3]
arg2 = 2
output:
[[1, 1], [2, 2], [3, 3]]

Example 2:
arg1 = [1, 2, 3]
arg2 = 3
output: 
[[1, 1, 1], [2, 2, 2], [3, 3, 3s]]

Write a list comprehension which flattens a matrix.

Example 1: 
input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

Extra: flatten a matrix of matrices.

Example 1: 
input: [[[1], [2], [3]], [[4], [5], [6]]]
output: [1, 2, 3, 4, 5, 6]