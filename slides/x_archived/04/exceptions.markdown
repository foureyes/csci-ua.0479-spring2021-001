---
layout: slides
title: "Exception Handling"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## I've Made a Huge Mistake

__What are some broad categories of errors that can occur in Python program?__ &rarr;

1. {:.fragment} __syntax__ (yup, pretty common... missed a closing double quote; program _doesn't even run_)
2. {:.fragment} __ruuuuntiiiiiime__ (program runs, but crashes)
3. {:.fragment} __logic__ (program runs totally fine, but it doesn't meet requirements / specifications)

</section>

<section markdown="block">
## Exceptions

__Exceptions__ are runtime errors.

* we can _gracefully_ recover from exceptions
* ...but if we don't do anything with them, our program crashes

__What are some exceptions we've seen?__ &rarr;

* {:.fragment} <code>NameError</code>: <code>a + 5 # a doesn't even exist yet!</code>
* {:.fragment} <code>TypeError</code>: <code>'a' + 5 # string + int? nope!</code>
* {:.fragment} <code>ZeroDivisionError</code>: <code>5 / 0</code>
* {:.fragment} <code>IndexError</code>: <code>'oops'[99]</code>
* {:.fragment} <code>KeyError</code>: <code>{'a': 5}['some_key']</code>
* {:.fragment} <code>ValueError</code>: <code>int("five") # strings are ok, so not type error</code>

</section>

<section markdown="block">
## Tell Me More About Gracefully

We can use __try__, __except__ to _do deal with runtime errors_. 

<pre><code data-trim contenteditable>
try:
    # tricky stuff
except:
    # recover
finally:
    # optional
</code></pre>

* we attempt to execute _error prone_ code in the <code>try</code> block
* if there's an error, we execute the code in the <code>catch</code> block
* otherwise, skip the <code>catch</code> block and continue program execution
* everything in the <code>finally</code> block gets executed regardless


</section>

<section markdown="block">
## Many Variations

__The try/except syntax allows for:__ &rarr;

* catching all exceptions
* specifying one or more exceptions to catch
* accessing the exception information

__There are a few different ways that you can specify a try/except... and the next few slides we'll go through them with examples.__ &rarr;

</section>

<section markdown="block">
## No Exception

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
try:
    print("hello")
except:
    print("error!")
print("done")
</code></pre>

<pre><code data-trim contenteditable>
hello
done
</code></pre>
{:.fragment}

No error... so except block is skipped.
{:.fragment}

</section>
<section markdown="block">
## Catch All Exceptions

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
try:
    print(int("hello"))
except:
    print("error!")
print("done")
</code></pre>

<pre><code data-trim contenteditable>
error!
done
</code></pre>
{:.fragment}

An error occurred, so the code in the except block is executed... then the program happily proceeds to the next statement.
{:.fragment}
</section>


<section markdown="block">
## Catch All Exceptions (Again)

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
try:
    print(int("hello"))
except Exception:
    print("error!")
print("done")
</code></pre>

<pre><code data-trim contenteditable>
error!
done
</code></pre>
{:.fragment}

We specify that we'd like to catch all exceptions of type <code>Exception</code> (that is, a generic exception)... this is the same as saying... _just catch any exception_ (think of <code>Exception</code> as the superclass of all other exceptions if you're coming from another object-oriented language).
{:.fragment}
</section>

<section markdown="block">
## Catch a Specific Exception

__What's the output of this code if the user types in 1?__ &rarr;

<pre><code data-trim contenteditable>
planets = ['mercury', 'venus', 'earth']
answer = input('Give me an index\n>')
try:
    i = int(answer)
    print(planets[i])
except IndexError:
    print("That index doesn't exist!")
print("Done!")
</code></pre>

<pre><code data-trim contenteditable>
venus
done
</code></pre>
{:.fragment}

No error... things run along smoothly.
{:.fragment}

</section>

<section markdown="block">
## Catch a Specific Exception Continued

__What's the output of this code if the user types in 987?__ &rarr;

<pre><code data-trim contenteditable>
planets = ['mercury', 'venus', 'earth']
answer = input('Give me an index\n>')
try:
    i = int(answer)
    print(planets[i])
except IndexError:
    print("That index doesn't exist!")
print("Done!")
</code></pre>

<pre><code data-trim contenteditable>
That index doesn't exist!
done
</code></pre>
{:.fragment}

An IndexError occurs, but our except block takes care of it
{:.fragment}
</section>

<section markdown="block">
## Catch a Specific Exception Continued

__What's the output of this code if the user types in 'MILKY WAY!'?__ &rarr;

<pre><code data-trim contenteditable>
planets = ['mercury', 'venus', 'earth']
answer = input('Give me an index\n>')
try:
    i = int(answer)
    print(planets[i])
except IndexError:
    print("That index doesn't exist!")
print("Done!")
</code></pre>

<pre><code data-trim contenteditable>
ValueError ...
Traceback (most recent call last):
    ...
    i = int(answer)
ValueError: invalid literal for int() with base 10: 'MILKY WAY'
</code></pre>
{:.fragment}

A ValueError occurs, but it remains uncaught.... so the program crashes.
{:.fragment}
</section>

<section markdown="block">
## Chaining Except Blocks

We can take different code paths depending on what exception we catch by chaining exceptions. __What's the output of this code if the user types in 'MILKY WAY!'?__ &rarr;

<pre><code data-trim contenteditable>
planets = ['mercury', 'venus', 'earth']
answer = input('Give me an index\n>')
try:
    i = int(answer)
    print(planets[i])
except IndexError:
    print("That index doesn't exist!")
except ValueError:
    print("That's not an integer!")
print("Done!")
</code></pre>

<pre><code data-trim contenteditable>
That's not an integer!
Done!
</code></pre>
{:.fragment}

A ValueError occurs, and it's caught with our second except block
{:.fragment}
</section>

<section markdown="block">
## Multiple Exceptions in a Single Except

A single except block can catch multiple exception types. __What's the output of this code if the user types in either 987 or MILKY WAY?__ &rarr;

<pre><code data-trim contenteditable>
planets = ['mercury', 'venus', 'earth']
answer = input('Give me an index\n>')
try:
    i = int(answer)
    print(planets[i])
except (IndexError, ValueError):
    print("Uh oh!")
print("Done!")
</code></pre>

<pre><code data-trim contenteditable>
Uh oh!
Done!
</code></pre>
{:.fragment}

Both a ValueError and an IndexError is caught by the same <code>except</code> block
{:.fragment}
</section>

<section markdown="block">
## Accessing an Exception Object

If an exception occurs, that exception is represented by an object. __You can access that object by naming it using <code>as</code> on the same line as <code>except:</code>__ &rarr;

<pre><code data-trim contenteditable>
planets = ['mercury', 'venus', 'earth']
answer = input('Give me an index\n>')
try:
    i = int(answer)
    print(planets[i])
except IndexError as e:
    print(e)
</code></pre>

In this case, if an <code>IndexError</code> occurs, it can be examined by using the variable name, <code>e</code>. __If the user types in 987, the resulting output woudl be the string reprsentation of the exception:__ &rarr;

<pre><code data-trim contenteditable>
list index out of range 
</code></pre>
</section>

<section markdown="block">
## Finally

You can use the <code>finally</code> clause to execute code regardless of whether or not an exception occurs.

<pre><code data-trim contenteditable>
planets = ['mercury', 'venus', 'earth']
answer = input('Give me an index\n>')
try:
    i = int(answer)
    print(planets[i])
except Exception:
    print("An error occurred")
finally:
    print("I'm always executed")
</code></pre>

<code>I'm always executed</code> is always printed out, regardless of what the user types in.
</section>
