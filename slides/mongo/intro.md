---
layout: slides
title: "MongoDB Intro"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Relational Databases

__Remember when we talked about broad generalizations regarding relational databases? 🤔__ &rarr;

* {:.fragment} relational databases are typically pretty rigid:
	* {:.fragment} highly structured
	* {:.fragment} you have to define the columns and the types of columns before inserting rows
	* {:.fragment} has a lot of features for maintaining  _data integrity_ (such user defined data constraints, foreign keys, etc.)
* {:.fragment} some relational databases guarantee that transactions (or changes in the database) are reliable 
* {:.fragment} see [ACID compliance](https://en.wikipedia.org/wiki/ACID) - Atomicity, Consistency, Isolation, Durability

</section>


<section markdown="block">
## NoSQL Databases

__Let's contrast that with NoSQL databases (that is, _non SQL_, non relational, or even _Not Only SQL_ (how's that for a backronym?)!)__ &rarr;

So, some _stereotypes_ for NoSQL Databases, such as __key-value__ and __document stores__, are that they're:
{:.fragment}


* {:.fragment} sometimes more simple in design and architecture
* {:.fragment} are less rigid / more flexible than relational databases
* {:.fragment} easier to scale "horizontally" (add more machines)
* {:.fragment} not necessarily normalized
* {:.fragment} the underlying structures aren't limited to tables (key-value, document, graph, etc.)

</section>

<section markdown="block">
## NoSQL Databases Continued

__Sounds good 👍 ... why didn't we start using these in the first place?__ &rarr;

Some compromises that a NoSQL database may have to make:

* {:.fragment} not usually ACID compliant
* {:.fragment} simple data structures and architecture moves constraints and referential integrity to application layer
* {:.fragment} lack of standard (or at least mostly standard) language like SQL
* {:.fragment} some NoSQL systems even exhibit lost writes or data loss (because not ACID compliant)

Again, these are very broad generalizations (some NoSQL databases are ACID compliant)
{:.fragment}

</section>


<section markdown="block">
## Document Stores

In __document stores__, data is organized (as the name implies) as semi-structured documents &rarr; 
* {:.fragment} think JSON (other formats too: XML, YAML, etc.)
* {:.fragment} or... a _richer_ key-value store (there's _meta data_ within the document... the keys are usually meaningful)
* {:.fragment} typically, no schema is required (that is, data types of values are inferred from values)
* {:.fragment} typically, semi structured (documents, property names, etc... do not have to be pre-defined)
* {:.fragment} some document stores are are known for high availability and scaling through replication / redundancy and sharding (separating large databases into smaller ones)

Good for applications where flexible data storage or constantly changing data storage is required.
{:.fragment}
</section>

<section markdown="block">
## MongoDB

__MongoDB is a nosql database__. Specifically, it's a document store:

* a single __record__ in Mongo is a __document__ 
* a document is a bunch of key value pairs... 
* hey... __that sounds like...__ &rarr; 
* {:.fragment} documents are similar to JSON / JavaScript objects 
* {:.fragment} (it's actually BSON? 🤷‍)
* {:.fragment} for convenience, we can say that __MongoDB uses JSON document to store records__ 
</section>


<section markdown="block">
## JSON 

__What's JSON again?__ &rarr;

__JSON__ is a data interchange format / file format that is composed of key value pairs. It's _a lot_ like JavaScript object literal notation or even Python dictionary literal notation. A single JSON document / object constists of:
{:.fragment}

* {:.fragment} curly braces
* {:.fragment} keys and values joined by :
* {:.fragment} key/value pairs separated by commas
* {:.fragment} __all keys must be double quoted__
* {:.fragment} values can be numbers, strings, arrays or other JSON documents/objects
* {:.fragment} (you can have documents embedded/nested within other documents)

</section>

<section markdown="block">
## BSON

__Uh BSON⁉️__ 

* {:.fragment} [see the spec](http://bsonspec.org/)
* {:.fragment} __MongoDB uses a binary-encoded format to store JSON documents__
* {:.fragment} this format is called __BSON__ or binary JSON
* {:.fragment} it's similar to JSON (it has embedded documents, arrays, etc.), but...
	* it has additional data types
	* more space efficient
	* faster to read

</section>

<section markdown="block">
## Documents and Collections

A couple of 🔑 terms to remember (yay, definitions again!)

* {:.fragment} __key__ - a field name - analogous to a column in a relational database
* {:.fragment} __value__ - obvs, a value
* {:.fragment} __document__ - a single object or record in our database, 
	* consists of key value pairs
	* similar to a single row in a relational database
* {:.fragment} __collection__ - a group of documents 
	* analogous to tables in relational databases
</section>

<section markdown="block">
## Data Types

Although MongoDB doesn't require you to pre-define the types of values that your documents will have, BSON does have data types ([see full list in docs](https://docs.mongodb.com/manual/reference/bson-types/)). These types __are inferred from the value__. Some available types include:

* {:.fragment} `string` - utf-8 string
* {:.fragment} __numeric types__ - such as `double` (64 bit floating point), `int`, etc.
* {:.fragment} `bool` - true / false
* {:.fragment} `array` -  a list of values
* {:.fragment} `date` - (use `new Date()` or `ISODate()`)
	* {:.fragment} no arg for _now_ or `'yyy-MM-dd HH:mm:ss'`
* {:.fragment} `objectID`

</section>

<section markdown="block">
## ObjectID

The __Object ID__ is a 12-byte value, consists of: a 4-byte timestamp (seconds since epoch), a 5-byte random value, and a 3-byte counter

* {:.fragment} each document in a collection requires a primary key, `_id` that uniquely identifies it
* {:.fragment} if an inserted document doesn't have an `_id`, it will be automatically generated as an __Object ID__

</section>

<section markdown="block">
## Installation

[Comprehensive docs are here](http://docs.mongodb.org/manual/installation/)

* basically, just [use the appropriate installer from their downloads page](http://www.mongodb.org/downloads)
* if you use a package manager, do that instead 
	* they have .debs for Debian and Ubuntu
	* since I'm on OSX, and I use homebrew, I used <code>brew install mongodb</code>
* starting will vary based on OS
* you may need to create and/or specify a directory where your data will be stored, so if mongo doesn't start up, it's missing its data directory
</section>	

<section markdown="block">
## A Whirlwind Tour

Working with MongoDB on the commandline...

If your OS doesn't autostart by default, you can run:

<pre><code data-trim contenteditable>
mongod
</code></pre>

To connect via the commandline MongoDB client and connect to a locally running instance:

<pre><code data-trim contenteditable>
mongo
</code></pre>

This drops you into the MongoDB shell (yay... more shell). You can issue commands that

* inspect the database
* modify and create documents and collections
* find documents
</section>

<section markdown="block">
## mongo (the default mongodb client)

__`mongo` is the client that comes bundled with `mongod`. It's an interactive shell, and it's JavaScript based:__ &rarr;

* {:.fragment} again, start it by typing `mongo` in your terminal
* {:.fragment} you can use JavaScript (the ES6 kind of JavaScript if _you care_) in your shell
* {:.fragment} which means ... you can create variables, use control structures, such as loops and conditionals
* {:.fragment} note that the types in the mongo shell match JavaScript types, not BSON types 
	* {:.fragment} `typeof` any numeric type is _just_ `number`, `typeof` an object id is _just_ `object`

</section>

<section markdown="block">
## Starting Out

__To begin using the commandline client to inspect your data:__ &rarr;

1. make sure that `mongod` is running in a different window (or running _in the background_ or as a daemon)
2. start up the commandline client with `mongo`
3. type in `use databaseName` to switch to the database that you're looking through

From there, you can start querying for data, inserting documents, etc. These basic create, read, update, and delete operations are called __CRUD__ operations...
</section>


<section markdown="block">
## Some Commands

__The following commands can be used to navigate, create and remove databases and collections__ &rarr;

* `show databases` - show available databases (remember, there can be more than one database)
* `use db` - work with a specific database (if unspecified, the default database connected to is test)
* `show collections` - once a db is selected, show the collections within the database
* `db.dropDatabase()` - drop (remove) the database that you're currently in (must `use` first)
* `db.collectionName.drop()` - drop (remove) the collection named `collectionName`

To get some inline help:

* `help` - get help on available commands

</section>

<section markdown="block">
## CRUD!?

__(C)reate, (R)ead, (U)pdate, and (D)elete operations:__ &rarr;

* {:.fragment} db.[collection].insert(obj)
	* <code>db.Person.insert({'first':'bob', 'last':'bob'})</code>
* {:.fragment} db.[collection].find(queryObj)
	* <code>db.Person.find({'last':'bob'})</code>
	* <code>db.Person.find() // finds all!</code>
* {:.fragment} db.[collection].update(queryObj, queryObj)
	* <code>db.Person.update({'first':'foo'}, {$set: {'last':'bar'}})</code>
* {:.fragment} db.[collection].remove(queryObj)
	* <code>db.Person.remove({'last':'bob'})</code>

Where `queryObj` is a name value pair that represents the property you're searching on... with a value that matches the value you specify
{:.fragment}
</section>

<section markdown="block">
## Finding

__Inserting, finding all, then finding by exact number of lives:__

<pre><code data-trim contenteditable>
> db.Cat.insert({name:'foo', lives:9})
WriteResult({ "nInserted" : 1 })
> db.Cat.find()
{ "_id" : ObjectId("57ff86a14639d0fd263f87a0"), "name" : "foo", "lives" : 9 }
> db.Cat.find({lives:9})
{ "_id" : ObjectId("57ff86a14639d0fd263f87a0"), "name" : "foo", "lives" : 9 }
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## Finding Continued

__Inserting more, then using greater than!__

<pre><code data-trim contenteditable>
> db.Cat.insert({name:'bar', lives:2})
WriteResult({ "nInserted" : 1 })
> db.Cat.insert({name:'qux', lives:5})
WriteResult({ "nInserted" : 1 })
> db.Cat.find({lives: {$gt: 4}})
{ "_id" : ObjectId("57ff86a14639d0fd263f87a0"), "name" : "foo", "lives" : 9 }
{ "_id" : ObjectId("57ff86c14639d0fd263f87a2"), "name" : "qux", "lives" : 5 }
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Find and Update Details

* [`find(query, projections)`](https://docs.mongodb.com/manual/reference/method/db.collection.find/#db.collection.find) and `findOne`
	* query documents (default and)
		* `null` or `{}`, `ObjectId("id")`, `ISODate`
	* projection documents (1 vs 0)
	* substr by using regex: `{prop: /substr/i}`
	* query by subdoc
	* `count`, `limit`, `sort` (-1 vs 1)
	* `k: {$op: v}` operators: `$lt`, `$lte`, `$in`, `$nin`, etc.
	* (default) and vs `$and` and `$or`
	* cursor, `next()`, `forEach`
* [`update(query, update, options)`](https://docs.mongodb.com/manual/reference/method/db.collection.update/#db.collection.update) and using `$set`
	* (what happens without it?)
	* push element to an array with `{$push: {k: v}}`
	* `multi` (false), `upsert` (false), others...


</section>

<section markdown="block">
## Insert a Bunch of Snakes


🐍 sneks:


```
db.snakes.insert({name: 'reese slitherspoon', length:3})
db.snakes.insert({name: 'hissy elliot', length:2})
db.snakes.insert({name: 'william snakespeare', length:2})
db.snakes.insert({name: 'hisstopher walken', length:3})
db.snakes.insert({name: 'billy i\'ll-hiss', length:4})
db.snakes.insert({name: 'monty python'})
```
{:.fragment}

</section>


<section markdown="block">
## Find, Limit, Count

🔍 ✋ ✌️


```
db.snakes.find()     // all snakes
db.snakes.find({})   // all snakes
db.snakes.find(null) // all snakes
db.snakes.find({name: null})   // name property is null or missing
db.snakes.find({_id: ObjectID("123abc")})  // snake w/ id 123abc
db.snakes.find(ObjectID("123abc"})         // snake w/ id 123abc
db.snakes.find().limit(2)   // 2 snakes (order implementation specific)
db.snakes.find({length: 3}).count()
```
{:.fragment}
</section>

<section markdown="block">
## Sorting, Projection


📁 🎥

```
db.snakes.find().sort({length: 1})            // sort ascending
db.snakes.find().sort({length: -1})           // sort descending
db.snakes.find().sort({length: -1, name: 1})  // sort w/ 2 criteria
db.snakes.find(null, {_id: 0})                // supress id
db.snakes.find(null, {_id: 0, name: 1})       // only include name

// projection and sort
db.snakes.find(null, {_id: 0}).sort({length: -1, name: 1})
```
{:.fragment}

</section>

<section markdown="block">
## Subdocument, Substring Query

Query for substring using regex:
{:.fragment}

```
db.snakes.find({name: /hiss/i}) // name has hiss, ignore case
```
{:.fragment}

Query object can include subdoc criteria:
{:.fragment}

```
db.books.insert({title: 'Dune', author: {first: 'Frank', last: 'Herbert'}})
db.books.insert({title: 'Frankenstein', author: {first: 'Mary', last: 'Shelley'}})
db.books.find({'author.first':'Mary'})
```
{:.fragment}

</section>

<section markdown="block">
## Operators

Example of greater than `$gt` and `$or`:

```
db.snakes.find({length: {$gt: 2}})
db.snakes.find({$or: [{name: /hiss/i}, {length: {$lt: 3}}]})
```
{:.fragment}
</section>


<section markdown="block">
## Updating

Replace document with `update`

```
db.snakes.update({name: 'hissy elliot'}, {length: 100})
db.snakes.find({name: 'hissy elliot'})  // uh-oh, whole doc replaced!
db.snakes.find()
```
{:.fragment}

Update property with `update` and `set`
{:.fragment}

```
db.snakes.update({length: 100}, {length: 2, name: 'hissy elliot'})
db.snakes.update({name: 'hissy elliot'}, {$set: {length: 100}})
db.snakes.find({name: 'hissy elliot'})
```
{:.fragment}


```
db.collection.update(query, updateDoc, {multi: true}) // update all!
// ⚠️  otherwise, only 1

```
{:.fragment}

</section>

<section markdown="block">
## Arrays


```
db.students.insert({name: 'alice', hw:[91, 92, 93]})
db.students.insert({name: 'bob', hw:[87, 83, 85]})
db.students.insert({name: 'carol', hw:[81, 82, 83]})
```
```
db.students.find({hw: 83}) // array has 83
```
{:.fragment}

```
db.students.find({hw: {$gt: 83}}) // has element > 83
```
{:.fragment}

```
// add 94 to hw array for alice
db.students.update({name: 'alice'}, {$push: {hw: 94}})
```
{:.fragment}


</section>

<section markdown="block">
## cursor, forEach, next

__Using find gives back a `cursor`... if assigned to a variable (`var`, `const`, `let`), you can call cursor methods: `next`, `forEach`, and `map`__ &rarr;

```
var result = db.snakes.find()
result.next()
```
{:.fragment}

```
var result = db.snakes.find()
result.forEach(snek => print(`${snek.name} is a snake`))
```
{:.fragment}

```
var result = db.snakes.find()
result.map(snek => snek.name.toUpperCase())
```
{:.fragment}


</section>

<section markdown="block">
## Importing Data

__Using a local mongodb instance... and the commandline client, `mongo`:__ &rarr;

Import files using `mongoimport`...
{:.fragment}

<pre><code data-trim contenteditable>
# csv
mongoimport --db test --collection books --type csv --file books.csv --fieldFile books_fields.txt
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
# json
mongoimport --db nyc --collection wifi --type json --file wifi3.json
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Adding and removing data

__A quick review of adding and removing data__ &rarr;

(oh yeah, don't forget to tab _a lot_)

* insert
	* `db.bar.insert({'greeting':'hello'})`
* delete
	* `db.remove({})`
* drop
	* drop collection: `db.bar.drop()`
	* `use` ... then `db.dropDatabase()`
</section>


<section markdown="block">
## Querying Books

__A quick examination:__ &rarr;

* {:.fragment} __what databases do we have?__
	* {:.fragment} `show databases`
* {:.fragment} __what collections do we have?__
	* {:.fragment} `show collections`
* {:.fragment} __do we have anything?__
	* {:.fragment} `db.books.find()`
* {:.fragment} __what's a book look like anyway?__
	* {:.fragment} `db.booksfindOne()`
* {:.fragment} __how do we prevent our eyes from bleeding?__ (so many curly braces :( )
	* {:.fragment} `db.books.find().pretty()`
	* {:.fragment} (maybe) `DBQuery.prototype._prettyShell = true in $HOME/.mongorc.js`
</section>

<section markdown="block">
##  Counting and Finding

* {:.fragment} __what if we want to see exactly two books?__
	* {:.fragment} `db.books.find().pretty().limit(2)`
* {:.fragment} __how many there exactly?__ 
	* {:.fragment} `db.books.find().count()`
	* {:.fragment} `db.books.count()`
* {:.fragment} __can we show only books by the author of Pride and Prejudice?__
	* {:.fragment} sure! hint: "Austen, Jane"
	* {:.fragment} use a criteria object / document!
	* {:.fragment} `db.books.find( {"AUTHOR":"Austen, Jane"} )`
* {:.fragment} __how about figuring how many books there are by the guy that wrote war and peace?__ 
	* `db.books.find({"AUTHOR": "Tolstoy, Leo"}).count()`
</section>


<section markdown="block">
## Projections

* {:.fragment} back to jane austen. __let's just see the title and year written of the book that we have on file__
	* {:.fragment} use a projection object / document!
	* {:.fragment} `db.books.find( {"AUTHOR":"Austen, Jane"}, {_id:0, "TITLE":1, "YEAR_WRITTEN": 1} )`
* {:.fragment} do the same, but exclude only the id
	* {:.fragment} `db.books.find( {"AUTHOR":"Austen, Jane"},{_id:0})`
* {:.fragment} __can we supress edition, but include title?__
	* {:.fragment} nah, nope, blah ... not this way:
	* {:.fragment} <s>`db.books.find( {"AUTHOR":"Austen, Jane"},{"EDITION":0,"TITLE":1,"YEAR_WRITTEN":1})`</s>
	* {:.fragment} can't mix inclusions and exclusions; can only supress id
	* {:.fragment} instead: `db.books.find( {},{_id:0,"AUTHOR":1,"TITLE":1,"YEAR_WRITTEN":1})`
</section>


<section markdown="block">
## Sorting

__let's try some sortin'__ &rarr;

* {:.fragment} __sort by author, then title__
	<pre class="fragment"><code data-trim contenteditable>db.books.find({},{_id:0,"AUTHOR":1,"TITLE":1,"YEAR_WRITTEN":1})
	.sort({"AUTHOR":1,"TITLE":1})
</code></pre>
* {:.fragment} __how about by year ascending?__
	<pre class="fragment"><code data-trim contenteditable>db.books.find( {},{_id:0,"AUTHOR":1,"TITLE":1,"YEAR_WRITTEN":1})
	.sort({"year_written":1})
</code></pre>
* {:.fragment} __how about descending order by year?__
	* {:.fragment} use -1 instead of 1 (of course 🤷‍)
		<pre><code data-trim contenteditable>db.books.find( {},{_id:0,"AUTHOR":1,"TITLE":1,"YEAR_WRITTEN":1})
		.sort({"YEAR_WRITTEN":-1})
</code></pre>
</section>

<section markdown="block">
## Comparisons

__OK... now try some comparisons.__  &rarr;

* {:.fragment} __find all books written after 1870__ &rarr;
	* {:.fragment} `db.books.find( {"YEAR_WRITTEN":{$gte:1870}},{ _id:0} )`
* {:.fragment} __how about 1870 and 1900 (inclusive)__ &rarr;
	* {:.fragment} `db.books.find( {"YEAR_WRITTEN":{$gte:1870, $lte: 1900}},{ _id:0} )`
* {:.fragment} __...and sort the result by author__
	* {:.fragment} `db.books.find( {"YEAR_WRITTEN":1900},{ _id:0} ).sort({"AUTHOR":1})`
* {:.fragment} __anything written exactly in 1870?__
	* {:.fragment} `db.books.find( {"YEAR_WRITTEN":1870},{ _id:0} ).sort({"AUTHOR":1})`
</section>

<section markdown="block">
## Operators

* {:.fragment} __books that cost $15 or more... or after 1899__
	<pre class="fragment"><code data-trim contenteditable>db.books.find(
	{ "$or": [ {"PRICE":{"$gte":15}},{"YEAR_WRITTEN":{"$gte":1900}}]})
</code></pre>
* {:.fragment} __same with author, title, year and price__
	<pre class="fragment"><code data-trim contenteditable>db.books.find(
	{"$or":[ {"PRICE":{"$gte":15}},{"YEAR_WRITTEN":{"$gte":1900}}]},
	{_id:0,"AUTHOR":1,"TITLE":1,"YEAR_WRITTEN":1,"PRICE":1})
</code></pre>
* {:.fragment} __now sort by author and title__
	<pre class="fragment"><code data-trim contenteditable>db.books.find(
	{ "$or":[ {"PRICE":{"$gte":15}},{"YEAR_WRITTEN":{"$gte":1900}}]},
	{_id:0,"AUTHOR":1,"TITLE":1,"YEAR_WRITTEN":1,"PRICE":1}
).sort({"AUTHOR":1,"TITLE":1})
</code></pre>
</section>

<section markdown="block">
## And More with Operators

__Show the title, author and year of all books written after 1870 by either Tolstoy or Woolf__ (sort by year) &rarr;

* {:.fragment} using or: 
	<pre class="fragment"><code data-trim contenteditable>db.books.find(
	{YEAR_WRITTEN: {$gt: 1870}, $or: [{AUTHOR: 'Woolf, Virginia'}, {AUTHOR: 'Tolstoy, Leo'}]}, 
	{_id: 0, TITLE: 1, YEAR_WRITTEN: 1, AUTHOR: 1}).sort({YEAR_WRITTEN: 1})
</code></pre>
* {:.fragment} using in: 
	<pre class="fragment"><code data-trim contenteditable>db.books.find(
	{YEAR_WRITTEN: {$gt: 1870}, AUTHOR: {$in: ['Woolf, Virginia', 'Tolstoy, Leo']}}, 
	{_id: 0, TITLE: 1, YEAR_WRITTEN: 1, AUTHOR: 1}
).sort({YEAR_WRITTEN: 1})
</code></pre>
</section>

<section markdown="block">
## Xtra: `$group`!

<pre><code data-trim contenteditable>
db.books.aggregate(
	[{$group : {
		_id: "$YEAR_WRITTEN", 
		books: {$push: "$TITLE"}
	}}]
)
</code></pre>

<pre><code data-trim contenteditable>
db.books.aggregate(
	[{$group : {
		_id: "$YEAR_WRITTEN", 
		books: {$push: "$TITLE"}, 
		price: {$avg: "$PRICE"}
	}}]
)
</code></pre>
</section>

<section markdown="block">
## Group

What was that??? [Let's see the docs on grouping](https://docs.mongodb.com/manual/reference/operator/aggregation/group/)...

* {:.fragment} `_id` is expression to group by... here we just use `$fieldname` to group by a field
* {:.fragment} `field` ...then an arbitrary number of fields that accumulate values using operators such as `$push` or `$avg`
* {:.fragment} [some examples of accumulator operators](https://docs.mongodb.com/manual/reference/operator/aggregation/group/#accumulators-group)


</section>

<section markdown="block">
## Practice

__Exploring wifi3.json__ &rarr;

First, import with: `mongoimport --db test --collection wifi --file /tmp/wifi3.json`

* {:.fragment} __how do we show databses?__
* {:.fragment} __how about switch databases?__ 
* {:.fragment} __how do list the collections?__
* {:.fragment} __how do list all of the documents in the collection?__
* {:.fragment} __let's show only the cities__
* {:.fragment} __show only the ones in the bronx__
* {:.fragment} __show only the ones that are free__ 
</section>

<section markdown="block">
## Practice Continued

__Now with moar operators!__ &rarr;

* {:.fragment} __show only the ones that are free and in flushing__ 
* {:.fragment} __are there any that are free and in the bronx?__ 
* {:.fragment} __show only wifi hotspots in the bronx ... or ones that are free?__ 
* {:.fragment} __that's a mess... let's limit output of the results to the fields city and type__
* {:.fragment} __now sort it by alphabetical order by city__
* {:.fragment} __...and now descending__
* {:.fragment} __how about... only in bronx or flushing, but without id__
* {:.fragment} __oookkkkk... not in bronx or flushing!?__
</section>



{% comment %}
{AUTHOR:"Tolstoy, Leo", YEAR:1800}
wifi
-----
* __how do we show databses?__
* __how about switch databases?__ switch to nyc
* __um...how do we know what we have?__
* __let's show only the cities__
	* db.wifi.find({}, {"CITY":1})
* __get only the ones in the bronx__
* __get only the ones that are free?__ 
* __get only the ones that are free and in flushing?__ 
* __are there any that are free and in the bronx?__ 
* __how about either in the bronx or price is free?__ 
	* db.wifi.find({"$or":[{"CITY":"Bronx"}, {"TYPE":"Free"}]})
* __how about either in flushing or price is fee based?__ 
* __that's a mess... let's limit the fields to city and type__
* __sort by alphabetical order by city__
* __descending__

wifi again
-----
* __only in bronx or flushing!?__
	* db.wifi.find({'CITY': {$in:['Flushing', 'Bronx']}})
* __only city, and keep id out of it puhleeze__
	* db.wifi.find({'CITY': {$in:['Flushing', 'Bronx']}}, {"CITY":1, "_id":0})
* __not in bronx or flushing!?__
	* db.wifi.find({'CITY': {$nin:['Flushing', 'Bronx']}}, {"CITY":1, "_id":0})


{% endcomment %}
