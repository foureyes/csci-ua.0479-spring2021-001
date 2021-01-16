---
layout: homework
title: "Final Project"
---

<style>
img {
    border: 1px solid #000;
}

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}
</style>

# Free-form "Homework" / Mini Project

## Due Monday, Dec 9th

For your last assignment, you'll have a free-form, mini-project! You can create __anything__ you want for your project, as long as it meets the technical requirements below. If you have a personal project that you've been looking to start (and is relevant to the material, of course) or if you just want something for your portfolio, This your chance to work on it!


## Requirements

* no group projects allowed!
* must work with a database

### OPTION 1 - Relational Database or NoSQL Database


* 20% - Documentation
* 20% - Create an ER Diagram or sample documents and collections
* 20% - Create scripts to import, collect, or generate data
	* These can be in pure sql or Python (any library is ok - `pandas`, `SQLAlchemy`, etc.)
	* Add comments in `.sql` or `Python` file
	* Data source can be:
		* directory from text files (`csv`, `tsv`, etc.)
		* an API
		* created (manually by using the `random` module or by using a module, like `faker`)
* 20% - Perform some analysis
	* If using SQL, must use two of any of the following (repetition is ok):
		* view
		* function
		* CTE
	* If using NoSQL must use two of any of the following (repetition is ok):
		* aggregation functions
	* IF using pure Python, must use two of any of the following (repetition is ok):
		* list comprehension
		* hof
* 20% - Research some technology not covered in class
	* This technology can be used in any previous part or additional part (for example, if you want to implement web visualization)
	* Some examples of postgres functionality that we have not used in class:
		* `cross tab`
	* Some examples of Python modules that we have not used in class:
		* `nltk`


Examples

* small gui / cli desktop application backed by a relational database
* small web application using mongodb as the backend
* visualization of database using Python and advanced matplotlib (or other visualization library)
#### Details


### Ideas

You're free to do whatever project you want, as long as it meets the technical requirements. You will not be graded on visual design, user experience or novelty. However, your project should be something that's _interesting_ for you to work on, and usually that means putting in some creative effort!

* an interactive story / web application
    * store high scores in a database or csv file
    * using flask to serve everything up
* data visualization
    * download data using requests
    * use csv module or beautiful soup to extract data
    * visualize data using turtle 
* creating a flask-like web framework
    * like we did in class / for hw
* instagram style site
    * using pil (the filters that you created form hw)
    * using requests to download an image from another iste
    * using flask to serve everything up
* use pygame to create a "platform" game
* digital instrument
    * digital signal processing
    * turtle or tkinter to create interface
