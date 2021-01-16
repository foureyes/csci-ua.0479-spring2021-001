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
##  Review Files!

__In Python, what built-in function do we use to interact with files?  How many parameters does it have, and what does it return?__ &rarr;

<div class="fragment" markdown="block">

* __open__ opens a file for reading or writing
* it takes two arguments: a __filename__ and a __mode__
	* __filename__ - the _absolute_ or _relative_ path from your program to the file you're opening
	* __mode__ - can be one of the following:
		* __'w'__ - write
		* __'r'__ - read
		* __'a'__ - append
* it returns a __file__ object
</div>
</section>

<section markdown="block">
##  A File Object ...

* is an object that allows your program to manipulate/read/write to an actual file on disk
* to create a file object and open a file, use the built-in function, __open__()

<pre><code data-trim contenteditable>
#  my_input_file is a file object
my_output_file = open("myfile.txt", "w")
</code></pre>
</section>

<section markdown="block">
##  Putting Data Into a File

__What are the steps for opening a file and putting data into it?  What file object method is used for putting data into a file?__ &rarr;
</section>

<section markdown="block">
##  Writing to a File

1. Get a file object using open with write mode: __open('filename', 'w')__
	* filename is the file to be opened
	* __'w'__ means that the file will be opened for writing
	* if the file doesn't exist, __'w'__ will __create__ it
	* if the file exists, __'w'__ will __overwrite__ it!
2. Use the __write__ method on the file object to write data to the file
	* takes a string as an argument (non-string will give a TypeError)
	* does not automatically add new lines
3. Use the __close__ method on the file object when you're done
</section>

<section markdown="block">
##  Writing to a File Code

<pre><code data-trim contenteditable>
#  open using mode 'w'
my_output_file = open("myfile.txt", "w")

#  use the write method
f.write("Monday\n")
f.write("Tuesday\n")
f.write("Wednesday\n")

#  close when you're done
f.close()
</code></pre>
</section>

<section markdown="block">
##  Retrieving Data From a File

__What are the steps for opening a file and retrieving data from it?  What file object methods can be used for reading data from a file?__ &rarr;
</section>

<section markdown="block">
##  Reading a File

__What about reading?__ &rarr;

1. {:.fragment} Get a file object using open with read mode: __open('filename', 'r')__
	* filename is the file to be opened
	* __'r'__ means that the file will be opened for reading
2. {:.fragment} To read data...
	* iterate over the file object itself (reads one line at a time)
	* or use __readline()__
    * or... __read()__
	* or lastly, __readlines()__
3. {:.fragment} Use the __close__ method on the file object when you're done
</section>

<section markdown="block">
##  Methods for Reading a File

All of the following methods do not have any parameters.

* __readline()__ - reads in a single line (with newline at the end of each line)
* __read()__ - reads in entire contents of a file as a string
* __readlines()__ - reads in __entire contents__ of a file as a list of lines

</section>

<section markdown="block">
##  Examples

The following examples assume the presence of a file called __ingredients.txt__ ([download here](ingredients.txt) - right-click and save as) in the same folder/directory as your program.

The contents of the file is:

<pre><code data-trim contenteditable>
3:tomatoes
1:garlic cloves
2:green peppers
</code></pre>

([Download](ingredients.txt) or recreate to follow along)
</section>

<section markdown="block">
##  Reading a File With Iteration

__A file object is actually iterable!__ &rarr;

* it gives you one line at a time as a string
* each line has a new line at the end
* iteration ends automatically when there are no more lines to read

<pre><code data-trim contenteditable>
my_input_file = open('ingredients.txt', 'r')
for line in my_input_file:
    print(line)
my_input_file.close()
</code></pre>
</section>

<section markdown="block">
##  Output of Reading a File With Iteration

Notice the extra new lines...

<pre><code data-trim contenteditable>
3:tomatoes

1:garlic cloves

2:green peppers

</code></pre>

You can use the string method, strip(), to get rid of them.

<pre><code data-trim contenteditable>
print(line.strip())
</code></pre>
</section>

<section markdown="block">
##  Reading a File With readline()

__The readline() method also reads in one line at a time__ &rarr;

* it always returns a string, even if it's just a new line character ("\n")
* if it returns an empty string, then we've reached the end of the file
* you'll have to loop forever and break on empty string

<pre><code data-trim contenteditable>
my_input_file = open('ingredients.txt', 'r')
while True:
    line = my_input_file.readline()
    if len(line) == 0:
        break
    print(line)
my_input_file.close()
</code></pre>
</section>

<section markdown="block">
##  Output of Reading a File With readline()

As with iteration, there are extra new lines:

<pre><code data-trim contenteditable>
3:tomatoes

1:garlic cloves

2:green peppers

</code></pre>

Again, you can use the string method, strip(), to get rid of them.

<pre><code data-trim contenteditable>
print(line.strip())
</code></pre>
</section>


<section markdown="block">
##  Reading a File With readlines()

__You can also call readlines (with an s) to just read the the entire contents of a file as a list__ &rarr;

* returns a list (see the 2nd line in the example code)
* each line is an element in a list
* each line still has a newline character at the end

<pre><code data-trim contenteditable>
my_input_file = open('ingredients.txt', 'r')
lines = my_input_file.readlines()
print(lines)
my_input_file.close()
</code></pre>
</section>

<section markdown="block">
##  Output of Reading a File With readlines()

The list is printed out.  Notice the newlines (as usual!). 

<pre><code data-trim contenteditable>
['3:tomatoes\n', '1:garlic cloves\n', '2:green peppers\n']
</code></pre>

Of course... you can then iterate over every item in the list:
<pre><code data-trim contenteditable>
for line in lines:
  print(line)
</code></pre>
</section>



<section markdown="block">
##  Finally, Reading a File with read()

__Use the read() method on your file handle object to read the file in all at once.__  

__read__() returns the entire contents of a file (including newlines) as a string.

<pre><code data-trim contenteditable>
my_input_file = open("ingredients.txt", "r")
contents = my_input_file.read()
print(contents)
</code></pre>

</section>

<section markdown="block">
##  Output of Reading a File With read()

Contents contains a string representing all of the data in the file.

<pre><code data-trim contenteditable>
3:tomatoes
1:garlic cloves
2:green peppers
</code></pre>
</section>


<section markdown="block">
##  Some Exercises
</section>

<section markdown="block">
##  Double the Ingredients

* using the original [ingredients.txt](ingredients.txt) file...
* open the file
* read every line
* double the number in the beginning of each line
* write out the new number and the ingredient in a new file called ingredients2.txt
</section>

<section markdown="block">
##  Let's Do This Step By Step
</section>

<section markdown="block">
##  Reading the Ingredients

__Let's try printing out every line in the ingredients file first:__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
my_input_file = open('ingredients.txt', 'r')
for line in my_input_file:
    print(line)my_input_file = open('ingredients.txt', 'r')
my_input_file.close()
</code></pre>
</div>
</section>

<section markdown="block">
##  Extracting Meaningful Information

__Let's add code to get the number out of each line, double it, and print it out along with the ingredient:__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
#  there's a problem with this solution...
my_input_file = open('ingredients.txt', 'r')
for line in my_input_file:
	number = int(line[0])
	# notice that we're using strip to get rid of the excess new line
	print(str(number * 2) + line[1:].strip())
my_input_file.close()
</code></pre>

__This solution works for the data that's currently in the file, but...__
</div>
</section>

<section markdown="block">
##  Extracting Meaningful Information Part 2

__What if the number in the beginnin of the line had 2 digits? ...like 10:cloves of garlic.__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
#  use split on the string...
my_input_file = open('ingredients.txt', 'r')
for line in my_input_file:
	clean_line = line.strip()
	parts = clean_line.split(":")
	number, ingredient = int(parts[0]), parts[1]
	print("%s:%s" % (number * 2, ingredient))
my_input_file.close()
</code></pre>
</div>
</section>

<section markdown="block">
##  Extracting Meaningful Information Part 2

__Now... let's write out the ingredients rather than printing out to the screen.__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
my_input_file = open('ingredients.txt', 'r')
#  add a file to write to
my_output_file = open('ingredients.txt', 'w')
for line in my_input_file:
	clean_line = line.strip()
	parts = clean_line.split(":")
	number, ingredient = int(parts[0]), parts[1]
	# write to file instead of print
	my_output_file.write("%s:%s\n" % (number * 2, ingredient))
my_input_file.close()
my_output_file.close()
</code></pre>
</div>
</section>

{% comment %}
<section markdown="block">
##  More Reading and Writing

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

{% endcomment %}

<section markdown="block">
##  Jane Austen

You can download a text version of [Pride and Prejudice](http://www.gutenberg.org/cache/epub/1342/pg1342.txt) from Project Gutenberg

__Using that file with our pig_latin and translate_passage functions... can you write out a pig latin version of Pride and Prejudice?__

Also... these are [sort](http://en.wikipedia.org/wiki/Sense_and_Sensibility_and_Sea_Monsters) [of](http://en.wikipedia.org/wiki/Pride_and_Prejudice_and_Zombies) from Jane Austen....

</section>

<section markdown="block">
##  Downloading the File

Save the text version of [Pride and Prejudice](http://www.gutenberg.org/cache/epub/1342/pg1342.txt) in the same folder that your program is in.

</section>

<section markdown="block">
##  Pig Latin

<pre><code data-trim contenteditable>
def to_pig_latin(w):
    """translates word to pig latin"""

    w = w.lower()

    if not w.isalpha():
        return w

    if w == '' or len(w) == 1:
        return w

    if w[0] in 'aeiou':
        return w + 'way'

    first_two = w[0:2]
    if first_two == 'qu' or first_two == 'ch' or first_two == 'sh' or first_two == 'th':
        return w[2:] + first_two + 'ay'

    return w[1:] + w[0] + 'ay'
</code></pre>
</section>

<section markdown="block">
##  Translate Passage

<pre><code data-trim contenteditable>
def translate_passage(passage):
    """translates text into pig latin"""
    translation = ""
    word = ""
    for c in passage:
        if not c.isalpha():
            translation += to_pig_latin(word)
            translation += c
            word = ""
        else:
            word += c
    if len(word) > 0:
        translation += to_pig_latin(word)
    return translation
</code></pre>
</section>

<section markdown="block">
##  Putting it All Together

<pre><code data-trim contenteditable>
#  open file for reading
fh_in = open('pg1342.txt', 'r')
s = fh_in.read()
fh_in.close()

#  translate and write
fh_out = open('pg1342_translated.txt', 'w')
fh_out.write(translate_passage(s))
fh_out.close()
</code></pre>
</section>
