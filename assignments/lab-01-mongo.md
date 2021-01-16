---
layout: homework
title: "Lab #01 / Homework #7"
---
<style>
.hl {
	background-color: yellow;
}
img {
    border: 1px solid #000;
}

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}

.hidden {
    display: none;
}

.hintButton {
    color: #7788ff;
    cursor: pointer;
}

.background {
	background-color: #eeffee;
}
</style>
<script>
document.addEventListener('DOMContentLoaded', hideHints);

function hideHints(evt) {
    document.querySelectorAll('.hint').forEach((ele, i) => {
        const div = document.createElement('div');
		const label = ele.getAttribute('data-name');
        div.id = 'hint' + i + 'Button';
        ele.id = 'hint' + i;
        ele.classList.add('hidden');
        div.addEventListener('click', onClick);
        div.textContent = `Show ${label}`;
        div.className = 'hintButton';
        ele.parentNode.insertBefore(div, ele);
    });

}

function onClick(evt) {
    const hintId = this.id.replace('Button', '');
    const hint = document.getElementById(hintId);
    hint.classList.toggle('hidden');
	const label = hint.getAttribute('data-name');
    this.textContent = this.textContent === `Show ${label}` ? `Hide ${label}` : `Show ${label}`;
}
</script>

# Lab #01 / Homework #07 - SQL Alchemy, MongoDB - Due In-Class, November 26th at End of Class

In this lab, you'll:

1. Work with SQLAlchemy's ORM to:
	1. Create classes that represent tables in your database
	2. Create _actual_ tables in the database (without writing any SQL!)
	3. Insert rows into the tables that you created (without writing any SQL!)
	4. Read some data from the tables (without writing any SQL!)
2. Try out MongoDB
	1. Export Postgres data to a json file
	2. Install MongoDB (if 
	3. Import the json file into MongoDB
	4. Run a few queries on the resulting dataset through MongoDB

__Scoring__

* 60% - attending
* 85% - submitting any code
* 15% - attempted both parts

__Submission__

⚠️ Submit by using the form at the end of the instructions.

__Starter Code__

[Homework 07 Starter](homework07-starter.zip)

## Part 1: SQLAlchemy

Your _Scoot Share_ business is still running along, but you're tired of using SQL to keep track of your inventory. You're more of a Python person (dare I say... a _pythonista_ or a _pythoneer_?), so you decide to use SQLAlchemy to manage your scooter inventory. 


### Background Information for SQLAlchemy ORM Classes

Your repository should have a bunch of `.py` files already present in it. Your first step to freeing yourself from SQL jail is to create some classes (`ScooterType` and `Scooter`; `Company` will already be made for you) in `model.py` that can be used to represent tables for your scooter inventory. A company makes different types of scooters, and your inventory consists of scooters that are each a specific type (you can have multiple of the same kind of scooter).

The tables that represent scooters, scooter types and companies won't exist yet; they'll be created by using the classes that you implement. The classes should also allow you to write the following Python code to insert new scooters and get scooter data, all without writing any SQL.

👀 __Skim__ through the background material below to see how the classes can be used (no need to code yet).

<div class="hint background" data-name="Background Material" markdown="block">
__Setup (Modules and Initialization)__

In the imports below:

* `db.py` is a module that is already fully implemented and included in your repository
* it connects to the database an gives you access to an engine object: `db.engine`
* `model.py` is the module that you will implement your classes in
	* ... the classes that you'll implement are `ScooterType` and `Scooter` (`Company` is already created for you)
	* note that the base class for the classes, `Base`, is also accessible through the module when importing `model.py`

```
from sqlalchemy.orm import sessionmaker

# connect to the database / create engine (db.engine is available in module)
import db

# bring in the classes (including the base class, Base)
from model import Company, ScooterType, Scooter, Base

# create a session: 
Session = sessionmaker(db.engine)
session = Session()
```

__Creating Companies__

The following code uses the `Company` class to:

* create two companies...
* the first version sets attributes explicitly: `foo.bar = 'baz'`
* while the second version uses keyword args to set attributes: `Foo(bar='baz')`
* (either version is ok to use for setting attributes)
* primary keys are left out and filled in the by the database (once the objects are "saved" to the database)

```
superfastco = Company()
superfastco.name = 'Super Fast Co'
superfastco.website = 'superfast.lol'
superfastco.founded = 2017

scootz = Company(
    name='Scootz LTD',
    website='scootz.jp',
    founded=2000 
)
```

__Creating Scooter Types__

The code below... 

* creates 3 scooter types by using the `ScooterType` class
* ...and relates them to a company (by simple assignment)
* note that this relation to a company is through an attribute called `manufacturer` (this actually won't exist in the database, but will exist in our objects!)
* again, these scooter types are created by using a mix of keyword arguments and setting attributes
* again, primary keys are left out and filled in the by the database (once the objects are "saved" to the database)

```
sf_pro = ScooterType()
sf_pro.model = 'SFV1'
sf_pro.max_range = 200
sf_pro.weight = 15
sf_pro.max_speed = 40

# manufacturer refers to a company!
sf_pro.manufacturer = superfastco

sf_lite = ScooterType(
    model='Scoot Lite v2',
    max_range=100,
    weight=10,
    max_speed=30,
    # manufacturer refers to a company!
    manufacturer=superfastco
)
```

__Creating Scooters__

Using the `Scooter` class, the code below:

* makes 3 scooters...
* the `scooter_type` is set using the types created above
* `retired` has a default value, so it can be left out
* as usual, primary keys are left out and filled in the by the database (once the objects are "saved" to the database)

```
s1 = Scooter()
s1.acquired_date = '2017-10-01'
s1.scooter_type = sf_pro
# (we don't set retired, allow default value of False)

s2 = Scooter()
s2.acquired_date = '2017-08-05'
s2.retired = True
s2.scooter_type = sf_pro

s3 = Scooter(
    acquired_date='2018-12-30', 
    # explicitly set retired (despite already set default value of False)
    retired=False,
    scooter_type=sf_lite
)
```

__Finally, Insert Scooters, Scooter Types and Companies!__

* `session.add_all` and `session.commit` will add all of the scooter to the database
objects
* note that the "links" to scooter types and companies will cause those objects to be saved too (in the `scooter_type` and `company` tables)

```
# the scooters along with their types and companies will be inserted!
session.add_all([s1, s2, s3])
session.commit()

# notice that that the primary key for these scooters will be filled in!
for scooter in [s1, s2, s3]:
    print(scooter)

session.close()
```
</div>

### Create SQLAlchemy ORM Classes and Tables (`model.py`, `config.ini`)

With the information above, you're ready to start coding!

In this part you will:

1. ✏️ write code in `model.py`
2. 🏃 run `create.py` (which imports your work from `model.py`)

Detailed instructions: 

1. Create the following SQLAlchemy classes: `ScooterType` and `Scooter` (`Company`) in `model.py` 
	* __infer__ the types and fields of your SQLAlchemy classes in `model.py` from the examples above and also ⚠️__make sure to view the example tables__⚠️ later on in step 3 of this section 
	* implement the classes so that a `Scooter` has a `ScooterType` and a `ScooterType` has a `Company` (from the other perspective, `Company` can have many `ScooterType`s ...and a `ScooterType` can have multiple _actual_ `Scooter`s
	* use the notes from the [SQLAlchemy slides](https://cs.nyu.edu/courses/fall18/CSCI-UA.0480-007/_site/slides/py-db/sql-alchemy-relationships.html) to construct the classes
	* in combination with these slides, [check the documentation to include back references](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-one) so that in a one-to-many relationship, both the parent (one) and child (many) can refer to each other 
	* this should allow functionality like: retrieving all the companies, and then asking for the scooter types for each company by dotting the company instance (`c.scooter_types`):
		<pre><code data-trim contenteditable># assuming session is created and all imports are present:
companies = session.query(Company)
for c in companies:
    print(f'The company, {c}, has the following scooter models:');
    for i, scooter_type in enumerate(c.scooter_types):
        print(i, scooter_type)
    print('\n')
</code></pre>
	* this is done by setting  `relationship("ScooterType", back_populates="manufacturer")` (you can see this in the defintion of `Company`)
	* ...but it should also allow going back up the other way; that is refer to company from a scooter
	* in the example below, notice that this is done through a `manufacturer` attribute (note that `manufacturer` doesn't exist in the table, just in the instance... and of course, the relationship is only possible by setting up by a `company_id` foreign key)
		<pre><code data-trim contenteditable>scooter_types = session.query(ScooterType)
for s in scooter_types:
    print(f'{s.manufacturer.name} ==> {s.model}')
</code></pre>
	* all classes should have surrogate / artificial primary keys
	* (these can be named at your discretion; just make sure to match up the names to set up relationships between classes appropriately)
	* in addition to creating the appropriate fields and relationships, add a `__repr__` and `__str__` method to each class (both doing the same thing):
		* for a company, the string returned should be: the company's name, website and year founded
		* for a scooter type, the string returned should be: the name of the company that manufactured it followed by the model name, max speed and weight
		* for an _actual_ scooter, the string returned should be: the scooter's id, retired status, type (that is the same string as above), and when it was acquired
		* hint 1: a nested field can be retrieved by chaining the dot operator (for example, to get the scooter model from the scooter_type from within the `Scooter` class: `self.scooter_type.model`)
		* hint 2: if referencing an instance of a related class within a string context, that instance's `__str__` is called (so within the `Scooter` class, using f'self.scooter_type' would give the string version of the associated `scooter_type`)
2. Create a configuration file called `config.ini` so that your Python scripts can connect to a database called `homework07`
	* copy `config.ini.example` to a file called `config.ini`; this will be the configuration for all of the Python scripts that have to connect to the database
	* modify `config.ini` so that the username and password are correct for your database setup
	* ⚠️ __if you don't typically use a password when working with postgres, delete BOTH the username and password fields in `config.ini`
	* alternatively, if you don't have a password you can also:
		* create a new super user by issuing the following command in your postgres client (`psql`, `pgAdmin`, `datagrip`, etc.)
		* `create role YOUR_NEW_USERNAME with login superuser password 'YOUR_NEW_PASSWORD';`
		* you may have to change `pg_hba.conf` to include this line:
		* `host    all             joe             127.0.0.1/32            md5` 
		* ...and restart your server
3. Create the tables specified by your classes
	* the file, `create.py`, contains code that will use the classes that you implemented in `model.py` to create tables
	* 🏃 run `create.py`
	* (it imports the `Company`, `Scooter Type` and `Scooter` classes and runs `model.Base.metadata.create_all(db.engine)`)
	* when you're done creating classes, the resulting tables should like like this (check in psql or DataGrip):
	* __company__
		<pre><code data-trim contenteditable>   Column   |       Type        
------------+-------------------
 company_id | integer           
 name       | character varying  
 website    | character varying  
 founded    | integer            
</code></pre>
	* __scooter_type__
		<pre><code data-trim contenteditable>     Column      |       Type        
-----------------+-------------------
 scooter_type_id | integer           
 model           | character varying  
 max_range       | integer            
 weight          | integer            
 max_speed       | integer            
 company_id      | integer            
</code></pre>
	* __scooter__
		<pre><code data-trim contenteditable>     Column      |  Type   
-----------------+---------
 scooter_id      | integer 
 acquired_date   | date     
 retired         | boolean  
 scooter_type_id | integer  
</code></pre>


### Creating and Reading Data (`mock.py`)

Generate some data! In this part, you will:

1. ✏️  write code in `mock.py`
2. 🏃 run `mock.py` to fill your newly created tables


Write a script to fill your database with companies, scooter types and scooters _without_ writing any SQL!

1. In the file, `mock.py`, use the classes you implemented to make:
	1. 3 (or more) x companies
	2. 8 (or more) x scooter types
	3. 70 (or more) x scooters
2. It's ok to manually create the companies and scooter types, but you _should_ programmatically generate the scooters by using random numbers
	* (the reference solution _actually_ randomly generates scooter model names and company names, so if you're feeling ambitious, feel free to do that as well)
	* hint 1: a `Date` field can be set by using the following string format: `YYYY-MM-DD` (for example, `'2018-12-07'`) 
	* hint 2: here's one way to create a random date with `0` padding for month and day: `f'{random.randint(2014,2018)}-{random.randint(1, 12):02}-{random.randint(1,28):02}'`
    * hint 3: use the `random` module's `choice` method to retrieve a random element from a list: `random.choice(['foo', 'bar', 'baz'])` 
	* hint 4: it _may be_ a good idea to create companies first, with each company in a list... and then do the same with scooter types... this will make it easier to use `random.choice` to -- for example -- assign a random scooter type to a scooter or a random company to a scooter type
	* hint 5: if you have your relationships set up correctly for your classes, you'll only need to `session.add(LIST_OF_SCOOTERS)` for a list of scooters (rather than for scooters __and__ scooter types and companies
3. After calling `session.commit()`, write these two queries (adjust field name and/or variable names as necessary) to:
	* get all companies, and print all of the scooter types produced by each company
		<pre><code data-trim contenteditable>for c in session.query(Company):
&nbsp;&nbsp;&nbsp;&nbsp;print(f'The company, {c}, has the following scooter models:');
&nbsp;&nbsp;&nbsp;&nbsp;for i, scooter_type in enumerate(c.scooter_types):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(i, scooter_type)
&nbsp;&nbsp;&nbsp;&nbsp;print('\n')
</code></pre>
	* get all the scooters types and print out the manufacturer name (company name) and the model name
		<pre><code data-trim contenteditable>for s in session.query(ScooterType):
&nbsp;&nbsp;&nbsp;&nbsp;print(f'{s.manufacturer.name} ==> {s.model}')
</code></pre>
4. 🏃 run `mock.py`

### Validating Data

To check the data that you created, use either the psql commandline client or DataGrip to:

1. View the first few rows of your table
2. Determine if the data is "joinable" ... for example, you can try to:
	* show the scooter id, company name, scooter model, weight, max speed and retired status

## Part 2: MongoDB Export and Queries (`model.py`, `scooter.json`, and `mongodb-output.md`)

Export part of the data from the `homework07` postgres database into json. Use that json as an import for mongodb... and run some basic `mongo` commandline queries against it.

1. Modify your `Scooter` class by adding a `to_dict(self)` method (this should be present)
	* within that method, create a dictionary 
	* add the following keys
     	* `acquired_date` (should be set to the scooter's acquired date by using `self.acquired_date.strftime('%Y-%m-%d')`)
		* `retired`	
		* `scooter_type` (in this case, just use the associated scooter type's model name as the value) 
   		* `max_speed`
        * `weight`
        * `manufacturer` (should be set to the company that produces the type of scooter that this scooter is by using `self.scooter_type.manufacturer.name`),
		* "website" (should be the manufacturer's website)
	* return the dictionary
2. Once that method is complete, 🏃 run `export_to_json.py` ... converts all of the scooters in the database into dictionaries, which are then serialized into JSON and written to a file called `scooters.json`
3. Install MongoDB: [use the official documentation](https://docs.mongodb.com/manual/installation/)
4. Import the data using the commandline tool, `mongoimport`:
	* import into a database called `homework07`
	* use a collection called `scooters`
	* `mongoimport --db homework07 --collection scooters --file scooters.json --jsonArray`
5. Make sure the __server__ (mongodb) is up by running `mongod` in terminal / cmd.exe
6. Start the mongodb commandline __client__ by running `mongo` in terminal / cmd.exe
7. In the client, write the following queries:
	1. write a query that filters results based exactly exactly on one property and shows all properties
		* as a markdown header, write the number associated with your query in `mongodb-output.md` (use `##`)
		* write a short description of what your query does adjacent to the number
		* from the mongo client, copy your query and the result of your query into a code block in `mongodb-output.md` (use triple backticks)
	2. write a query that shows only a subset of all properties (a projection) of the first 10 documents
		* in `mongodb-output.md`, document this query in the same manner that you did for query #1
	3. write a query that matches on exactly two properties (use _implicit and_) and shows a subset of all properties and ensure that `_id` is not shown
		* in `mongodb-output.md`, document this query in the same manner that you did for query #1
	4. write a query that uses a dollar operator (such as comparisons or a test for membership)
		* in `mongodb-output.md`, document this query in the same manner that you did for query #1
	5. write a query that uses `$or`
		* in `mongodb-output.md`, document this query in the same manner that you did for query #1
	6. find all scooters in your inventory that either have a max_speed greater than 30 or a weight less than 20... only show: scooter type, manufacturer, max_speed, and weight... and order by fastest to slowest
 	7. find the number of scooters in the inventory per manufacturer by displaying the manufacturer name and count ([see the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/group/))	
		* in `mongodb-output.md`, document this query in the same manner that you did for query #1
	8. add a scooter that's missing some key value pairs... and then try to find it
		* in `mongodb-output.md`, document this query in the same manner that you did for query #1

## Submit the Lab

Turn in the lab at the end of class using this form:

[https://docs.google.com/forms/d/e/1FAIpQLSf3IfBpC81Ifr-ZXk6oiwWN7ILKbO-EX_A0v5vao3LcbVbJGA/viewform](https://docs.google.com/forms/d/e/1FAIpQLSf3IfBpC81Ifr-ZXk6oiwWN7ILKbO-EX_A0v5vao3LcbVbJGA/viewform)
