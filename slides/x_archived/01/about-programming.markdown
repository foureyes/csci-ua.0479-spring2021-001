---
layout: slides
title: About Programming 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  What's a Program?
<aside>And what's all this talk about computer science?</aside>
</section>

<section markdown="block">
##  Here's One!

<pre><code data-trim contenteditable>
{% include classes/01/source/cats.py %}
</code></pre>
<details open markdown="block">
* QUESTION - (next) What does this do?
* QUESTION - (next) What's a program?
</details>
</section>

<section markdown="block">
##  A Quick Exercise
<aside>
What do you think this program does?  Try walking through it line-by-line. &rarr;
</aside>
<div class="fragment" markdown="block">
<p>This program prints out photo posts from tumblr that have at least two tags, with "cat" as one of those tags.</p>
<aside>
Let's try running it (hopefully looking for cats is a sufficiently benign search!). &rarr;
</aside>
{:.fragment}
<p>(You can try this out too if you have your laptop and can follow along)</p>
{:.fragment}
<aside>
Based on this example, describe what a program is. &rarr;
</aside>
{:.fragment}
<p>One simple description might be: a set of instructions that tell the computer to do things.</p>
{:.fragment}
</div>
</section>

<section markdown="block">
##  A Formal Definition
__program__ - a sequence of instructions that specifies to a computer actions and computations to be performed
</section>

<section markdown="block">
##  This Course is About _Programming_, not Just Programs
<aside>So... what's programming?</aside>
</section>

<section markdown="block">
##  Programming

* writing a program (of course!)
* all of the ancillary processes involved in writing that program
	* designing / planning / requirements
	* testing
	* debugging
	* refactoring (changing code) 
</section>

<section markdown="block">
##  Programming Can Be:
* Engineering (software engineering)
	* Precise and exacting
	* Provable and formally verifiable
* A craft  (creative coding)
	* Creative and iterative process
	* Expertise built through experience
* A science (computer science)
	* The study of information processing and computation 
	* Related to mathematics and philsophy
</section>

<section markdown="block">
##  But It's Really Just Problem Solving
<aside>Taking a step back, we write programs to scratch an itch</aside>
</section>

<section markdown="block">
##  Why Would You Want to Learn How to Program?
<aside>
Some motivation...
</aside>
* I'm going to be the next [Sid Meier](http://en.wikipedia.org/wiki/Sid_Meier), [Ada Lovelace](http://en.wikipedia.org/wiki/Ada_Lovelace#First_computer_program), or [Mark Zuckerberg](http://en.wikipedia.org/wiki/Mark_Zuckerberg)!
* (Speaking of Ada Lovelace, [this is a computer!](https://upload.wikimedia.org/wikipedia/commons/a/ac/AnalyticalMachine_Babbage_London.jpg))
* I'm obsessive about my [spreadsheets](http://globalgeeknews.com/wp-content/uploads/2011/04/Spreadsheet-Batman.jpg); I need to get that formula/conditional formatting to work! 
* Statistics is hard; I need to learn some [R](http://en.wikipedia.org/wiki/R_(programming_language))!
* Physics is hard; I need to learn some [MATLAB](http://en.wikipedia.org/wiki/MATLAB)!

<details open markdown="block">
* QUESTION - anyone know sid meier or ada lovelace
* DEMO - wiki articles
* DEMO - R?
</details>
</section>

<section markdown="block">
##  Why Else?
<aside>
Some more motivation...
</aside>
* I'm managing a bunch of nerdy programmers; we need to figure out how to talk to each other.
* Technology is the art medium of the future; I'm going to be the next [Cory](http://www.coryarcangel.com/things-i-made/2002-001-super-mario-clouds) [Arcangel](http://en.wikipedia.org/wiki/Cory_Arcangel)!
* I want to make [MineCraft](http://www.minecraft.net/), like [Notch](http://en.wikipedia.org/wiki/Notch_(game_designer)), or at least make [minecraft in minecraft](http://www.youtube.com/watch?v=GwHBaSySHmo) 
* __It's fun!__ (seriously, it is!)

<details open markdown="block">
* QUESTION - anyone know cory arcangel or minecraft?
* DEMO - art
* DEMO - wiki article
* DEMO - video?
</details>
</section>

<section markdown="block">
##  Great, I'm convinced!  __Sign me up!__
<aside>
But before we get too much into programs ...
</aside>
</section>
