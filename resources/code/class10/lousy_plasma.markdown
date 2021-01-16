---
layout: hw
title: lousy_plasma.py
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
</style>

<div markdown="block" class="assignment">

#  lousy_plasma.py 

<aside>This exercise is based on materials from Professors Case, Engel, and Kapp</aside>

Write a program that takes the [lyrics to Taylor Swift's song](http://genius.com/Taylor-swift-bad-blood-lyrics), Bad Blood, and replaces a half of its words with synonyms. With enough of the song changed, you can create your own hit song and roll in the money! 	&#128176;&#128176;&#128176;

The last parts of this exercise depend on a [thesaurus file](thesaurus.txt) and a [lyrics file](bad_blood.txt) that you'll have to download (__right-click and save as...__) to the same directory that your program is in.

This exercise will cover recent material on:

* dictionaries
* file i/o

<hr>

##  Part 0

Start off with creating a thesaurus by using a Python dictionary. The thesaurus only has 2 entries in it:

<pre><code data-trim contenteditable>thesaurus = { 
    "happy": "glad",
    "sad"  : "bleak" 
}</code></pre>

The dictionary contains two keys - <code>"happy"</code> and <code>"sad"</code>. Each of these keys holds a single synonym, a string, for that key.

Write a program that asks the user for a phrase. Then compare the words in that phrase to the keys in the thesaurus. If the key can be found, you should replace the original word with a random synonym for that word. Words that are changed in this way should be printed in UPPERCASE letters. Make sure to __remove all punctuation__, but __keep letters/numbers and spaces__ from your initial phrase so that you can find all possible matches (numbers probably don't matter that much, though). Here's a sample running of your program:

__Example Interaction__

<pre><code data-trim contenteditable>Enter a phrase
> Happy Birthday! exclaimed the sad, sad kitten
GLAD birthday exclaimed the BLEAK BLEAK kitten</code></pre>

Notice that the 1st sad was substituted, and the comma was removed.

__Hints__

* Removing punctuation and keeping letters, numbers and spaces
	* One way to do this is to accumulate all of the characters that are alphanumeric (<code>my_character.isalnum()</code>) or space
	* While it's not required, it might be useful to move this functionality into a separate function (maybe call it <code>remove_punctuation</code> ... have it take a string and return a new string
* Breaking apart a string into single words
    * Multiples ways of doing this
    * Here are a couple of suggestions:
	    * Accumulate until you see space, then you know you have a word
	    * __OR__ simply use <code>split</code>, and then <code>join</code> at the end

<hr>

##  Part 1

Modify your program above so that the thesaurus word can have more than one synonym for each word:

<pre><code data-trim contenteditable>thesaurus = { 
    "happy":["glad",  "blissful", "ecstatic", "at ease"], 
    "sad":["bleak", "blue", "depressed"] 
}</code></pre>

In this version, the dictionary contains two keys - <code>"happy"</code> and <code>"sad"</code>. Each of these keys holds a list that contains synonyms of that key.

Change your original program by replacing the original word with a __random__ synonym for that word. Again, words that are changed in this way should be printed in UPPERCASE letters. Here's a sample running of your program:

__Example Interaction__

<pre><code data-trim contenteditable>Enter a phrase
> Happy Birthday! exclaimed the sad, sad kitten
ECSTATIC birthday exclaimed the DEPRESSED BLEAK kitten</code></pre>

<hr>

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
    * you'll have to lean out all punctuation again, and only keep letters/numbers and spaces
    * break apart into single words
    * substitute with a random word from thesaurus
4. However, only do this in 1 out of every 2 words that are found in the thesaurus... 
    * that is, if you a word from the lyrics is found in the thesaurus
    * there is a 50% chance that it will be substituted with the thesaurus word
5. Again, words that are swapped should be printed in all UPPERCASE letters. 
6. Print out the new lyrics!
7. Profit!!!

See a sample running of the program below (note that you can simply remove all punctuation from the lyrics once you've read them in from the source file):

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
