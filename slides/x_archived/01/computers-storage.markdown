---
layout: slides
title: Computers and How They Store Data
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
##  Hardware and Software

__So... um, what's the difference between hardware and software?__ &rarr;

<div class="fragment" markdown="block">
* __hardware__ - the physical device(s) that a computer is made of
* __software__ - the programs that run on a computer
</div>
</section>

<section markdown="block">
##  Hardware

* __hardware__ refers to all of the actual parts that a computer is made of
* computers are composed of several specialized components
* __what do you think the main components of a computer are?__ &rarr;

</section>

<section markdown="block">
##  Major Components of a Computer System

1. __the CPU__ (Central Processing Unit)
2. __main memory__ (also called RAM or Random Access Memory)
3. __secondary storage__ 
4. __input devices__ 
5. __output devices__

</section>

<section markdown="block">
##  The CPU (Central Processing Unit) 

__What does it do?__ &rarr;

<div class="fragment" markdown="block">

* the part of the computer responsible for _actually_ running programs
* modern CPUs are also called __microprocessors__ 
* they're tiny computer chips 

__This may just be for the hardware geeks, but what are some examples of microprocessors?__ &rarr;

* {:.fragment} the Intel Core i3 in your laptop 
* {:.fragment} the Apple A6 in your iPhone or iPad
* {:.fragment} the Atmel chip on an Arduino 
</div>
</section>

<section markdown="block">
##  Main Memory

__What does it do?__ &rarr;

<div class="fragment" markdown="block">

* __main memory or RAM__ (Random Access Memory) is the computer's work area
* it's where the computer stores a running program and the data related to that program
* __RAM__ is _volatile_; it needs continuous power to store data
* consequently, RAM is temporary storage
* when your computer is turned off, the content that's stored in main memory is wiped out
</div>
</section>

<section markdown="block">
##  Secondary Storage

__What does it do?__ &rarr;

<div class="fragment" markdown="block">
* __secondary storage devices__ - devices meant to store data for long periods of time
* unlike __RAM__, these storage devices are _non-volatile_ - they do not require power to retain data

__What are some examples of non-volatile data stores?__ &rarr;

* {:.fragment} your hard drive or SSD
* {:.fragment} CDs, DVDs, etc.
* {:.fragment} __floppy disks__ (!?)

</div>
</section>

<section markdown="block">
##  You Know...

<div class="img-container" markdown="block">

<img style="border:0px" src="http://media.giphy.com/media/B2MvAVY5c1Uv6/giphy.gif">
</div>
</section>

<section markdown="block">
##  Input and Output Devices

These devices allow:

* a user to send data to the computer 
* or allow the computer to present data or feedback to a user

__What are some examples of input and output devices?__ &rarr;

<div class="fragment" markdown="block">
* input - your desktop computer's keyboard and mouse
* input - the camera on your laptop
* input and output - the touch screen on your phone
* output - the speaker on your laptop
</div>
</section>

<section markdown="block">
##  Software

Hardware is nice and all, but...

* a computer by itself is pretty inert
* in order to do anything with it, you'll need some software 
	* that is, you'll need a program or two
	* (or... I guess you can call them _apps_ as well, if you _really_ want to)

</section>

<section markdown="block">
##  Types of Software

* __operating systems__ (and other _system_ software)  
	* the most fundamental set of programs on a computer 
	* allows interaction with the underlying hardware 
* __application software__ 
	* programs that are actually _useful_ for everyday tasks 
* __what are some examples of operating systems and applications__? &rarr;

<div class="fragment" markdown="block">
* operating systems - Windows, Linux, Android, iOS
* applications - Chrome, mail.app, Excel, ProTools, Avid
</div>
</section>

<section markdown="block">
##  Storing Data
</section>

<section markdown="block">
##  It's All 0's and 1's

* computers deal with data as a series of __bits__ or _binary digits_
* a __bit__ (binary digit) can hold only one of two values, a __0__ or __1__
* turns out, storing 0's and 1's is convenient for computers. __why?__ &rarr;

<div class="fragment" markdown="block">
* easily represented by electronics!
* 0 and 1 are essentially analogous to off and on
* (or in actuality the presence or absence of a specific charge or voltage)
</div>
</section>

<section markdown="block">
##  Bits 

__How many pieces of information can be encoded into 1 bit?__ &rarr;

<div class="fragment" markdown="block">
* 2 pieces of information:
	* 0 and 1

__How about 2 sequential bits?__ &rarr;

* 4 (2 x 2) pieces of information (or 4 different combinations of 0's and 1's):
	* 00, 01, 10, 11
</div>
</section>

<section markdown="block">
##  Bytes 

A __byte__ is 8 bits.  __How many possible combinations of 0's and 1's are there in 8 bits?__ &rarr;

<div class="fragment" markdown="block">
* 256 possible combinations (2 x 2 x 2 x 2 x 2 x 2 x 2 x 2)!
* computers can use a __byte__ to encode different kinds of data!
	* numbers
	* letters
</div>
</section>

<section markdown="block">
##  Storing Numbers 

Using a binary numbering system, a computer can store the numbers 0 through 255 in a single _byte_.

* a series of 8 bits represents numbers 0 to 255
* each bit is in a place: _ _ _ _ _ _ _ _
* each place represents the presence or absence of a power of 2:
* summing all of the places gives the decimal version...
* an example: 00101000

<pre><code data-trim contenteditable>

2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0
----+-----+-----+-----+-----+-----+-----+-----
128 | 64  | 32  | 16  |  8  |  4  |  2  |  1 
----+-----+-----+-----+-----+-----+-----+-----
 0  |  0  |  1  |  0  |  1  |  0  |  0  |  0   = 40
----+-----+-----+-----+-----+-----+-----+-----
</code></pre>
</section>

<section markdown="block">
##  Storing Numbers Continued

* the first bit represents either 0 or 1 ...  __1__'s
* the second bit represents either 0 or 1 ...  __2__'s
* the third bit represents either 0 or 1 ... __4__'s
* the fourth bit represents either 0 or 1 ... __8__'s
* .... and so on through the 8th bit, or 2 to the 7th, which represents 128 (notice that each place is just a power of 2, starting at 2 to the 0th power!)
* all of these added together give a number between 0 and 255
* sometimes this is called a base-2 numeral system
* __how does a base-10 numeral system work?__
</section>


<section markdown="block">
##  Storing Numbers - Examples

* __00011100__
	* (0 x 128) + (0 x 64) + (0 x 32) + (1 x 16) + (1 x 8) +  (1 x 4) + (0 x 2) + (0 x 1)
	* &rarr; 28
* __01000010__ 
	* (0 x 128) + (1 x 64) + (0 x 32) + (0 x 16) + (0 x 8) +  (0 x 4) + (1 x 2) + (0 x 1)
	* &rarr; 66
</section>

<section markdown="block">
##  Storing Numbers - Questions

__00000001__ &rarr;

1
{:.fragment}

__00000010__ &rarr;
{:.fragment}

2
{:.fragment}

__00000011__ &rarr;
{:.fragment}
 
3
{:.fragment}

__00000100__ &rarr;
{:.fragment}

4
{:.fragment}

</section>

<section markdown="block">
##  Storing Numbers - Questions Continued

<div class="fragment" markdown="block">
__10000101__ &rarr;

133
{:.fragment}

__10000001__ &rarr;
{:.fragment}

129
{:.fragment}

__00100000__ &rarr;
{:.fragment}

32
{:.fragment}

</div>
</section>

<section markdown="block">
##  An Addendum to Storing Numbers

* note that this works well for integers... 
* specifically 0 through 255
* to work with more numbers, use more bits!
* there are also other encoding schemes
* __what are some other characteristics of numbers that can be encoded?__ &rarr;

<div class="fragment" markdown="block">
* sign (negative or positive numbers)
* decimal point (real / floating point numbers)
</div>

</section>

<section markdown="block">
##  Storing Letters and Other Characters

Storing numbers is a breeze - using bits to represent binary numbers works well.  __How do you think letters and punctuation are stored using bits?__ &rarr;

<div class="fragment" markdown="block">
Since it's easy to store numbers, use some sort of encoding scheme that translates numeric values into characters.  
</div>
</section>

<section markdown="block">
##  ASCII

One encoding scheme is called __ASCII__.

* __ASCII__ defines a set of numeric codes that can be translated to English letters, punctuation marks and other characters
* the first version of __ASCII__ stored characters in 7 bits

__How many different characters can be stored in 7 bits?__ &rarr;

<div class="fragment" markdown="block">
128 characters... [see the table on wikipedia](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters)
</div>

</section>

<section markdown="block">
##  ASCII Continued

ASCII is an older encoding scheme that has some flaws.  __What do you think ASCII's major shortcoming is?__ &rarr;

<div class="fragment" markdown="block">
* it can only store 128 _English_ characters!  
* what about additional alphabets and writing systems?
* (for example Chinese characters number in the tens of thousands)
</div>
</section>

<section markdown="block">
##  Unicode

The current __standard__ for consistently representing text through different character sets and encodings is called __unicode__. 

* in __unicode__, __code points__ are numbers (specifically integers) that represents a _character_ or _glyph_
* the most current version of unicode supports 110,000 characters
* here's a table of [code points](http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec)
	* note that 65-90 are uppercase latin letters; 97-122 are lowercase
	* this matches the older, but limited encoding scheme, ASCII
* here's a [unicode snowman](http://unicodesnowmanforyou.com)
</section>

<section markdown="block">
##  OK... So, How Does a Program Actually Run?

<aside>We already know the physical devices that make up a computer and we know how computers store data.</aside>
</section>

<section markdown="block">
##  How is a Program Executed?

__What part/component of your computer is responsible for executing a program?__

<div class="fragment" markdown="block">
The CPU!
</div>
</section>

<section markdown="block">
##  The CPU Revisited

The CPU can perform some very basic tasks and operations:

* add, subtract, divide and multiply
* read a piece of data from memory
* move data around from one place in memory to another
* ...and others

These operations vary from processor to processor by design.

</section>

<section markdown="block">
##  Machine Language

The CPU executes its operations based on instructions specified by a program.  However, computers really only understand 0's and 1's

* these instructions are written in __machine language__, or __machine code__
* every kind of processor has its own machine code __instruction set__
* __machine code__ instructions are patterns of bits that correspond to different commands/operations on the processor
* for example, 00000101 may mean _subtract one from the data that's in this location_

</section>

<section markdown="block">
##  Don't Panic.  We Won't be Programming in Machine Language!

<aside>What will we be programming in, then?</aside>
</section>


<section markdown="block">
#  [Let's Talk Programming Languages](programming-languages.html)
</section>

