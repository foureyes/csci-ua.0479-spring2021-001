---
layout: slides
title: Formatting
---

<section markdown="block" class="title-slide">
#  Formatting Output
{% include title-slide-footer.html %}
</section>


<section markdown="block">
###  Formatting With Print (Review) 

__How can we format output with print (that is, control what gets printed out between separate arguments, and what gets printed out after the actual value)?__ &rarr;

<div class="incremental" markdown="block">
We can use special arguments, called __keyword arguments__, to control output with print. <code>sep="separator"</code> and <code>end="ending"</code>. 
</div>

__Let's check out some examples in the next slide.__ &rarr;
</section>

<section markdown="block">
###  Formatting With Print Examples

* note that there are __no quotes__ around <code>sep</code> and <code>end</code>
* these __keyword arguments__ go __after regular arguments__

{% highlight python %}
// instead of using space to separate arguments, use comma!
print("foo", "bar", "baz", sep=", ")

// use a + instead of a newline at the end!
print("foo", "bar", "baz", end="+")

// you can combine both sep and end
print("foo", "bar", "baz", sep=", ", end="+")
{% endhighlight %}
</section>


<section markdown="block">
###  The format() Function

The __format()__ function can be used to format a value __before you use it elsewhere__ (for example, before you print out to the user)

* it takes two arguments 
	* the thing (value) you want formatted (can be a string or numeric type)
	* some formatting pattern (expressed as a string)
* format() always __returns a string__ 
* the original value is not modified in any way!
</section>

<section markdown="block">
###  Padding Strings

You can use format to ensure that you string has some number of characters in it. 

* to fill out the remaining characters, format will add spaces before or after your original string
* this is specified by the format string
* for example, <code>'>20s'</code> and  <code>'<20s'</code> add spaces to the beginning and end of a string...

{% highlight python %}
formatted = format('hello', '>20s')
print(formatted)
{% endhighlight %}

</section>

<section markdown="block">
###   Examples of Formatting Floats

Specifying places after decimal (. means decimal, number is the number of spaces, f means floating point format)

{% highlight python %}
a = 1.333333
b = format (a, '.2f') # format as a float, 1.33
c = format (a, '.3f') # format as a float, 1.333
d = format (a, ',.5f') # add a comma separator
e = format (a, '>20,.2f') # pad it too!
{% endhighlight %}

</section>

<section markdown="block">
###   Examples of Formatting Integers

Specifying places after decimal (, means add comma, d means integer)

{% highlight python %}
a = 20000
print(format(a, ',d'))
print(format(a, '>20,d'))
{% endhighlight %}
</section>

<section markdown="block">
###  The Formal Specification

Ok... so if you want to know how __format__ really works:

* the second argument is a string that represents a format
* and it's written in a "mini-language" (yes, a language in a language!)

{% highlight python %}
format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
fill        ::=  <any character>
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | 
                 "G" | "n" | "o" | "s" | "x" | "X" | "%"
{% endhighlight %}

(taken from [the official documentation](https://docs.python.org/3.6/library/string.html#formatspec))

</section>

<section markdown="block">
##  Additional Notes

__There are a few other minor details with format__ &rarr;

* you can leave out the type of you're not doing any specific formatting based on that type
    * `format(1.2)`
* if you use a type with an incompatible value, you'll get an error
    * `format(1.2, 's')`
* notice the other possible items that you can add to the format specifier? 
    * you can try adding things like `fill`, `sign`, etc.

</section>

<section markdown="block">
##  Let's Try This...

__What format string should we use to format the number 1000.32 so that it gives back a stirng composed of 20 characters:__ &rarr;

<div class="incremental" markdown="block">
`'---------1,000.32000'`
</div>

<div class="incremental" markdown="block">
`format(1000.32, '->20,.5f')`
</div>

</section>
