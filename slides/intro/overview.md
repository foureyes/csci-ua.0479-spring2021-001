---
layout: slides
title: Intro
---
<section markdown="block" class="intro-slide">

# {{ site.vars.course_name }}

### {{ site.vars.course_number}}

#### (Hi 👋)
</section>

<section markdown="block">

## What _is_ This?


Special Topics - __{{ site.vars.course_name }}__ 
{:.fragment}

* {:.fragment} (y, very catchy name)

Course Number __{{ site.vars.course_number }}__, Section __{{ site.vars.course_section }}__
{:.fragment}

* {:.fragment} (are you in the right class? 🤷‍)

</section>

<section markdown="block">
## Today!

Here's what we'll be covering today:

__In these slides...__ &rarr;

1. {:.fragment} course topics ✅
2. {:.fragment} introductions 👋
3. {:.fragment} workload 😅

__And then...__ &rarr;
{:.fragment}

1. {:.fragment} _some_ tools 🔨
2. {:.fragment} maybe python stuffs 🐍 if there's time
</section>

<section markdown="block">
## Topics

### U Will Learn Some Stuff, Like...
{:.fragment}


* {:.fragment} finding data 👀
* {:.fragment} cleaning data 🛀
* {:.fragment} "wrangling" data 🤠
* {:.fragment} storing data 🗄

<!--
* {:.fragment} _loving_ and _caring_ for your data as if it were your own tiny toddler child (made of 1's and 0's) ❤️👶💻
  * {:.fragment} (what does that _even_ mean??? idk!) 
-->

</section>


<section markdown="block">
## Topics (Really)

The semester will be broken down into <span class="hl">three parts</span>:

1. {:.fragment} __Using Python to manipulate data__
  * {:.fragment} with Python 3.x, Jupyter notebook/lab, `numpy`, `pandas`, `matplotlib`, `requests`, `requests-html`, etc.
  * {:.fragment} ([{{ site.vars.book1 }}]({{ site.vars.book1_link }}), [{{ site.vars.book3 }}]({{ site.vars.book3_link }}), and [{{ site.vars.book4 }}]({{ site.vars.book4_link }}))
2. {:.fragment} __Designing a data model, storing data in a database, manipulating data in a database__
  * {:.fragment} with PostgreSQL, MongoDB, and Python 3.x as _glue_ sometimes
  * {:.fragment} ([{{ site.vars.book2 }}]({{ site.vars.book2_link }}), [{{ site.vars.book5 }}]({{ site.vars.book5_link }}))
3. {:.fragment} __Visualizing data (on the web this time), deploying _in the cloud_, working with large data sets__
  * exact tech may vary, but stuff like firebase and d3
</section>


<section markdown="block">
## \#goals

Basically ...  you'll be <span class="hl">learning how to use various tools to build end-to-end data pipelines </span>: 

From sourcing data &rarr; to using that data for some _useful_ purpose.
{:.fragment}

* {:.fragment} __ETL__ <span class="fragment">(<strong>E</strong>xtract <strong>T</strong>ransform and <strong>L</strong>oad)</span>
  * {:.fragment} extracting data from single / multiple sources, cleaning and transforming data to a adhere to a particular format, and loading data into persistent storage
* {:.fragment} __+ _something useful_ ...__
  * {:.fragment} visualization on the web 📈🕸
  * {:.fragment} deployment in the cloud ☁️
  * {:.fragment} analysis of large data sets 🗻🗄

</section>

<section markdown="block">
## This is Not...

__This course isn't about...__

* {:.fragment} Machine learning 🚫
* {:.fragment} Natural Language processing 🚫

__We'll touch on the following topics, but it'll only be introductory material__
{:.fragment}

* {:.fragment} Data visualization on the web 🤷‍
* {:.fragment} Consuming web APIs🤷‍
* {:.fragment} Big data 🤷‍
* {:.fragment} Cloud computing 🤷‍
</section>

<section markdown="block">
## About... You

__I expect (hope?) that you__:

1. {:.fragment} are comfortable __quickly picking up basics of a new programming language__
  * {:.fragment} Python, SQL ...and to a lesser extent, JavaScript (probably in the context of d3) and SVG (maybe)
2. {:.fragment} are _ok_ using the __commandline__
3. {:.fragment} have the ability to __install tools and software__, navigate through your __file system__ - you know _everyday computing stuffs_
4. {:.fragment} are comfortable learning some topics on your own / researching on your own (especially when finding your own data sets)
5. {:.fragment} __submit assignments on time, come to class on time__, etc.

</section>

<section markdown="block">
## A Quick Poll

__Hands up 🙌 if you__... 

* {:.fragment} took Database and Web Implementation (60)
* {:.fragment} started off with Intro to Programming  (in Python, 0002)
* {:.fragment} went through Big Data Science or Predictive Analytics (grad classes and a 480)
* {:.fragment} took AIT (specifically because there was some MongoDB in there)
* {:.fragment} worked professionally in data analytics or data science
* {:.fragment} ...are in the CS major? <span class="fragment">DS major?</span> <span class="fragment">other?</span>
</section>




<section markdown="block">
## What if you already know this? 💡

* {:.fragment} Maybe you've __already taken several web minor courses__ 
  * (specifically CSCI-UA.0060, the course on databases)
* {:.fragment} Or you __do this professionally__ 
  * {:.fragment} as an ETL engineer
  * {:.fragment} or as a data scientist?

There may be __signficant overlap__ with the material in the __web minor databases class__ or in your professional work
{:.fragment}

* {:.fragment} <span class="hl">you should give some thought as to whether or not you should stay enrolled</span> in this course
</section>

<section markdown="block">
## What About Python 🐍?

However, if you...  

* already took <span class="hl">0002</span> (intro to programming) 
* or if you have some beginner <span class="hl">Python experience</span>

__It's ok!__ 🙌
{:.fragment}

* {:.fragment} we'll go over some __intermediate python features__
* {:.fragment} and some __popular libraries__ you _may_ not be familiar with yet 

(⚠️ the first couple of weeks will cover python _very_ quickly! 🐍⏩)
{:.fragment}
</section>

<section markdown="block">
## Ok, So... About Me

### Joe Versoza

* {:.fragment} I also teach __AIT__ (_perhaps u no of this 🤔?_), an __Intro to Programming__ course (in Python, of course), and sometimes (er, _never_?)  __101__
* {:.fragment} I'm a __Clinical Assistant Professor__ (you can find me at: {{ site.vars.office_hours_room }})
* {:.fragment} In former a life, I worked with PostgreSQL and Python _a lot_
  * {:.fragment} (not-so-much now...)
  * {:.fragment} for things like... <span class="fragment">data driven web sites</span><span class="fragment">, data in a regulated environment</span><span class="fragment">, and simple analytics</span>

</section>


<section markdown="block">
## Workload 

* {:.fragment} <span class="hl">2 x exams</span> (__final is last day of class, not during finals week!__)
* {:.fragment} <span class="hl">8 x [homeworks](../../syllabus.html#homework)</span> (maybe 1 or 2 more)
  * {:.fragment} __Write your own code!__
  * {:.fragment} submit via git (fill out the survey!)
* {:.fragment} <span class="hl">8 x [online quizzes](../../syllabus#quizzes)</span>, completed from home (maybe 1 or 2 more)
* {:.fragment} <span class="hl">1 x small project</span> (this be a small research project of your choosing, approximately 2 weeks long)
</section>


<section markdown="block">
## About that Homework

__If you need help__ &rarr;

* {:.fragment} __please ask on piazza__ - public posts are encouraged (just don't give away the solution)
* {:.fragment} high level discussions with other students are ok ✅
* {:.fragment} help debugging an exception/error from other students is ok ✅
* {:.fragment} see me or the tutor (office / tutoring hours)

</section>

<section markdown="block">
## What About Help from the Internets???

__Using online resources outside of the course materials...__
{:.fragment}

* {:.fragment} is <span class="hl">ok if it's just a line or two and you annotate your code with a comment</span> and a link ... for example:
    * a snippet of example code directly from documentation
    * a couple of lines from stackoverflow to get a library working 
* {:.fragment} is <span class="hl">not ok if  you're lifting significant amount of code from an online tutorial or another project</span> found online

</section>

<section markdown="block">
## Writing Your Own Code

Whatever you do, though... __write your own code!__ This means:

* {:.fragment} __don't copy__ (clone, download, etc.) anyone else's code 👯
* {:.fragment} __don't distribute/publish your code__ (including publishing to a public git repository or posting in a forum) 🚫

The Director of Undergraduate Studies will handle any instances of cheating or software plagiarism
{:.fragment}


</section>


<section markdown="block">
## Additional Course Info

* {:.fragment} __Office Hours:__ {{ site.vars.office_hours }}
* {:.fragment} __Office Hours Room:__  {{ site.vars.office_hours_room }}
* {:.fragment} __Readings:__ [See book info on syllabus](/syllabus.html#books)
  * {:.fragment} {{ site.vars.book2 }} (first 6 weeks of class)
  * {:.fragment} {{ site.vars.book1 }} (next 6 weeks of class)
  * {:.fragment} various online references / documentation (remainder of class)
* {:.fragment} __Grading:__ [weights for homework, exams, etc.](/syllabus.html#grading)
</section>


<section markdown="block">
## Required Software

__Python 3.x and associated libraries__
{:.fragment}

* {:.fragment} `numpy`, `pandas`, `matplotlib`, `jupyterlab`, `requests`, etc.
* {:.fragment} installed through either... 
  * Anaconda / `conda` (recommended)
  * or `pip` 
  * or `pipenv`, `poetry`, etc.
* {:.fragment}  you're free to use any editor and os you want
  * {:.fragment} I'd recommend [spyder](https://www.spyder-ide.org/) or [PyCharm](https://www.jetbrains.com/pycharm/)
  * {:.fragment} we'll also be using Jupyter Notebook / Lab _a lot_ early on

__PostgreSQL__
{:.fragment}

* {:.fragment} a local install of [PostgreSQL](https://www.postgresql.org/), maybe [DataGrip](https://www.jetbrains.com/datagrip/)

</section>

<section markdown="block">
## Reading

We'll be using these books:

* [{{site.vars.book1}}]({{site.vars.book1_link}})
* [{{site.vars.book2}}]({{site.vars.book2_link}})
* [{{site.vars.book3}}]({{site.vars.book3_link}})
* [{{site.vars.book4}}]({{site.vars.book4_link}})
* [{{site.vars.book5}}]({{site.vars.book5_link}})

They _should_ all be available from the library (__DEMO TIME!__); I'd recommend browsing through them and then deciding which ones you'd like to own.

The readings often list chapters that cover the same material, but from different books; it's adequate to just read one (er... minimally _enough to do the quizzes?_).


</section>

<section markdown="block">
## This Site, These Slides

* you can find my courses at [http://cs.nyu.edu/~jversoza/](http://cs.nyu.edu/~jversoza/)
* use <span class="hl">arrow keys</span> to navigate ⬅️➡️
* click on <span class="hl">print</span> to see a one page version 📄
* probz does not work great on mobile (sry) 😅
	* {:.fragment} (also, for those in AIT, u _still trust me_ to teach u abt the web? ... this site is _terrible_ 🤮)

</section>

<section markdown="block" data-background="#440000">
## A Quick Summary

* {:.fragment} There's a <span class="hl">decent amount of work</span> as this will be a _hands-on_ / practical class! 🛠
* {:.fragment} But don't worry... __I'm available for help__! 
  * piazza or ...
  * in-person (ask the question in class, during office hours, or make an appointment) 🤚
* {:.fragment} the <span class="hl">2nd exam is on the last day of class</span>, NOT DURING FINALS WEEK ⚠️
* {:.fragment} If you're a __graduating senior__, make sure you do the work; I can't just hand out C's (also, are you _really_ just trying to get a C?)! 🎓
* {:.fragment} __Write your own code for assignments!__ ✏️
* {:.fragment} Plz do the readings / quizzes 📕


</section>
