## reload restart

* reload reloads configuration, does not restart server
	* connections that are already present stay connected
	* (and they may not see config changes)
* restart --- a full stop and then a start

## client / server architecture

* a long running process... your database server
* some sort of client to connect to the server
	* (multiple clients ... concurrently connected)
	* (the clients can be ... a commandline client, or a graphical client)
		* psql
		* pgadmin - graphical
		* datagrip 30 day free
		* phppgadmin - web based one

## hierarchy

* postgres instance (an installation or a "cluster")
* databases
* schemas <-- default schema is public
	* relations
		* tables
		* views
		* functions etc.


## psql commands

\l - list all dbs
\d - all relations
\dn - all schemas
\dv - all views
\dt - all tables
\d tableName - describe that table
... if you add uppercase S, that will show you system object


naming conventions
====
* consistent pluralization or non-pluralization of table names
	* student or students (but make sure all other table match)
	* table and column names are typically lowercase and underscore separated
	* postgres is case insenstive without quoting, but with quoting it is
		* without quoting it'll automatically lower
	* common suffixes for table names: \_id <-- to denote pk or fk
	* descriptive names that don't clash with reserved words
* sql... some conventions are this:
	* most sql is written with keywords as uppercase
	* (but really it doesn't matter)


## SQL Syntax

* semis to end a query ;!
	* a query can span multiple lines
* if you want a string, delimited by ' single quotes
	* escape a single quote '' <--- actual single quote
	* $$what's this?$$ <--- single quote as well
* comments which are prefixed with --
* calling a function is just function with parens, arument list w commas


## postgres (ANSI SQL)

numeric types

* numeric / decimal (floating point)
* integer (4 bytes)
* real (4 bytes, varying precision)
* serial <--- auto incrementing integer

string types

* text - string of any length
* character varying(n) ... varchar(n) where n is number of characters
* character

weirdo other types that are kind of numeric

* inet, cidr <-- ip address (ipv4 and 6.... a range of ip addresses)
* money <-- localization dependent... will add currency symbol as well as decimal place  (and commas)

temporal types

* timestamp
* timestamptz <--- just use the one with timezone
	* stored as utc
	* when you query, it comes out as local time zone
	* ISO standard for dates and times YYYY-MM-DD HH:mm:ss

## casting

CAST (colname as newType)
val::newType





student

netid
classes
first
last
expected grad date
student debt
midtermscore

-- don't error out and just try to drop the table if it's there
DROP TABLE IF EXISTS student;

-- if it exists replace w/ new def
CREATE TABLE student (
	netid varchar(100) PRIMARY KEY,
	class text,
	first varchar(255) NOT NULL,
	last varchar(255) NOT NULL,
	grad_date timestamptz DEFAULT NOW(),
	debt money,
	midtermscore numeric
);


## constraints

* NOT NULL
* PRIMARY KEY <-- not null AND unique identifier
	* PRIMARY KEY(colName)
* UNIQUE 

* DEFAULT specifies default value

## primary key

* can be something found in data
	* natural primary key 
* you could also create it
	* surrogate or artificial
	* auto increment (serial field)

1. make sure that it's unique (that holds true for either kind)
2. natural primary key means less columns (less noise)
3. intuition if natural
4. trickier to ensure uniqueness
5. your primary key shouldn't change its value





























































































































