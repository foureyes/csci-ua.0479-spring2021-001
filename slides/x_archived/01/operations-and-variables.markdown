---
layout: slides
title: Operations and Variables 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##    Operations on Strings and Numeric Types
</section>

<section markdown="block">
##   int operations 
<aside>The Usual...</aside>

As you'd expect: addition, subtraction and multiplication &rarr;

* add - __+__ 
* subtract - __-__
* multiply __\*__
</section>

<section markdown="block">
##   Division is Special

* the division operator is __/__
* __what do you think 5/2 gives__ &rarr;			
* __what type is the result?__ &rarr;

<pre><code data-trim contenteditable>
&gt;&gt;&gt; 5/2
2.5
&gt;&gt;&gt; type(5/2)
&lt;class 'float'&gt;
&gt;&gt;&gt; 
</code></pre>
{:.fragment}

* __note that even if numbers divide evenly, you still get back a float__: &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
>>> 12/4
3.0
>>> type(12/4)
<class 'float'>
>>> 
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##   We Don't Need No Decimal Points
<aside>Integer Division</aside>

* the __integer division__ operator is __//__ (double forward slash)
* it will always give back an integer: 21//10 &rarr; 2
* if the result is a float, it will go to the nearest integer to the left on the number line (or... more simply put, just round down)!
* __what will 5//2 give back?__
* __what will -5//2 give back?__

<pre><code data-trim contenteditable>
>>> 5//2
2
>>> -5//2
-3
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##   Modulo Operator (Remainder)
<aside>What's Left Over?</aside>
* the remainder operator is % (the percent symbol)
* __what would 5%2 give back?__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
>>> 5%2
1
</code></pre>
</div>
</section>

<section markdown="block">
##   Exponentiation 
<aside>We NEED MORE STARS</aside>
* the exponentiation operator is __\*\*__ (two asterisks)
* __what do we get for 2**2__? &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
>>> 2**2
4
</code></pre>
</div>
</section>

<section markdown="block">
##   Order of Operations
<aside>Too Many Operators!  What To Do First?</aside>

* as you would expect (remember PEMDAS?)
* __what does 12 + 10 / 5  give?__ &rarr;

<pre><code data-trim contenteditable>
>>> 12 + 10 / 5
14.0
</code></pre>
{:.fragment}

__BTW, what type did we get back?__
{:.fragment}

float! (division, even with integers, gives back floats)
{:.fragment}
</section>


<section markdown="block">
##   (Parentheses)
<aside>(I Use Them A Lot)</aside>
* you can use parentheses to group expressions...
* this will affect odrer of operations
* __what will (6 + 4) * 5 return?__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
>>> (6 + 4) * 5
50
</code></pre>
</div>
</section>

<section markdown="block">
##   You Could Always Use It As a Calculator
<aside>A Quick Activity</aside>

__Translate this formula into Python code__ &rarr;

* take the fraction 9 over 5 and multiply it by 37... then add 32

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
(9 / 5) * 37 + 32
</code></pre>
</div>
</section>

<section markdown="block">
##   str Operations
</section>

<section markdown="block">
##   Multiplication!?
* the multiplication operator is __*__
* it returns a new string with the original string duplicated the number of times specified by the operand on the right side
* __what would "hey" * 3 return?__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
>>> "hey" * 3
'heyheyhey'
</code></pre>
</div>
</section>

<section markdown="block">
##   String Concatenation
* use the __+__ to stitch together strings
* it's basically just adding strings together
* example: print("knocked " + "my" + "socks" + "off") &rarr;
* why are the words all smashed together? 
* how would we fix it? 
* __let's try different types! - does it work?__ &rarr;
	* with an int? try: 3 + " blind mice" &rarr;
	* with a float?
	* what kind of error are we getting?

<div class="fragment" markdown="block">

* string concatenation only works __when both operands are strings__

</div>

</section>

<section markdown="block">
##   Let's repeat: string concatenation requires both operands to be strings

<aside>Otherwise you get an error!</aside>
</section>

<section markdown="block">
##   Let's Fix It!
<aside>Type Conversion...</aside>

You can change from one type to another using __functions__ of the same name as the __type__ you are trying to convert to.  Let's look at what autocomplete says about the following functions and demo them.  &rarr;

* __int__(), __str__(), and __float__()
* unlike print, these functions __return a value__ to your program!
* this is called __type conversion__ or __casting__
</section>

<section markdown="block">
##  And This Helps... How? 
__Let's fix our previous string concatenation__ &rarr;


<pre><code data-trim contenteditable>
3 + " blind mice"
</code></pre>

(of course, this is contrived, since we know that 3 is an int, and we could have just wrapped it in quotes: '3'... but imagine if we didn't know the type beforehand!)

<div class="fragment" markdown="block">

<pre><code data-trim contenteditable>
>>> str(3) + " blind mice"
'3 blind mice'
</code></pre>
</div>
</section>

<section markdown="block">
##   Review
* what operators do we use for exponentiation and integer division?
* what does -10//3 give back?
* what's an easy way of creating a string that has 100 exclamation points in it? 
* what's string concatenation?
</section>

<section markdown="block">
##   A Quick Summary of Operators for Numeric Types

__Name as many operators that work on numeric types as you can:__ &rarr;

<div class="fragment" markdown="block">
* __+__ - addition
* __-__ - subtraction
* __*__ - multiplication
* __/__ - division (always gives back float)
* __//__ - integer division
* __%__ - modulo (remainder)
* __\*\*__ - exponentiation
</div>
</section>

<section markdown="block">
##   A Quick Summary of String Operators

__Name as many operators that work on strings as you can:__ &rarr;

<div class="fragment" markdown="block">
* __+__ - concatenation (addition), only works when __both operands are strings__
* __*__ - repetition (multiplication), only works when one operand is a __str__ and the other is an __int__
</div>
</section>


<section markdown="block">
##   Variables
</section>

<section markdown="block">
##   What's a Variable?
* __variable__ - name that refers to a value
* this terminology is important; very specific... __name__ and __value__
* we can now use that name instead of the explicit value
* sometimes you'll hear me say the string "literal" - representation of a value within a program... i mean... the thing in quotes
</section>

<section markdown="block">
##   So How Do Variables Actually Work?
<pre><code data-trim contenteditable>
some_variable_name = "a value"
</code></pre>

* this is an __assignment statement__ - binds a value to a name
* the equals sign __assignment token__ - the "operator" that we use to bind a name to a value
	* name on left
	* value on right
	* eeezy.... just like maths
</section>

<section markdown="block">
##   Another Aside - Interactive Shell
Whenever you type something in the interactive shell, it will always return a value. &rarr;

* a value returns a value
* a variable returns a value
* a function can return a value
* if a function doesn't actually return a value, like print, the resulting value will be None (NoneType)
</section>

<section markdown="block">
##   Some More Miscellaneous Comments
* how can I tell if something is printed vs a value is returned?
	* returning a string shows the string in quotes, while printing displays the string without quotes
	* confusing for other types, just know that each line _gives back a value_ to your program, and consequently that value gets shown after each line is entered
* another btw, __metasyntactic variables__: 
	* typical to use nonsense names such as foo, bar, baz as variable names in examples
	* don't use these names, though; use more meaningful names when you write programs!

</section>

<section markdown="block">
##   Variables That Aren't Defined Yet
* __what happens when you use a variable that doesn't exist?__ &rarr;	

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
&gt;&gt;&gt; foo
Traceback (most recent call last):
  File "&lt;pyshell#0&gt;", line 1, in &lt;module&gt;
    foo
NameError: name 'foo' is not defined
&gt;&gt;&gt; 
</code></pre>
</div>
</section>

<section markdown="block">
##   More About Reassignment

* you can reassign or rebind
* __let's see that in action__ &rarr;
<pre><code data-trim contenteditable>
>>> a = 23
>>> a
23
>>> a = "foo"
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##   Naming Variables
* you can make them as long as you want... though I suppose it could crash your computer
	* __what's an easy way to create a long variable name?__ &rarr;
	* __btw, you can autocomplete in the shell by using tab__ &rarr;
* names can only consist of __alphanumeric__ (numbers and letters) characters and the __underscore__
* the __first character__ has to be a __letter or an underscore__
* __case sensitive__ - case matters
* the name can't be a keyword or reserved word
</section>

<section markdown="block">
##   Am I a Valid Name?

__Which of the following are valid variable names in Python?__

1. _foo
2. 1_foo
3. foo
4. 1foo
5. $foo

<div class="fragment" markdown="block">
1 and 3 are valid variable names.
</div>
</section>

<section markdown="block">
##   Let's Actually Use Some Variables

__Try the following on your own:__ &rarr;

* create a variable called __exclaim__, set it eqaul to __"!!!"__ and __print out the variable__
* create 2 variables, __length__ and __width__... 
	* set them both equal __25__ and __8__ respectively
	* multiply both variables and and store the result in a variable called __area__
	* __print out the result__
</section>

<section markdown="block">
##   [User Input](user-input.html)
</section>
