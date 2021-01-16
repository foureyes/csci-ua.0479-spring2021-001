---
layout: slides
title: Programming Languages
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  First Let's Talk About Natural Languages
<aside>
What are some characteristics of natural languages? &rarr;
</aside>
<div class="fragment" markdown="block">
* meant for communication between people (usually!)
* these are the languages that people speak ([English, Urdu, Catalan, etc.](http://en.wikipedia.org/wiki/List_of_languages_by_name))
* not intentionally designed - evolved naturally / organically
* usually verbose
* room for ambiguity, interpretation, etc.
</div>
<details open markdown="block">
* QUESTION - (header) What are some characteristics of natural languages?
* DEMO - list of languages
</details>
</section>

<section markdown="block">
##  A Programming Language...
<aside>
On the other hand? &rarr;
</aside>
<div class="fragment" markdown="block">
* is artificial / synthetic
* is created specifically to communicate __instructions__ to a machine 
* usually has a rigid structure or grammar 
* is usually very strict about __syntax__
* some words / symbols have special meanings
* is usually exact / explicit in its meaning
* information dense; each character counts!
* provides a layer of __abstraction__ between programmer and machine
</div>
<details open markdown="block">
QUESTION - (header) What are some characteristics of programming languages?
</details>
</section>

<section markdown="block">
##  This Makes Reading and Writing Programs Much Different From Natural Languages
</section>

<section markdown="block">
##  Reading a Programming Language
* reading a program requires analysis of a program's __structure__ 
* information density can make comprehension a slow process
* again, meaning is usually unambiguous 
	* behavior / meaning usually backed by formal specifications
	* though language is unambiguous, programmer intent may not be!
</section>

<section markdown="block">
##  Writing a Program
* easy to introduce minor syntactic errors (you must be careful with syntax and grammar)
* may have multiple implementation possibilities
* may offer constructs for abstraction and preventing repetition
	* potentially further improves on human readability
	* important for refactoring, improving your program, and future maintenance
* don't necessarily have to know entire language to write a program!
</section>

<section markdown="block">
##  Sooo Many Programming Languages...
<aside>(You could even make one yourself!)</aside>
</section>

<section markdown="block">
##  These Are 20 of the Most Used Languages Today
<aside markdown="block">
(At least, according to [TIOBE](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html), September 2017)
</aside>
<div style='text-align:center;'>
<table style='text-align:left;margin:auto;'>
<tr>
	<td width="33%">
		<ol>
		<li>Java</li>
		<li>C</li>
		<li>C++</li>
		<li>C#</li>
		<li><strong>Python</strong></li>
		<li>PHP</li>
		</ol>
	</td>
	<td width="33%">
		<ol start="7">
		<li>JavaScript</li>
		<li>Visual Basic .NET</li>
		<li>Perl</li>
		<li>Ruby</li>
		<li>R</li>
		<li>Delphi</li>
		<li>Swift</li>
		</ol>
	</td>
	<td width="34%">
		<ol start="14">
		<li>Assembly</li>
		<li>MATLAB</li>
		<li>Go</li>
		<li>Objective C</li>
		<li>PL/SQL</li>
		<li>Scratch</li>
		</ol>
	</td>
</tr>
</table>
</div>
<details open markdown="block">
* DEMO - click through to TIOBE
* INFO - don't know details, but uses search engine results
* INFO - note that is no indication of what's the _best_ languages to use; that's up to you!
</details>
</section>

<section markdown="block">
##  That's a Lot!
<aside>Why so Many?</aside>
<div markdown="block" class="fragment">
* endless number of potential applications (right tool for the job)
* personal preference! (what works best for you)
* multiple platforms (web, mobile, operating systems, processors, etc.)
</div>
<details open markdown="block">
QUESTION - (header) why so many?
</details>
</section>

<section markdown="block">
##  Here Are Some Ways That We Can Describe Programming Languages
<aside>This will motivate the tools that we'll use in this class</aside>

<details open markdown="block">
INFO - a lot of material, some not in readings... but most important parts are reinforced in readings, of course
</details>
</section>

<section markdown="block">
##  Some Characteristics of Programming Languages Include:
1. high-level and low-level
2. interpreted and compiled
3. by _paradigm_
4. esoteric and mainstream
</section>

<section markdown="block">
<h1> High-Level <br /> and Low-Level <br />Languages</h1>
<aside>Some languages are friendlier than others</aside>
</section>

<section markdown="block">
##  Low-Level Language
A __programming language__ designed for execution by a computer. (Not so friendly.)

* loosely speaking, __a computer can only directly execute programs written in low level languages__
* generally makes no attempt to hide the machinery that it _instructs_
* usually _fast_ and _resource efficient_
* some examples include:
	* __machine code__ - as close as you can get to the machine
	* __assembly language__ - just a step above machine code
</section>

<section markdown="block">
##  Low-Level Languages Look Like:
<aside>Don't worry, we won't be using them in this class!</aside>

__Assembly__
<pre><code data-trim contenteditable>
MOV AL, 1h        ; Load AL with immediate value 1
MOV CL, 2h        ; Load CL with immediate value 2
MOV DL, 3h        ; Load DL with immediate value 3
</code></pre>

__Machine Code__
<pre><code data-trim contenteditable>
10110000 01100001
</code></pre>
</section>

<section markdown="block">
##  High-Level Language
A __programming language__ that is designed to be easy for humans to read and write.

* must be __compiled__ or __interpreted__ to a lower-level language so that a computer can execute it
* provides abstractions that free the programmer from dealing with the details of the underlying machine
* meant for the programmer rather than the computer
* usually prioritizes usability over efficiency
* more likely to be _correct_
* _portable_ across different operating systems/architectures
</section>
<section markdown="block">
##  Examples of Some High-Level Languages:
<aside>BTW, what do you think these examples do?</aside>
__Ruby__

<pre><code data-trim contenteditable>
100.times do |i|
	puts i if i % 2 == 0
end
</code></pre>
__PHP__

<pre><code data-trim contenteditable>
$count = 0;
while($count < 100) {
	print($count);
	$count = $count + 2;
}
</code></pre>

<details open markdown="block">
* QUESTION - (header) what do these examples do?
* DEMO - run the program
</details>
</section>

<section markdown="block">
##  High-Level vs Low-Level
* high level 
	* more human readable, but also usually more verbose
	* some are closer to natural languages
	* usually abstracts away intricacies of dealing with underlying machine / computer
	* loosely speaking, meant for programmers
* low level
	* usually terse / less verbose
	* usually does not look like a natural language
	* need some knowledge of underlying machine / computer
	* loosely speaking, meant for machines
</section>

<section markdown="block">
##  Compiled and Interpreted 
<aside>If computers only know how to execute low-level programs, how do high-level programming languages <em>work</em>?</aside>
</section>

<section markdown="block">
##  Two Ways to Execute a Program
Before a program can be executed, the source code of a high-level language must be translated into something that the computer can understand.  You can:

* __compile__ the __source code__ into another (usually  __low-level__) language using a __compiler__... then execute 
* execute the __source code__ immediately using an __interpeter__ 
</section>

<section markdown="block">
##  Compiling a Program
* when we talk about __source code__ (or just __code__), we're referring to the program prior to compilation
* programs called __compilers__ perform this translation
* a compiler __parses__ your source code in order to do this translation
	* __parse__ - to examine a program and analyze the syntactic structure
	* we do this for natural languages too!
* the result of this translation is usually referred to as __object code__
* the __object code__ is what is run by the computer
</section>

<section markdown="block">
##  Compiling a Program... Continued
__General Workflow__

1. Write code
2. Compile
3. Execute program
4. Go back to step #1

__Examples of Compiled Languages__

* Basic
* C/C++
* Java (there are some subtleties here that we'll talk about later)
</section>

<section markdown="block">
##  Interpreting a Program
* a program can be executed using an __interpeter__
* an __intpreter__ is a program that executes source code without the need for compilation
	* the way that a program is executed behind the scenes varies by language and implementation
	* perhaps compilation is done behind the scenes
	* ...or the interpreter acts as a _virtual machine_ where the codes _just runs_
* Sometimes an __interpeter__ may also allow a program to be run interactively
	* also called an __interactive shell__ or an __interactive console__

<details open markdown="block">

* DEMO - python interactive shell
* DEMO - irb

</details>
</section>

<section markdown="block">
##  Interpreting a Program... Continued
__General Workflow__

1. Write code
2. Execute program
3. Go back to step #1

__Examples of Interpreted Languages__

* Ruby
* PHP
* Lisp
</section>

<section markdown="block">
##  Compiled vs Interpreted
<aside>Some stereotypes...</aside>
* compiled languages are usually considered faster and more efficient than interpreted languages
* interpreted languages are generally thought of as easier to use (less steps, immediate feedback, etc.)
</section>

<section markdown="block">
##  And What Does This Mean for Us?
Despite the pros and cons of compiled and interpreted languages, for our purposes, the _main_ difference between a __compiled__ and __interpreted__ language is:

* a __compiled language__ requires an explicit compilation step
before the program can be run. 
* an __interpreted language__ can be run immediately
</section>

<section markdown="block">
##  Some Important Caveats
* distinction is wholly dependent on implementation, not language design
* a programming language may be considered compiled, interpreted or even both!
* hybrids exist (to further complicate things!)
	* a language may be __compiled__ to an intermediary form 
		* this form may be run by an __interpeter__!
		* still considered __compiled__ because of explicit compilation step
	* a language may be __compiled__ to an intermediary form that's run immediately by the __interpreter__
</section>



<section markdown="block">
##  Programming Paradigms  

<aside markdown="block">
Think: _programming style_
</aside>
</section>

<section markdown="block">
##  Some Programming Paradigms  
<aside>This is how we approach a programming problem</aside>
* [Procedural](http://en.wikipedia.org/wiki/Procedural_programming)
* [Imperative](http://en.wikipedia.org/wiki/Imperative_programming)
* [Object Oriented](http://en.wikipedia.org/wiki/Object-oriented_programming)
* [Functional](http://en.wikipedia.org/wiki/Functional_programming)
* [Aspect Oriented](http://en.wikipedia.org/wiki/Aspect-oriented_programming)
* [Declarative](http://en.wikipedia.org/wiki/Declarative_programming)
* and more...
</section>

<section markdown="block">
##  For This Class...
We'll mostly be concerned with __imperative__ and __procedural__ programming. (So don't worry about the others).

* this approach most closely resembles our definition of what a program is
* solves a problem through a sequence of commands
* these commands (or statements) can change the program's state (data)

The tools that we use may include bits of __object oriented__ programming.
</section>

<section markdown="block">
##  And, Lastly... Is it Practical?
<aside markdown="block">
Esoteric and mainstream languages
</aside>
</section>
<section markdown="block">
##  Esoteric vs Mainstream
* mainstream
	* widely adopted
	* may adopt features found in __esoteric languages__
* esoteric
	* experimental - not necessarily meant for practical use
	* may serve as a proof of concept
	* recreational - a thought exercise, or even a joke!
	* examples - [Piet](http://www.dangermouse.net/esoteric/piet/samples.html), [LOLCODE](http://en.wikipedia.org/wiki/LOLCODE#Example_3), and [Befunge](http://en.wikipedia.org/wiki/Befunge#Sample_Befunge-93_code)

<details open markdown="block">
* DEMO - Piet
* DEMO - LOLCODE
</details>
</section>
<section markdown="block">
##  [Let's Use Python](tools.html)
<aside markdown="block">
It's a friendly high-level interpreted\* language that supports multiple programming paradigms.
</aside>
</section>
