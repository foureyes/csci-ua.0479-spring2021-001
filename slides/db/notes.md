* course evaluations
	* bowen - bring up evaluations
	* how challenging is it (too difficult too easy just right)
	* how are you finding the homeworks
	* is it what you expect
	* things that are going well
	* things that can be improved
* last minute hw questions
	* data cleaning simple transforms, filling missing values (4 or 5 transformations)
	* ok to use label list and table, but you'll prob have to modify
		* use other python libraries - nltk, dictreader for reading and writing csvs
	* plotting ... ok to use other plotting library (.plot on a dataframe or bring in seaborn)
* database

Characteristics of Tabular Data
====

* table consists of type definitions ... and these types dictate the columns
* columns represents attributes or types of data
* rows represent the _actual_ data ... rows are also called:
	* maybe think of rows as instances of table
	* records
	* tuples

* primary key that is unique for each row in a table
	* artificial pk - manufactured for your data
		* an ever increasing increasing sequence of integers
	* natural pk - an attribute that uniquely ids a row that is part is already part of the data: netid, n-number
	* composite pk - a primary key composed of multiple columns
* multiple tables can be related to each other based on this primary key
	* via foreign keys
	* in table 1, create a new column that contains the primary key of a row in table 2
	* there other models for this, but always some combo of foreign and primary key
* model arbitrarily complex relationships between tables:
	* one to many
	* many to one
	* many to many


all of these are separate columns:

person

id
first
last
address_id


joe 1
alice 1

address

id
street
state
zip
person_id


251 mercer user_id = 1
123 ave a user_id = 1
only one address for every person

user_id | person_id
1          1
2          1
1          2



























