---
layout: slides
title: Review 
---

<section markdown="block" class="title-slide">
#  Values, Types, Variables Review 
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  Previously on ...

<aside markdown="block">
[This handout](../../resources/handouts/class03/types-variables-operators-comments.pdf) covers material from our last class (function calls, types, values, input, operators and variables).
</aside>
</section>

<section markdown="block">
###  Values

__What's a value? &rarr;__

<div class="incremental" markdown="block">
A value is just data!

1. it can be stored in a variable 
2. it can be used an an expression
3. it can't be _evaluated_ further (2 + 3 is not a value; it can be evaluated further)
</div>
</section>

<section markdown="block">
###  Types

__What's a type? &rarr;__

<div class="incremental" markdown="block">

A type is just a kind or category of values.  __Name the types that we learned about. &rarr;__

1. str (string)
2. int (integer)
3. float (floating point number)
4. complex
</div>
</section>

<section markdown="block">
###  Basic Data Types - Strings

__str__ - strings

__What's a string? How do we know a literal value is a string? &rarr;__

<div class="incremental" markdown="block">
* ordered sequence of characters
* examples: 'string', "string", """string""
* escape special characters using backslash or alternate delimiter
</div>
</section>

<section markdown="block">
###  String Operators

__Name two operators that can be used with strings__ &rarr;

* describe what they do
* name the types of operands that they work with

<div class="incremental" markdown="block">
* __+__ - concatenation (addition) 
	* joins strings together
	* both operands must be strings
* __\*__ - multiplication or repetition
	* repeats a string
	* one operand must be a string, the other, an int
</div>
</section>

<section markdown="block">
###  String Operators Continued

__What do the following lines of code output (error is a possible answer)?__ &rarr;

{% highlight python %}
print("three" + " blind" + " mice")
print(3 + " strikes")
print(3 * "ring ")
print("hey" * "three")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
three blind mice

TypeError: unsupported operand type(s) for +: 'int' and 'str'

ring ring ring

TypeError: can't multiply sequence by non-int of type 'str'
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Basic Data Types - Integers

__int__ - integers

__What's an int? &rarr;__

<div class="incremental" markdown="block">
* whole number - negative or positive
* examples: 1751, -95
* "unlimited"
</div>
</section>

<section markdown="block">
###  Basic Data Types - Floating Point Numbers

__float__  - floating point numbers

__What's a float? How do we know a literal value is a float? &rarr;__

<div class="incremental" markdown="block">
* real number - contains decimal point
* 10.00, 491.545532111
* may overflow
* small and large numbers expressed in scientific notation
</div>
</section>

<section markdown="block">
###  Operators for Numeric Types

__Name 7 operators that can be used on floats and/or ints. &rarr;__

<div class="incremental" markdown="block">
1. addition: __+__
2. multiplication: __\*__
3. subtraction: __-__
4. division: __/__ (results in a float even if two integers - ex 10 / 2 &rarr; 5.0)
5. integer division: __//__ (closest integer to the left - ex -23 // 3 &rarr; -8)
6. modulo: __%__ (ex 10 % 7 &rarr; 3)
7. exponentiation: __**__ (ex 2 ** 3 &rarr; 8)
</div>
</section>

<section markdown="block">
###  Operators for Numeric Types Continued

__The following block of code will cause a run time error.  Why?__ &rarr;

{% highlight python %}
a = "20"
print(a + 5)
{% endhighlight %}

<div class="incremental" markdown="block">
A Type Error will occur... the operator, plus, doesn't support int and str.  __What can be done to fix this?__ &rarr;

One fix is to convert the variable, __a__, into an integer using the __int__ function:

{% highlight python %}
a = "20"
print(int(a) + 5)
{% endhighlight %}

</div>
</section>

<section markdown="block">
###  Type Conversions

__Name three functions that can be used to convert a value from one type to another.__ &rarr;

<div class="incremental" markdown="block">
1. int
2. float
3. str
</div>

</section>

<section markdown="block">
###  Type Conversions: a Closer Look 

The following functions will attempt to convert the parameter(s) passed in into the type that the function is named after:

* int 
	* converts "int like" parameters to ints
	* int("54") &rarr; 54
	* int("   54   ") &rarr; 54
	* int(54.2) &rarr; 54
	* int("54.0") &rarr; results in ValueError
	* int("54.2") &rarr; results in ValueError

</section>

<section markdown="block">
###  Type Conversions Continued

* float
	* float("54.2") &rarr; 54.2
	* float(54)	&rarr; 54.0
* str
	* str(54) &rarr; "54"
	* str(54.0) &rarr; "54.0"

</section>

<section markdown="block">
###  Variables

Variables allow us to bind names to values so that the variable name can be used in place of the literal value.  __In code, how would we assign the value 12 to a variable called n?__ &rarr;

<div class="incremental" markdown="block">

{% highlight python %}
n = 12
{% endhighlight %}

* use the assignment operator (just one equals sign): __=__
* name to the left, value to the right

</div>
</section>

<section markdown="block">
###  Valid Variable Names
* names can only be alphanumeric (numbers and letters) and/or the underscore
* the first character has to be a letter (uppercase or lowercase) __or an underscore__
* however, names are __case sensitive__ - case matters
* can't be a keyword or reserved word
{% highlight python %}
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return 
def       for       lambda    try
{% endhighlight %}
</section>


<section markdown="block">
##  [And on to Built-In Functions...](function-calls.html)
</section>
