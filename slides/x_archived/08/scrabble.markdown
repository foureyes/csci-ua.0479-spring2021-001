---
layout: slides
title: Scrabble
---
<section markdown="block" class="title-slide">
#  Scrabble
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  And Now... Scrabble(?)

Imagine that you're playing Scrabble (or... Words With Friends?).  

What are some _valid_ words can you create if you have the following letters left in your rack of tiles? 

__t__, __r__, __c__, __a__

</section>

<section markdown="block">
###  Whatever List We Came Up With...

_It's probably not complete_

<div class="incremental" markdown="block">
{% highlight python %}
act
ar
arc
art
at
car
cart
cat
rat
ta
tar
{% endhighlight %}

__So ... who do you think would be _particularly_ good at finding valid scrabble words from a set of letters?__
</div>
</section>

<section markdown="block">
##  As Always...  Let's let the computer do this for us

</section>

<section markdown="block">
###  You Saw This Coming

Let's write a program that asks for a set of letters, and determines all of the valid words that can be created by that set of letters.  

It'll probably look like this:

{% highlight python %}
Please enter some letters
> trca
act
ar
arc
art
at
car
cart
cat
rat
ta
tar
{% endhighlight %}

(__let's check out a demo__ &rarr;)
</section>

<section markdown="block">
###  Scrabble Solver

* write a program that asks for input (a set of letters)
* it should print out all of the combinations of letters that make valid words _in alphabetical order_
* don't worry about an empty string for now
</section>

<section markdown="block">
###  Some Questions About the Scrabble Solver....

__What data will we need?__  __Can we break this problem down into smaller parts?__ &rarr;

<div class="incremental" markdown="block">
* data...
	* a dictionary or list of valid words
	* the letters that the user entered
* implementation...
	* ask the user for input
	* find a list of valid words and load that list into the program
	* devise algorithm to determine if word can be formed from input
</div>
</section>

<section markdown="block">
###  We Know How to Do This (Mostly)

So...  finding a list of valid words and loading it is the only part that's new for us.

* first off... there are a [bunch of freely available word lists online](http://www.puzzlers.org/dokuwiki/doku.php?id=solving%3awordlists%3aabout%3astart)
* [This one (enable1.txt)](http://www.puzzlers.org/pub/wordlists/enable1.txt) is pretty popular
* but then, we'll have to learn how to get that list into our program
* which is why we're going to talk about __file input and output__ (or File I/O for short)
</section>

<section markdown="block">
##  So... Let's Look at _File Input and Output_!
</section>

<section markdown="block">
##  ... Aaaaaand We're Back!
</section>

<section markdown="block">
###  Scrabble Solver 

Write a program that...

* asks the user a set of letters
* print out all of the combinations of letters that make valid words _in alphabetical order_
* don't worry about an empty string for now

{% highlight python %}
Please enter some letters
> rhtu
hurt
hut
rut
ruth
thru
uh
ut
{% endhighlight %}
</section>

<section markdown="block">
###  A Strategy...

* create a function called find_words
	* it should take two arguments, 
		* letters (the set of letters to choose from) and dictionary (the file name of the scrabble dictionary)
		* it should open the file
	* ...and find valid words from the set of letters
	* ...and return a list of valid words
* get user input 
* use the function, find_words, to get valid words
* print out result
* remeber to [download a word list - enable1.txt](http://www.puzzlers.org/pub/wordlists/enable1.txt)
</section>
<section markdown="block">
###  Pseudocode Without Going Through All Permutations

We could try finding every permutation of letters in a word, including substrings... and checking for a substring.

However, there's a way to do this by going through every word in the list and seeing if the letters can form that word. __How__ &rarr;

<div class="incremental" markdown="block">
* for every word in the dictionary
* check if each letter exists in a copy of your set of all letters
* if it does, "remove" it from your copy (it's been exhausted)
* if it doesn't, then your letters can't create the dictionary word
</div>
</section>

<section markdown="block">
###  Potential Solution With Readline

{% highlight python %}
def find_words(letters, dictionary):
    words = []
    f = open(dictionary, 'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        word = line.strip()
        temp_letters = list(letters)
        letters_in_word = True
        for char in word:
            if char in temp_letters:
                temp_letters.remove(char)
            else:
                letters_in_word = False
                break
        if letters_in_word:
            words.append(word)
    f.close()
    return words
{% endhighlight %}
</section>

<section markdown="block">
###  Potential Solution Iterating Over a File Object

{% highlight python %}
def find_words(letters, dictionary):
    words = []
    f = open(dictionary, 'r')
    for line in f:
        word = line.strip()
        temp_letters = list(letters)
        letters_in_word = True
        for char in word:
            if char in temp_letters:
                temp_letters.remove(char)
            else:
                letters_in_word = False
                break
        if letters_in_word:
            words.append(word)
    f.close()
    return words
{% endhighlight %}
</section>

<section markdown="block">
###  Main Function

{% highlight python %}
def main():
    dictionary_file_name = 'enable1.txt'
    answer = input('Please enter some letters\n> ')
    possible_words = find_words(answer, dictionary_file_name)
    possible_words.sort()
    for w in possible_words:
        print(w)

main()
{% endhighlight %}
</section>

<section markdown="block">
##  Recursive Solution

__If you wanted to use recursion to get all permutations...__ &rarr;

<div class="incremental" markdown="block">

{% highlight python %}
def find_perms(s):
    if len(s) == 1:
        return [s]
    perms_list = []
    found_perms = find_perms(s[1:])
    for perms in found_perms:
        for i in range(len(perms) + 1):
            perms_list.append(perms[0:i] + s[0] + perms[i:])
    # include sliced off letter and found sub perms
    return [s[0]] + perms_list + found_perms

print(find_perms('ab'))
print(find_perms('abc'))
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  Or... Using a Module

(But this just gives you permutations, doesn't include substrings).

{% highlight python %}

def find_perms(s):
    import itertools
    l = list(s)
    return [''.join(perm) for perm in itertools.permutations(l)]

print(find_perms('ab'))
print(find_perms('abc'))
{% endhighlight %}



</section>

