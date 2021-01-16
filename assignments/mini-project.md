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


⚠️ __Please "scope" your project accordingly; it should result in about one week of work (similar to a homework assignment)__

* it can be as challenging (or easy) as you like
* scoring is transparent; 👀 see the grading rubric below


## Base Requirements

1. Individual work only (no group projects)
2. Project must involve the use of a relational database or NoSQL database
3. ⚠️ __DO NOT INCLUDE PASSWORDS IN YOUR REPOSITORY__
	* read your database credentials from a configuration file that you place into `.gitignore`
	* or simply leave the credentials blank and add instructions in the `README.md` to fill them in for the grader


## Grading Rubric


### __20%__ - Documentation

* (5 pts) In `README.md`, briefly describe your project
* (10 pts) Choose one:
	1. If working with existing data:
		* Document the source of the data
		* Describe the fields / columns and their types
	2. If generating new data
		* Describe how this data will be used and how data will _eventually_ be generated
		* Describe the fields / columns and their types
* (5 pts) ⚠️ Add instructions for the grader
	* Specify what scripts to run (if any)
	* Or link to a file showing the output of your analysis


### __20%__ - Create an ER Diagram or sample documents and collections

* ⚠️ If using an image, make sure to embed the image into `README.md`
* ...otherwise, you can simply use a fenced called block (three backticks at the beginning and end of the code) to format a MongoDB document

### __20%__ - Create scripts to import, collect, or generate data

* These can be in pure sql or Python (any library is ok - [`pandas`](https://www.youtube.com/watch?v=eVGu5xMoncM), [`SQLAlchemy`](https://www.sqlalchemy.org/), [`pymongo`](https://docs.mongodb.com/ecosystem/drivers/pymongo/), etc.)
* Add comments in `.sql` or `Python` files
* Data source can be:
	* text files (`csv`, `tsv`, etc.) included in the repository (size permitting)
	* colected via an API
	* created or generated (manually by using the `random` module, using a module, like [`faker`](https://github.com/joke2k/faker))
* (5 pts) Describe any clean up or pre-processing necessary to import or create data
* (15 pts) ⚠️  Link to the actual import scripts in `README.md`



### 25% - Perform some analysis

* (2 pts) In `README.md` Describe the goals of your analysis
* (8 pts) Choose one:
	1. If using SQL, must use two of any of the following (repetition is ok):
		* view
		* function
		* CTE
	2. If using NoSQL must use two of any of the following (repetition is ok):
		* aggregation functions
	3. If using pure Python, must use two of any of the following (repetition is ok):
		* list comprehension
		* your own higher order functions
		* your own class
* (15 pts) ⚠️  Link to the actual analysis scripts in `README.md`


### 15% - Research some technology not covered in class

* This technology can be used in any previous part or additional part (for example, if you want to implement web visualization)
* Some examples of postgres functionality that we have not used in class:
	* [cross tab](https://www.postgresql.org/docs/current/tablefunc.html)
	* [PostGIS](https://postgis.net/)
* Some examples of Python modules that we have not used in class, but you may be interested in:
	* [`faker`](https://github.com/joke2k/faker)	
	* [seaborn](https://seaborn.pydata.org/)
	* or other more ambitious libraries outside the scope of what we've learned:
		* [`nltk`](https://www.nltk.org/)
		* [`skilearn` / sciekit-learn](https://scikit-learn.org/stable/)
		* [`torch` / pytorch](https://pytorch.org/)
* (15 pts) ⚠️  In `README.md`, link to the lines in your repository where you use this library and describe what you've used it for


## Examples / Ideas

Similar to what we've done in class:

* visualization of data in database (data in postgres or mongodb, visualization in notebook using matplotlib, seaborn, etc.) 

More ambitious: 

* small gui / cli desktop application backed by a relational database
* small web application using mongodb as the backend
