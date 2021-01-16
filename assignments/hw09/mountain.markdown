---
layout: homework
title: mountain.py
---
<link href='https://fonts.googleapis.com/css?family=Merriweather:400,700,400italic,700italic' rel='stylesheet' type='text/css'>

<style>
# bd { 
	background-color: #eee;
}

# content {
	padding-top: 0 !important;
}

.assignment {
	background-color: #fff;
	max-width: 37em;
	margin: auto;
	padding: 1em 2em;
	margin: auto;
	line-height:1.5;
	font-family: 'Merriweather', Georgia, 'Times New Roman', Times, serif;
}

aside {
	font-size: 0.75em;
}

.assignment h1, .assignment h2, .assignment h3 {
	color: #530510 !important;
}

.assignment h1 {
	font-size: 2.747em;
}

.assignment h2 {
	font-size: 0.874em;
}

.assignment h3 {
	font-size:1.229em;
}

code {
	color: #530510;
	font-size: 1.15em;
	background-color: #fee;
	padding: 0.25em 0.5em 0.25em 0.5em;
}

pre code {
	background-color: #fee;
	padding: 0em !important;
}

pre {
	background-color: #fee;
	padding: 0.25em 0.5em 0.25em 0.5em;
}

.assignment a:visited {
	color: #556699 !important;
}

.assignment a {
	color: #3355bb !important;
}

img {
    width: 75%;
    height: 75%;
}
</style>

<div markdown="block" class="assignment">

#  mountain.py (just for fun!)


Write a program that randomly generates rocky mountains. Do this using:


* lists of tuples
* turtle

Here's a few examples of mountains rendered by this program:

![mountain 1](../../resources/img/mountain1.png)
![mountain 2](../../resources/img/mountain2.png)
![mountain 3](../../resources/img/mountain3.png)


<hr>

##  Part 0

__Set up a turtle program__ and create a function called `draw_line`:

* parameters:
    1. start - a tuple representing a coordinate in a 2-dimensional plane
    2. end - a tuple representing a coordinate in a 2-dimensional plane
* processing:
    * using start and end as end points
    * draw a line from start to end with turtle
* return:
    * (this function does not return any value)
    * None

Test your program:

```draw_line((-100, 0), (100, 50))
```
![line](../../resources/img/mountain_line.png)

##  Part 1

Create a function called `get_midpoint`


##  Part 2

Rather than use a hard-coded dictionary as your thesaurus, use an [external thesaurus file](thesaurus.txt) (right-click and save as... __to where your Python program is__) to populate the keys and values in your dictionary. Use the following line to read in your file (do not use absolute paths):

<pre><code data-trim contenteditable>f = open('thesaurus.txt', 'r') </code></pre>

The data in the file is in the following format:

<pre><code data-trim contenteditable>word1,synonym1,synonym2,...,synonymN-1,synonymN
word2,synonym1,synonym2,...,synonymN-1,synonymN
word3,synonym1,synonym2,...,synonymN-1,synonymN</code></pre>

Every word occupies its own line followed by a comma-separated list of synonyms. Every word can have a potentially unlimited # of synonyms. Your task for this part is to open this file and parse it into a Python dictionary object so that it functions just like the simple thesaurus from the previous part. Here's a sample running of your program:

__Example Interaction__

<pre><code data-trim contenteditable>Enter a phrase
> happy birthday said the sad kitten
CONTENT ANNUAL HOLIDAY PRONOUNCED the DOLOROUS CHESHIRE CAT</code></pre>

__Hints__

Generating the thesaurus will be the trickiest part:

1. For each word in the thesaurus you will need to create a new list that contains all of the synonyms for that word. 
2. You can then store this list in the dictionary using the 1st word as the key.
3. Again, <code>split</code> is incredibly helpful here!

<hr>

##  Part 3

Finally, modify your above program to write a song for you. It'll use another external file, the [lyrics to Taylor Swift's Bad Blood](bad_blood.txt), as a source for lyrics.

1. Download the [lyrics to Bad Blood](bad_blood.txt) (right-click and save as to the same directory that your program is in)
2. Instead of asking the user for a phrase... open the lyrics file (bad_blood.txt), and read the entire contents as a string using <code>file_object.read()</code>
3. Using the same algorithm that you used in the previous program, change the words in the song to a random word from the thesaurus
4. However, only do this in 1 out of every 2 words (that are found in the thesaurus)... so that only 50% of the words are matched in the thesaurus are substituted
5. Again, words that are swapped should be printed in all UPPERCASE letters. Here's a sample running of your program (note that you can simply remove all punctuation from the source file for this program):
6. Print out the new lyrics!
7. Profit!!!

__Example Output__

<pre><code data-trim contenteditable>Cause baby now we got DISAPPROBATION blood
You know it use to be mad love
So PLEASURABLENESS a ATTENTION SOCIALITY what youve done
Cause INFANT now we got bad blood ...</code></pre>

<hr>

##  (Optional) Part 4

If you're on OSX, you won't even have to sing the lyrics that you _"wrote"_! Instead, you can have the computer sing it for you. Use the following lines of code at the end of your programming, substituting the variable <code>lyrics</code> with your own variable that contains lyrics:

<pre><code data-trim contenteditable># lyrics is the variable that contains the new lyrics to your song
from os import system
system("say -i -v Fiona " + "\"" + lyrics + "\"")</code></pre>

</div>
