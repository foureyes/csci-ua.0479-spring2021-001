---
layout: slides
title: File I/O 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Where's My Stuff?

When our programs are run, we usually have a bunch of variables that store numbers, lists, strings and all sorts of other data.  __But where do you think this data is actually stored?__ &rarr;


<div class="fragment" markdown="block">
Our program and the data that our programs have been using is stored in your computer's main memory (really!  I mean, where _else_ would you put values that need to be _remembered_)
</div>
</section>

<section markdown="block">
##  RAM!?

Your computer's __main memory__ or __RAM__ (random access memory) is an example of __volatile memory__.

* __volatile memory__ - memory that requires an electrical current to maintain state
* __non-volatile memory__ - memory that can maintain state without power

__What are some examples of non-volatile memory__ &rarr;

<div class="fragment" markdown="block">
Hard drives, flash drives, CDs and DVDs
</div>
</section>

<section markdown="block">
##  Storing Data in Main Memory

__What are the consequences of your data being stored in your computer's main memory?__ &rarr;

<div class="fragment" markdown="block">
* data may go away at the end of the program, or when the computer gets turned off
* if you're working with large amounts of data, you may run out of RAM (which is typically less than the amount of non-volatile memory that you have)!
</div>
</section>

<section markdown="block">
##  I Want Data to Last Longer Than That

__What if we want to persist our data beyond the lifetime of the running program... or through on-off cycles?__ &rarr;

<div class="fragment" markdown="block">
* let's store data on non-volatile media!
* ... maybe as a file on your hard drive or SSD...
</div>
</section>

<section markdown="block">
##  File Input and Output

* we can store data in files!
* Python can handle file input and output - __file I/O__
</section>

<section markdown="block">
##  open

Python has a __built-in__ function called __open__.  

* __open__ opens a file!
* it can be used for __reading__ or __writing__
* it takes two arguments: a __filename__ and a __mode__
	* __filename__
		* the absolute path... 
		* or relative (to the script that your writing) path
	* __mode__ ... for now, we only care about:
		* __'w'__ - write
		* __'r'__ - read
		* __'a'__ - append
* it returns a __file object__
</section>

<section markdown="block">
##  A File Object ...

* is an object that allows your program to manipulate/read/write to an actual file on disk
* to create a file object and open a file, use the built-in function, __open__()

</section>

<section markdown="block">
##  Writing to a File

<pre><code data-trim contenteditable>
f = open("test.txt", "w")
f.write("I'm in yr filez!\n")
f.write("Writin' some bits!\n")
f.write("...\n")
f.close()
</code></pre>

* call __open__ ...
	* with the name of the file to open, 'test.txt'
	* and the mode, 'w' to specify that we're writing to it
* use the __write__() method to write strings to a file
* you must always call __close__() on  file when you're done with it
</section>

<section markdown="block">
##  Using open to Write to a File

Let's look at __open__ and __write__ in more detail:

__open(filename, mode)__

* filename is the file to be opened
* a mode of 'w' means that the file will be opened for writing
* if the file doesn't exist, 'w' will __create__ it
* if the file exists, 'w' will __overwrite__ it!

__write(s)__

* does not automatically add new lines
* takes a string as an argument (non-string arguments result in an error)
</section>



<section markdown="block">
## Remember to Close It!!!

Once you're done working with your file, __remember to close it by__:

<pre><code data-trim contenteditable>
file_obj.close()
</code></pre>

* if you don't do this, the file may not be written to!
* (if you're interested in a better way to deal with this, look for context managers in the python docs... or the `extra file i/i` slides)

</section>
<section markdown="block">
##  Lottery Ticket

Write a program that creates a lottery ticket.  The lottery ticket should:

* have the words "Lucky Numbers" on the first line
* contain 5 __unique__ numbers between 1 through 59
* each number printed from __lowest to highest__
* each number printed on its own line
* be saved to a file named lotto.txt

<pre><code data-trim contenteditable>
Lucky Number
3
28
33
50
51
</code></pre>
</section>

<section markdown="block">
##  Pseudocode #1

<pre><code data-trim contenteditable>
"""
create a list of numbers
mix up the numbers
open a file
write out 'lucky numbers' to file
get the last 5 numbers from list
sort them
for each number in list
	write it the number
"""
</code></pre>
</section>

<section markdown="block">
##  Pseudocode #2

<pre><code data-trim contenteditable>
"""
create an empty list to store numbers
while length of list < 5
	generate a random number
	if the number isn't in the list of stored numbers
		add it
sort numbers
open a file
write out 'lucky numbers' to file
for every number in the list
	write it to the file
"""
</code></pre>
</section>

<section markdown="block">
##  Potential Solution

<pre><code data-trim contenteditable>
import random

#  generate list of sorted unique random numbers
random_number_list = []
while len(random_number_list) < 5:
    n = random.randint(1, 59) 
    if n not in random_number_list:
        random_number_list.append(n)
random_number_list.sort()

#  write out the list of numbers to a file
file_handle = open('lotto.txt', 'w')        
file_handle.write('Lucky Numbers\n')
for n in random_number_list:
    file_handle.write('%s\n' % n)
</code></pre>
</section>

<section markdown="block">
##  How About Some Tidying Up

__Can we abstract out some of this code into a reusable function?__ &rarr;
</section>

<section markdown="block">
##  Another Version

<pre><code data-trim contenteditable>
import random
def unique_random_list(sample_size, a, b):
    """ 
    sample_size is the number of random numbers to return
    a is the start of the pool of numbers to choose from
    b is the end of the pool of numbers to choose from
    """
    numbers = []
    while len(numbers) < sample_size:
        n = random.randint(a, b)
        if n not in numbers:
            numbers.append(n)
    return numbers 

observed = unique_random_list(3, 1, 5)
assert 3 == len(observed)
for n in observed:
    assert 1 == observed.count(n)

</code></pre>
</section>

<section markdown="block">
##  Another Version Continued

<pre><code data-trim contenteditable>
random_number_list = unique_random_list(5, 1, 59)
random_number_list.sort()
file_handle = open('lotto.txt', 'w')
file_handle.write('Lucky Numbers\n')
for n in random_number_list:
    file_handle.write('%s\n' % n)
</code></pre>
</section>



<section markdown="block">
##  BTDubz (re random)

By the way... (of course) there's already a function in the random module that does this: 

* random.__sample__(population, k)
	* __population__ - a sequence or set (think list) containing the elements to sample from
	* __k__ - the number of elements to retrieve
* example output:

<pre><code data-trim contenteditable>
>>> print(random.sample([1, 2, 3, 4, 5, 6, 7], 4))
[7, 3, 1, 6]
>>> print(random.sample([1, 2, 3, 4, 5, 6, 7], 4))
[7, 5, 4, 6]
>>> print(random.sample([1, 2, 3, 4, 5, 6, 7], 4))
[5, 6, 3, 4]
</code></pre>
</section>

<section markdown="block">
##  Reading a File

To open a file in read mode, use "r" as the second argument:

<pre><code data-trim contenteditable>
f = open("test.txt", "r")
</code></pre>

</section>

<section markdown="block">
##  Reading a File

Once you have a __file object__ (sometimes called a file handle), you can read the contents of a file by: using one of the following methods on your __file handle object__:

* __iterating__ over the __file object__ itself (use a for loop with the file object)
* using one of the following __methods__ on the __file object__
	* __readline__() - read one line at a time
	* __readlines__() - reads entire contents of a file into memory as a list (each element is a line)
	* __read__() - reads the entire contents of a file into memory as a string

{% comment %}
__Why would you use one method over another?__

<div class="fragment" markdown="block">
* you may want to use read if you're operating on the contents of the file as a whole
* you may want to use readline if you're working with a very large file
</div>
{% endcomment %}
</section>

<section markdown="block">
##  The Easiest Way to Read a File

Once you have a file object, you can actually _iterate_ over the file object itself. That is, you can use a __for loop__ to loop over every line in the __file object__:

<pre><code data-trim contenteditable>
f = open("test.txt", "r")
for line in f:
    print(line)
</code></pre>

</section>

<section markdown="block">
##  Using readline

__readline__() takes no arguments, and it returns a string.

* it always returns a string, even if it's just a new line character ("\n")
* if it returns an empty string, then we've reached the end of the file
</section>

<section markdown="block">
##  Using readline Continued

__To use readline to read the contents of a file, loop forever (or at least until we know that we're at the end of a file! ...__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
f = open("test.txt", "r")
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line)
f.close()
</code></pre>
</div>
</section>

<section markdown="block">
##  Using readline() Continued More!

Using the test.txt file we've used in previous examples:


<pre><code data-trim contenteditable>
I'm in yr filez!
Writin' some bits!\n
...
</code></pre>

__What is the first line that will be printed?  What is the actual string representation? How many times will the loop run?__

<pre><code data-trim contenteditable>
f = open("test.txt", "r")
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line)
f.close()
</code></pre>

<div class="fragment" markdown="block">
* I'm in yr filez!
* "I'm in yr filez!\n"
* 3 times
</div>
</section>

<section markdown="block">
##  Reading a File in All At Once

Use the __read__() method on your file handle object to read the file in all at once.  __read__() returns the entire contents of a file (including newlines) as a string.

<pre><code data-trim contenteditable>
f = open("test.txt", "r")
contents = f.read()
print(contents)
</code></pre>

</section>

<section markdown="block">
##  Reading a File in All At Once

Use the __readlines__() method on your file handle object to read the file in all at once as a list, with each line being a single element in the list. 

<pre><code data-trim contenteditable>
f = open("test.txt", "r")
lines = f.readlines()
for line in lines:
	print(line)
</code></pre>

</section>

<section markdown="block">
##  Memory Efficiency

__Which function uses more main memory, readline or read/readlines? Why?__ &rarr;

<div class='fragment' markdown='block'>
* read/readlines consumes more memory because it reads the entire file at once!
* similarly, in our previous exercises... we had solutions that either used up a lot of memory... or were expensive computationally
</div>
</section>


<section markdown="block">
##  Some Notes...
</section>

<section markdown="block">
##  A File Object and For Loops

__Again, a file object is itself an iterable (you can loop over it using a for loop)... and it reads in chunks of the file as you go along__ &rarr;
 
<pre><code data-trim contenteditable>
f = open('my_file.txt', 'r')
#  read chunks at a time
for line in f:
  print(line)
</code></pre>

</section>


<section markdown="block">
##  Creating Text Files with IDLE

Some of these exercises require you to work with existing text files. So, __how do you create these files__? &rarr;

IDLE can be used to work on files that _aren't_ Python programs. __To save a _plain text_ file__ &rarr;

* go to __new file__ as usual
* ...and __save as__ ... but add __.txt__ as your extension

(You can also open file that aren't .py or .txt in IDLE, as long as they're just _plain text_)

</section>

<section markdown="block">
##  Multiple File Objects

__You can have more than one file object open at a time. The following example:__ &rarr; 

* reads every line from readme.txt 
* writes each line with an exclamation point at the end to a file called writeme.txt
 
<pre><code data-trim contenteditable>
input_file = open('readme.txt', 'r')
output_file = open('writeme.txt', 'w')
for line in input_file:
    output_file.write("{}!\n".format(line))
</code></pre>
</section>

<section markdown="block">
##  File System and Paths

Oh... make sure you know about your [file system and how paths work (see these slides!)](paths.html) &rarr;
</section>

<section markdown="block">
##  An Exercise
</section>

<section markdown="block">
##  Reading and Writing

* read the contents of a file called names.txt
* the file will have first names in it
* sort the names by alphabetical order
* write the newly sorted names to another file
* the original file should remain unchanged

The contents of [names.txt (download and save to where your program is)](names.txt) will be:

<pre><code data-trim contenteditable>
Erin
Charles 
Bob
David
Alice
</code></pre>

</section>


<section markdown="block">
##  A Potential Solution

<pre><code data-trim contenteditable>
file_in = open("names.txt", "r")
names = file_in.readlines()
#  or alternatively...
#  contents = file_in.read()
#  names = contents.split("\n")
names.sort()
file_in.close()
file_out = open("names_sorted.txt", "w")
for name in names:
        file_out.write(name + "\n")
file_out.close()
</code></pre>
</section>

