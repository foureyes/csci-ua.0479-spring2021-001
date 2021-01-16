---
layout: slides
title: "Composition, Inheritance, More About Classes"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section> 
{% comment %}
Topics
=====

contract, abstraction / encapsulation, private variables
-----
* contract - class is an abstraction, hides away underlying necessary but irrelevant details of implementation so you can focus on problem you're trying to solve
* we can create data types uses classes
    * usage based on what class "exposes"
    * details can be changed if _public_ interface remains the same
* private variables / methods
    * use leading underscore for convention (signal to class user that they should not use this) 
    * but not an error if you access these!
* example 1: create class called queue
    * queues are essentially lines...
        * usually first in, first out (first in line, first served)
            * fifo...
        * though there can be different _queueing policies_, in line for exams - alphabetical order by last name, or a todolist where high priorit items are done first
            * priority queue
    * queue method
    * dequeue dequeue
    * queue __str__
    * use in program
    * doesn't matter how it's implemented as long as first in is first out
        * append to queue and remove 0 to dequeue
        * insert before pop to dequeue
    * change implementation, prog still works

id() method, __class__, dispatching
-----
* integer guaranteed to be unique and constant for object during its lifetime
* in the implementation of python (CPython) you're using, it's probably the memory location
* id of two different objects
* create two lines

Static Revisited
-----
* saw static method
    * using decorator @staticmethod
    * can call with instance or with class name
    * without... leave out self, can only call with class name
* static variable
    * defined without self in class
* example 1: 
    * SolarSystem, GRAVITY = 9.8
* example 2:
    * counting planets

Composition
-----
* has-a relationship (there's also aggregation, but we can skip that)
* object _contains_ another object
* example 1: RecordingArtist may have Albums?
    * name
    * album title
    * album year
    * record label
* example 2: quiz and multiple choice question
    * quiz has a / many multiple choice questions
    * see solution

Duck Typing
-----
* typically we say type dictates operations and functions
    * not entirely true
    * as long as something _behaves_ like the thing we want to use
* example 2: class Duck
    * class NotADuck
    * use both instances to quack
* example 2: get_first_and_last_line
    * implement file like obj by implementing some methods that a file would have
    * get_first_and_last_line() --> tuple of first and last 
    * lines = f.readlines()
        * return lines[0], lines

Inheritance
-----
* if we want properties and methods of one class to based off another
* everything by default inherits from object
* inherit from object always! (for Python 2)
* example 1: door, locked door
* example 2: the 'ol Person / Student trick
* example 3: extending Exception

Polymorphism
-----
* objects of different type behave the same... 
* can be done with inheritance or with ducktyping
* example 1: dog / wolf, barkforme?
    * http://stackoverflow.com/questions/2835793/how-does-polymorphism-work-in-python
* example 2: file io
* different from java

Super, calling Super methods with self
-----
* super().methodname(args)
* works with constructor, __str__, etc.
* super().__init__(args)

Multiple Inheritance
-----
* diamond problem
* person -> teacher , student -> grad student?
    * who's do_stuff_at_night?
    * who's __str__
* TODO ... how does Python do it?

Inheritance vs Composition
-----
* two different techniques to describe two different relationships
    * a Rectangle is a Polygon
    * a Polygon has a (multiple) Point
* sometimes you can use either, though!
* see [online reading](http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-1-objects-and-types/#.Vws3NBMrKRs)
* example 2: door
    * color is static
    * but locked is not
    * create two doors

Private Variables, Name Mangling Again
-----
* name mangling
* from the docs "Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped"

More magic variables ()
-----
* \_\_dict\_\_
* \_\_getattr\_\_

Example using Pig game?
-----
* functional version
* object oriented version? 
{% endcomment %}
