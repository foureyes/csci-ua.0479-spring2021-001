---
layout: default
nav-state: help
---

## General Help

{{site.office_hours}}

## Installing Packages / Modules

Sometimes Python's built-in modules just aren't enough! Maybe you want to do some fancy plottin' with [matplotlib](http://matplotlib.org/) or you want to make an amazing web application with [Django](https://www.djangoproject.com/).

How do you install them!?

Um... you could use commandline tools, which is totally fine (and probably a good thing to know how to do if you're planning on working with Python professionally, and your environment is OSX or Linux). Check out these tutorials: [Python 3 w/ virtualenvwrapper on OSX](http://www.marinamele.com/2014/07/install-python3-on-mac-os-x-and-use-virtualenv-and-virtualenvwrapper.html), [same on another blog](http://gpiot.com/blog/install-python-3-and-virtualenv-mac-osx/), aaaand [yet another one](https://github.com/QUTPy/QUTPy/blob/master/Getting%20started%20with%20Python3%20on%20OS%20X%20Yosemite.md).

A much easier alternative (and the one I'd recommend for this class), is to let PyCharm manage all of this insanity for you. __See the instructions below.__ &rarr;




### Starting a PyCharm Project With a virtualenv

You'll need to start out with a __virtualenv__, which is basically an isolated Python environment (an interpreter along with a bunch of installed modules).

1. create a new project
2. click on the gear icon next to the field marked interpreter
3. choose "Create VirtualEnv"
4. fill in a name for your virtualenv 
5. ensure that the base interpreter is Python 3.x ... and hit ok
5. this will automatically set the interpreter field with your newly named virtualenv

You can see all of this in the video below...

### Installing a Module with PyCharm

Once you have a virtualenv, you can install modules to your heart's content (but they'll be isolated to your virtualenv, which is specific per project).

1. Go to PyCharm &rarr; Preferences
2. In the left panel, expand Project: projectname, and choose Project Interpreter
3. Click on the + icon...
4. Search for the module to install

Again, check out the video below.

### A reallllly long video with no sound and a lot of pauses (YES!)

<video controls>
    <source src="resources/video/pycharm-virtualenv.webm" type="video/webm">
    <source src="resources/video/pycharm-virtualenv.mp4" type="video/mp4">
    Your browser does not support the <code>video</code> element.
</video>
