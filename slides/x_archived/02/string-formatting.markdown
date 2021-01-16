---
layout: slides
title: String Formatting with %
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Putting Strings Together

__We've already learned one way to put together strings. What is it? &rarr;__

<div class="fragment" markdown="block">
* concatenation (__+__)
* "string 1" + " string 2" &rarr; "string 1 string 2"
</div>
</section>

<section markdown="block">
##  There's Also String Formatting with %

__String formatting__ allows you to put placeholders in your string where values should go.  

* one way to this is to use the __%__ operator 
* (there's a more modern syntax, but you'll still see this a lot)
* the __%__ sign signals that the string on the left will be populated by the comma separated values enclosed in parentheses on the right
* __%s__ will represent a placeholder in your string

<pre><code data-trim contenteditable>
s = "string"
print("this is a %s" % (s))
</code></pre>
</section>

<section markdown="block">
##  Multiple Values

* more than one %s in the string
* each substitute value separated by comma
* the original string can be a variable with a value of a string with placeholders 

<pre><code data-trim contenteditable>
lyrics = "you can get with %s or you can get with %s"
s1 = "this"
s2 = "that"
print(lyrics % (s1, s2))
</code></pre>
</section>

<section markdown="block">
##  String Formatting
__What was it again?__

<div class="fragment" markdown="block">
Allowing placeholders in a string to accommodate variable / value substitution.

<pre><code data-trim contenteditable>
#  note the use of variables... 
#  string formatting doesn't have to consist of string literals!
#  values don't have to be strings!?
greeting = "Hi.  My name is %s and I have %s %s"
name = "Joe"
number_of_pets = 314
pet = "aardvarks"
result = greeting % (name, number_of_pets, pet)
print(result)
</code></pre>
</div>
</section>

<section markdown="block">
##  A Closer Look at String Formatting
<aside>What just happened there?</aside>

* we passed in a non-string type, and it didn't complain
* the placeholder, __%s__, signifies a __string__ substitution
* str is called on the values (convenient!)
* there are other placeholders 
	* like %i or %f, they represent other types, like int and float
	* but they don't necessarily call a conversion function
	* we'll just stick with %s right now
</section>

<section markdown="block">
##  When to Use String Formatting
* less _cumbersome_ than string concatenation
* less error prone!  __why?__
* however, it can get complicated
	* there are even more features to string formatting!
		* supporting / restricting to other data types
		* formatting floats
	* sufficient to just get the basics down for our simple use-cases  
</section>

<section markdown="block">
##  So, What Does print() Do?
Both __string concatenation__ and __string formatting__ evaluate to a value - specifically a string!  That means:

* you can assign it to a variable, etc!
* but for print... the result is None

As for print()

* it just prints out strings; it returns nothing
* using multiple parameters in print let's you skip the construction step
* (again) __but it doesn't give you back a value__
</section>

<section markdown="block">
##  Greetings (Revisited)
__Write a program that asks for the user's name.  The program will print out "Hello (name)" using string formatting.  &rarr;__

<pre><code data-trim contenteditable>
What's your name?
>Joe
Hello Joe!
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
name = input('What\'s your name?\n>')
print("Hello %s" % (name))
</code></pre>
</div>
</section>

<section markdown="block">
##  And Mistakes Were Made
* string concatenation
	* adding a numeric type (we saw this earlier) &rarr;
	* missing quotes, missing plus symbol, etc.  &rarr;
* string formatting
	* not enough arguments (more placeholders than values) &rarr;
	* not all arguments converted (more values than placeholders) &rarr;
</section>
