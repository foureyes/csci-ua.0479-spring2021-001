---
layout: slides
title: User Input 
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Getting Input From the Shell

* we can prompt the user through the console / terminal / shell / command prompt
* the user enters input through the same mechanism
</section>

<section markdown="block">
##  The input() Function

There's a built-in function in Python called __input__ ...

* __what does it do? does it have parameter(s)?__ &rarr;
* __(how can we find out through IDLE?)__ &rarr;
* __what does it return?__ &rarr;
* __what if the user input is a number?__ &rarr;

* {:.fragment} __input__ takes one parameter - the prompt that is displayed (think of it as print plus retrieving user input!) 
* {:.fragment} use __help__! or check the docs...
* {:.fragment} it returns a string representing the user's input
* {:.fragment} it will __always return a string__ - even if the user inputs a number
</section>

<section markdown="block">
##  Let's Try Some Examples of input()
<pre><code data-trim contenteditable>
>>> s = input(">")
>foo
>>> type(s)
<class 'str'>
>>> x = input(">")
>5
>>> type(x)
<class 'str'>
>>> x = int(input(">"))
>5
>>> type(x)
<class 'int'>
</code></pre>

</section>

<section markdown="block">
##  The input function does two things: 

* __prints__ out the prompt
* __returns__ the value typed in by the user back to your program

</section>

<section markdown="block">
##  Write a Program That Asks For a Name
... and then says "hi".  Here's the sample output; the text after the &gt; is user input.

<pre><code data-trim contenteditable>
What's your name?
>Joe
Hi Joe
</code></pre>

__A potential solution...__ &rarr;

<pre><code data-trim contenteditable>
print("What's your name?")
name = input(">\n")
print("Hi " + name)
</code></pre>
{:.fragment}

(note that we used __newline__, __\n__, to create a line break for the prompt that's printed out)
{:.fragment}
</section>

<section markdown="block">
##  Write a Program That Adds Exclamation Points
Here's the sample output; the text after the &gt; is user input.

<pre><code data-trim contenteditable>
How loudly?
>4
This is really loud!!!!
</code></pre>
__A potential solution...__ &rarr;

<pre><code data-trim contenteditable>
loudly = input("How loudly?\n>")
print("This is really loud" + "!" * int(loudly))
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##  Review
* how do we get user input?
* when we get input, what's the type of the value that's returned?
</section>

<section markdown="block">
##  [Design, Input, Processing, and Output](design-input-output.html)
</section>
