# 2010 geographic census data

* unified school districts


Initial pass at data file
====

1. download the file
2. view it in libreoffice / excel
3. cross reference that with column guide

Goal
====

* get it into a database
* simple data cleaning / preparation
* ask some questions
* which state has the most school districts
* which state has the largest population density


Make a table
====
* data type
* primary key
* what is a null valuej
	* null is missing value
	* null is not same as ""
	* depending on your csv ... ,, <-- null  ,"", <-- empty string
	* COPY has facility to determine what's string

Import
====
COPY tablename
	FROM '/file/name.csv' -- <== make sure to change to forward slashes and surround in single quotes
	csv HEADER DELIMETER AS E'\t'

COPY school_district FROM '/tmp/Gaz_unsd_national.txt' csv HEADER DELIMITER AS E'\t'



Clean up Data
====



Queries
====
























