---
layout: slides
title: Idioms and Style 
---

<section markdown="block" class="title-slide">
#  Idioms and Style
{% include title-slide-footer.html %}
</section>


<section markdown="block">
###  Idioms

__What's an idiom?__

<div class="incremental" markdown="block">
* an __idiom__ can be:
	* a saying or expression whose meaning is not obvious from its individual parts  
	* an expression that is natural to a language
* generally native speakers, or people who _know_ the language, know the idioms
	* _it's raining cats and dogs_
	* _hace mucho frío_
	* _les carottes sont cuites_
</div>
</section>

<section markdown="block">
###  Some French and Spanish Idioms


BTW, does anyone know the literal and idiomatic translations for these sayings?

* _hace mucho frío_
* _les carottes sont cuites_

<div class="incremental" markdown="block">
* _hace mucho frío_
	* it makes much cold
	* it's very cold
* _les carottes sont cuites_
	* the carrots are cooked
	* I've had enough!
</div>
</section>


<section markdown="block">
###  Idioms in Programming Languages
<aside>Similar to Natural Languages</aside>

An __idiom__ in a programming language is:

* a common task, computation, or construct that's expressed in a way that's unique, peculiar to or encouraged by the particular programming language in use
* usually only those who use the language often know the idiomatic way to express things...
* shows knowledge of the language, culture, and conventions / norms
</section>

<section markdown="block">
###  More About Programming Language Idioms

* multiple ways to express something, but language or community of language users _prefer_ the idiomatic way
* not necessarily formally specified
* does __not__ have to be followed	
	* if idioms are not used, program can still run 
	* if you don't do it idiomatically, you won't cause errors
</section>

<section markdown="block">
###  Let's See an Example of an Idiom

<aside>In a programming language, of course</aside>

* in Python, there are a few ways to check if a value is in a _list_ of values; two are shown below
* both achieve the same result, but the second version is preferred

{% highlight python %}
#  one way to do it; check each value
if name == 'Kermit' or name == 'Gonzo' or name == 'Skeeter':
    print(name + ' is a muppet!')
{% endhighlight %}

{% highlight python %}
#  the idiomatic way; check for membership in a list
muppets = ['Kermit', 'Gonzo', 'Skeeter']
if name in muppets:
    print(name + ' is a muppet!')
{% endhighlight %}


(we'll look at lists later in the semester)
</section>

<section markdown="block">
###  About Style

* __style__ is how the code is formatted; it's how it looks
* __why is style important__?  &rarr;

<div class="incremental" markdown="block">
* you'll probably spend as much time reading code as writing it:
	1. code you've written
	2. example code from books, specifications, forums, etc.
	3. other people's code (collaboration, inherited code, etc.)
* if everyone follows the same style, it'll be easier to read and edit existing programs
</div>
</section>


<section markdown="block">
###  PEP 8

In Python, an enhancement proposal, called [PEP 8](http://www.python.org/dev/peps/pep-0008/), lays out some good rules to follow.

</section>


<section markdown="block">
###  Here Are a Few Conventions To Follow
* __consistency__ within a file / project!
* __4 space indentation__ (automatic in IDLE) &rarr;
{% highlight python %}
if answer == 5:
    print('correct')!
{% endhighlight %}
* __use blank lines to separate groups of related code__ to enhance readability
{% highlight python %}
x = 2
y = 5

print("x plus y is ...")
print(x + y)
{% endhighlight %}
</section>

<section markdown="block">
###  And a Few More...
* __surround operators with whitespace__ in expressions
{% highlight python %}
#  do this:
count = count + 1
#  *not* this:
count=count+1
{% endhighlight %}
* __only use lowercase letters in variables names__
{% highlight python %}
#  do this:
count = 0
#  *not* this:
Count=0
{% endhighlight %}
* __separate words in variable names using underscores__
{% highlight python %}
#  do this:
my_count = 1
#  *not* this:
mycount = 1
myCount = 1
{% endhighlight %}
<!--_ -->
</section>

<section markdown="block">
##  Make sure your code is formatted in a way that is readable and is consistent with common conventions.

<aside>(Please)</aside>
</section>

