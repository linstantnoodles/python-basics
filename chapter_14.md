# Generators

In this video you're going to learn what python generators are..

Here's a definition of a function that returns a single value. When I run this program, we expect see the number 1 printed.

Great, now let’s replace the return keyword with the yield keyword. Now we get an object of type generator.

1) Any function definition containing the yield keyword is a _generator function_.
2) Calling the generator function returns a _generator object_.

Now, let’s turn our attention to what we can do with this generator object. First, I’ll save it into the variable “x”. 

This object implements a __next__ method. Therefore, this object is an iterator! In python, calling __next__ is a way of retrieving values from an iterator. 

I’m going to add print statements into our generator function to illustrate what happens when we call __next__ on this generator object.

<Run it once> 
<Run it another time> 

<Run it with another yield and print> 

3 main things are happening here:

1) Each time we call __next__, the generator function executes the statements in the body. Just like a typical function call!
2) During execution, when it encounters a yield statement, the value in from of yield becomes the return value of __next__. We can say that the value was yielded.
3) Before the value is yielded, the state of the function is saved.

Essentially, what we have here is a resumable function. It returns something once, and can return something else at another point in time!

Now it’s time for you to answer some questions before we move on to the next video. 

if we wanted to count to 10, how would this function change? What are some different ways we can write this function to return values 1 to 10?

I’ll leave that as an exercise for you and we’ll explore those questions and more in the next video. 

I hope that was helpful.

If you liked this video and want to see more tutorials like this, please subscribe. And if you have any questions whatsoever, please leave them in the comments section below.




Now if we wanted to count to 10, we wouldn't want 10 yield statements. In part two, we’ll look at a more complex example involving a loop inside the function.

In the first call to next, the condition is false so we'll print and yield count. If we call it again, the function resumes. 

While calling __next__ repeatedly is a way to retrieve values from generator iterators, it's typically not used in real world code. If I wanted to print all 10 values for this function, I’d have to either write __next__ 10 times or write a loop to call __next__.

I'm only using it to highlight this defining behavior: that you can retrieve values over different points in time during program execution from a generator function. This is different from the typical behavior of functions, which return values at one point in time during program execution.

In practice (which is to say in the real, professional world), generator iterators are often used in for loops just like any other iterator. For statements expect iterators and take care of repetedly calling __next__ and handling StopIteration errors.

So if we rewrote our statement to be a for loop, we'll see all 10 numbers printed without having to worry about calling __next__ ourselves or handling the StopIteration error.

I hope that was helpful.

If you liked this video and want to see more tutorials like this, please subscribe. And if you have any questions whatsoever, please leave them in the comments section below.




Challenges
Dont ‘really use _-next__ manually in real code. Feels weird to be teaching using __next__ 
How slow should I talk? How often do I repeat concepts? 
How do I best introduce methods on objects? Using DIR? Or just pointing out that it has it. 
