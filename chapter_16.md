# I/O


First of all, don't look for File class. this aint ruby. all of the file operations are done using builtins. yes this is a lot like php. whatever.

all u gotta know for MOST use cases of doing i/o on text files where you just want to operate with strings is:

open(file_path, mode)

there's other shit obviously but 3 things

1. open returns a file object. it supports .read and .write.
2. file path can be absolute or relative
3. mode is what the fuck you want to do with the file. this sets constraints. if you don't want a file to be writable in ur program, obviously don't open it with write enabled.

in terms of remembering modes, 

read is default. safest. r 
w is write. when u write, it overwrites everything.
x lets you create! 
a lets you write but in an append stile

those are ALL the ones you need in MOST cases. to recap

r is most restrictive. all u can do is read. file must exist.
w is write. file must exist. CANNOT READ.
a is write with append. file must exist. READ
x is create AND read and WRITE. FILE DOES not have to exist

digging deeper:

* encoding
* binary files?
* auto matic close using context managers:

with open('wow', 'w') as x:
...     x.write('fukme')



