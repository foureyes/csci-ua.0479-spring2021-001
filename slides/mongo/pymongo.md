---
layout: slides
title: "Python and MongoDB"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Python + MongoDB 

__[PyMongo](https://pypi.org/project/pymongo/) is a python module that enables interaction with a MongoDB database via Python.__ &rarr;

* its [API resembles that of that commandline client](https://pymongo.readthedocs.io/en/stable/index.html), so running basic queries should be feel familiar.
* to install `pip3 install pymongo`


</section>

<section markdown="block">
## MongoClient

An [instance of `MongoClient`](https://api.mongodb.com/python/current/api/pymongo/mongo_client.html) will allow you to connect to a MongoDB database:

<pre><code data-trim contenteditable>
from pymongo import MongoClient
client = MongoClient('mongodb://localhost')
</code></pre>
{:.fragment}

* {:.fragment} this will connect to an instance of MongoDB running on the standard port, 27017
* {:.fragment} port can be specified after the hostname: `hostname:port` 
* {:.fragment} making a connection is blocking... a script will not continue until after connection
* {:.fragment} a failed connection will cause a server timeout exception
* {:.fragment} [keyword arguments can be passed to the constructor](https://api.mongodb.com/python/current/api/pymongo/mongo_client.html)
* {:.fragment} returns a client from which you can use databases and collections

</section>

<section markdown="block">
## Database, Collection

__Databases and collections can be accessed as attributes of an instance of `MongoClient`__ &rarr;

<pre><code data-trim contenteditable>
db = client.test # database is test
db.jobs # jobs collection
</code></pre>
{:.fragment}

From the collection, you can call queries that you're familiar with, like [`find`](https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find), `find_one`, and [`aggregate`](https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.aggregate).
{:.fragment}

Note the nomenclature and naming convention favors underscores rather than camelcase: `findOne` is `find_one` in `pymongo`
{:.fragment}
</section>

<section markdown="block">
## Find Example

[Working with job postings from New York City](https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t)...

__Find all postings where the `Agency` is `"DEPT OF PARKS & RECREATION"` and upper bound for salary is more than $30,000__

<pre><code data-trim contenteditable>
res = db.jobs.find({
    "Agency":"DEPT OF PARKS & RECREATION",
    "Salary Range To": {"$gt": 30000}
})

for r in res:
    print(r["Agency"], r["Business Title"], r["Salary Range To])
</code></pre>
{:.fragment}

Note that access to result document values is by _dictionary-style_keys_ (rather than using dots and attributes)
{:.fragment}
</section>


<section markdown="block">
## Aggregate Example

__Using `aggregate` on our collection, count the number of positions per agency that are hourly... order by most positions first__ &rarr;

Use `Salary Frequency` and `# Of Positions` to do this
{:.fragment}

<pre><code data-trim contenteditable>
sal_freq_filter = {"$match": {"Salary Frequency": 'Hourly'}}
group_by = {"$group": {
  "_id": "$Agency", 
  "count_pos": {"$sum": "$# Of Positions"}
}}
order_by = {"$sort": {"count_pos": -1}}
having = {"$match": {"count_pos": {"$gt": 100}}}
result = db.jobs.aggregate([sal_freq_filter, group_by, order_by])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
for r in result:
    print(r)
</code></pre>
{:.fragment}
</section>
