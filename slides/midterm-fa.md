"""
decorator will take an old function
return a new function
new function will "modify" old function in some way
"""
def f(old_fn):
	def g(*args):
	  type(args)
	  return old_fn(*args)
	return g
@f
def oldfn(a, b):




* review on group by (other queries too)
* having
* regular expressions
* map v applymap v apply
  * on series
* decorators
	* @ decorator syntax

exam on tuesday

format

* short answer
	* what are the categories of nosql databases
	* name some formats that we've and give a syntactically correct example of each
* what's the output
	* you'll get a bunch of code... and say what it prints, or resulting table / df / etc.
* short queries or code snippets
	* show me all of the rows that have a missing value in this dataframe
	* with a list comprehension transform this list in this manner
* coding questions
	* answer 3 out of 4 questions (2/3)
		* ~ 20 lines of code per question

priorities
-----
1. know what you did for homework
2. sample questions
3. slides / notebooks / quizzes
------
4. readings for reinforcement of above


topics
-----
classes 1 - 13

all homeworks so far:
* tabletools
* cleaning data / viz
* pandas
* sql

python
---
* basic list, string, etc. manipulation (esp. in realm of dealing w/ data)
* file io
* list, set, dict comprehensions
* iterators and generators
* functions as objects / decorators

file formats / data
---
* csv, json, whatever-delimted, fixed width
* using basic python to parse above (w/ and w/ out pandas)
* how do computers store data
	* character encoding ... utf-8
* working with web requests
* v basic css selectors

numpy
---
w/in context of pandas

* numpy array
* basic selections
* array ops... summary statistics
* vectorized ops
* broadcasting

pandas
---
* selecting
	* cols
	* using bools
* transforming
	* map/applymap
	* reindexing
	* adding columns
* misc
	* finding and filling missing values
	* grouping (multi index or group)
	* import (know u can do it, don't memorize keyword args)

db/sql
---
* diff types of db
	* nosql vs relational (object, hybrid, etc.)
	* types of nosql
		* key / value
		* object
* select
* select list
* from
* where
* group by / having
* aggregate functions (min, max, count, etc.)
* order by, limit, etc.
* figure out how they work (know the order of processing)
* alter
* create
* update
* delete


















