---
layout: slides
title: About Class #23 
---
<section markdown="block" class="title-slide">
#  About Class #23
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Topics 

* file i/o
* exceptions
* taking more cs courses? 

</section>

<section markdown="block">
###  Grades

* midterm #2 grades by end-of-week
* grades for homework #6 and #7 to be posted by weekend
</section>

<section markdown="block">
###  Tutoring

No tutoring during Thanksgiving break
</section>

{% comment %}
<section markdown="block">
###  Homework #8 Part 1

<aside>And speaking of homework...</aside>

* [get first word](../../homework/hw08/get_first_word.py)
	* check for space first
		* use conditional to check for -1
		* if it's not -1 (or greater than), you can use as end index of slice
	* alternatively, split would work (and return first element of resulting list)!
		* watch out for empty string
* [palindrome](../../homework/hw08/is_palindrome.py)
	* slices to reverse (3rd part of slice as step)
	* or continually add to beginning
</section>

<section markdown="block">
###  Homework #8 Part 2

* [pig latin](../../homework/hw08/pig_latin.py)
	* startswith prefix instead of slicing for comparisons
* [translate passage](../../homework/hw08/translate_passage.py)
	* expected use of pig_latin function
</section>


<section markdown="block">
###  Exercises / Additional Resources

* [Learn Python the Hard Way](http://learnpythonthehardway.org/book/)
* [Codecademy](http://www.codecademy.com/tracks/python)
* [Coding Bat](http://codingbat.com/python)
* [Khan Academy](http://www.khanacademy.org/cs) (JavaScript, though)
</section>
{% endcomment %}


<!--
<section markdown="block">
###  join and split

__What type/object are join and split called on?__ &rarr;

<div class="incremental" markdown="block">
* they are called on string objects (!?).
* a questions was asked about the rationale behind this design decision
* turns out, [any _iterable_ type will work, and the string is constant](http://lucumr.pocoo.org/2011/7/9/python-and-pola/#seemingly-inverse-logic)
* [another answer on stack overflow](http://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring)
</div>
</section>
-->
