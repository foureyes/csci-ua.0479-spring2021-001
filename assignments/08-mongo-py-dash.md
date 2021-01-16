---
layout: homework
title: "Homework #8"
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

# Homework #08 / _In-Class_ Group Project - SQLAlchemy, MongoDB, PyMongo - Due 5/1 at 11pm

__Overview__

In this lab, you'll:

1. Work with SQLAlchemy's ORM to:
	1. Create classes that represent tables in your database
	2. Create _actual_ tables in the database (without writing any SQL!)
	3. Insert rows into the tables that you created (without writing any SQL!)
	4. Read some data from the tables (without writing any SQL!)
2. Try out MongoDB
	1. Import csv data into MongoDB
	2. Run a few queries on the resulting dataset through MongoDB
3. Try out PyMongo


__Submissions__

* work in groups of 2 or 3
	* make sure that you all have postgres and mongodb
* ⚠️ submit by using the form at the end of the instructions

## Part 1: SQLAlchemy

### Requirements

Create classes to represent a person and the social networks that they belong to.  The classes should support the following usage:

1. Inserting data by:
	```
ig = SocialNetwork(name="Instagram", url="instagram.com")
yt = SocialNetwork(name="YouTube", url="youtube.com")
p1 = Person(first_name='Alice', last_name='Alvarez', birthday=datetime(1998, 9, 10))
p1.social_networks = [ig]
p2 = Person(first_name='Bob', last_name='Burke', birthday=datetime(1996, 7, 8))
p2.social_networks = [ig, yt]
session.add_all([p1, p2])
session.commit()
```
2. Querying and printing a person's social networks by:
	```
bob = session.query(Person).filter(Person.first_name == 'Bob').one()
print(bob)
for sn in bob.social_networks:
    print(sn)
# Burke, Bob - born 1996
# Instagram (instagram.com)
# YouTube (youtube.com)
```
3. Querying and printing a social network's members by:
	```
ig = session.query(SocialNetwork).filter(SocialNetwork.name == "Instagram").one()
print(ig)
for m in ig.members:
    print(m)
# Instagram (instagram.com)
# Alvarez, Alice - born 1998
# Burke, Bob - born 1996
```

### General Workflow and Testing

1. Create classes
2. Generate tables with `Base.metadata.create_all(engine)`
3. Create instances 
	* see sample code in usage section
	* don't forget to call `session.commit()` to save to database
4. Query for instances
	* see sample code in usage section
5. Copy and paste __classes only__ into submission form (do not include import and setup to avoid sending your database username and password)

### Hints

1. Import and setup:
	<pre><code data-trim contenteditable>from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
</code></pre>
	<pre><code data-trim contenteditable>dsn = 'postgres://YOURUSERNAME:YOURPASSWORD@localhost/DATABASENAME'
</code></pre>
	<pre><code data-trim contenteditable>engine = create_engine(dsn)
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()
</code></pre>
2. Use [the docs on many-to-many relationships](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html), paying special attention to the `backref` keyword argument to `relationship`
3. Use [strftime](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) to extract the year from a date

## Part 2: MongoDB Data Import, Queries

### Load Sample Data

1. Download [the latest `listings.csv.gz` data for __New York City__](http://insideairbnb.com/get-the-data.html)
	* Make sure the data that you're using is __New York City__ (there are several cities listed)
2. Extract the data (on Windows 10, you may need 7-zip, winzip, etc.)
3. In terminal/cmd.exe/powershell,  use `mongoimport` to bring in the json data
4. Use `homework08` as the database and `listings` as the collection name
	* if you're using windows, you may have to go into the `bin` folder of your mongodb install to run `mongoimport.exe`

### Query Sample Data

Use the `mongo` commandline client to run the following queries... __save both the query and the first two lines of the result in a text file__:

1. show exactly two documents from the `listings` collection in any order
2. show exactly 10 documents in any order... but print in easier to read format and noting the host names for further use
3. choose to host names... and show all of the listings hosted by either of the two hosts (for example, "Kamilla" or "Sonder"... though these two names may not exist in the _latest_ data set)
	* only show the `name`, `price`, `neighbourhood`, and `host_name`
4. find all the unique `host_name` ([see the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))
5. find all of the places that have more than 2 `beds` in `city` Brooklyn, ordered by `review_scores_rating` descending
	* only show the `name`, `beds`, `city`, `review_scores_rating`, and `price`
	* if you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`)... and lastly, if there's still an issue, you can set beds to exactly 2
5. show the number of listings per host
6. in `city`, New York, find the average `review_scores_rating` per `neighbourhood`, and only show the ones above a 95... sorted in descending order of rating ([see the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/))

## Part 3: pymongo 

### Setup

Install the following libraries to connect to mongodb with Python and to create a web visualization of your data

```
pip3 install pymongo
pip3 install dnspython
```

### pymongo

1. in a file called `test.py`...
2. [use the docs](https://api.mongodb.com/python/current/tutorial.html) and the Connect string for Python in MongoDB Atlas to set up a connection to your database
3. reproduce one of your earlier queries:
	* find all of the places that have more than 2 `beds` in `city` Brooklyn, ordered by `review_scores_rating` descending
	* only show the `name`, `beds`, `city`, `review_scores_rating`, and `price`
	* note that in pymongo, you'll have to quote all of your keys!

{% comment %}
### dash

1. in a file called `app.py`, copy and paste this code:
	<pre><code data-trim contenteditable>
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Example'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [go.Bar(x=['label1', 'label2', 'label3'], y=[5, 1, 7])],
            'layout': {
                'title': 'Bar Chart'
                }
            }
        )
    ])
if __name__ == '__main__':
    app.run_server(debug=True)
</code></pre>
2. (this is kind of tricky!) ... use pymongo to show the top 10 most expensive neighbourhoods based on average price of listings with 2 bedrooms... in a bar chart
	* you'll likely have to use the following operators:
		* [$project](https://docs.mongodb.com/manual/reference/operator/aggregation/project/) to select or calculate fields
		* [$reduce](https://docs.mongodb.com/manual/reference/operator/aggregation/reduce/), [$split](https://docs.mongodb.com/manual/reference/operator/aggregation/split/), and [$concat](https://docs.mongodb.com/manual/reference/operator/aggregation/concat/) to remove commas by splitting and joining again with concat
		* [$substrBytes](https://docs.mongodb.com/manual/reference/operator/aggregation/substrBytes/), [$strLenBytes](https://docs.mongodb.com/manual/reference/operator/aggregation/strLenBytes/), and [$subtract](https://docs.mongodb.com/manual/reference/operator/aggregation/subtract/) to remove dollar sign
		* [$convert](https://docs.mongodb.com/manual/reference/operator/aggregation/convert/) to convert to a double
{% endcomment %}

## Submit the Lab

Turn in the homework at the end of class (or by 11pm edt) using the form below:

* ⚠️you must be logged in to your NYU google account to see the form
* ⚠️every group member must submit their own form!

[https://forms.gle/Wc42RkcicZCZ65QK7](https://forms.gle/Wc42RkcicZCZ65QK7)

	

