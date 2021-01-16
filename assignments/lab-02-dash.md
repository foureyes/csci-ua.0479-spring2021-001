---
layout: homework
title: "Lab #02 / Homework #7"
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

# Lab #02 / Homework #07 - Dash, PyMongo, MongoDB Atlas - Due In-Class



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

* +60% - attending
* +20% - submitting queries
* +10% - attempting pymongo
* +10% - attempting visualization

__Submission__

⚠️ Submit by using the form at the end of the instructions.

## Part 1: Setup, Cloud MongoDB, Queries

### MongoDB Atlas

1. [Create an account (can use throw-away email if u want!))[https://www.mongodb.com/download-center] by filling in the `Try MongoDB in the Cloud` form
2. Choose a cloud provider and region; any provider will work, but choose a region in North America, and click on `Create Cluster`
	* this will take a little while, so you may want to take the time to prep other other steps
3. Add your IP Address
4. Add a user (remember your password!)

### Load Sample Data

1. Download the September 2019 New York City `listings.csv.gz` from [insideairbnb](http://insideairbnb.com/get-the-data.html)
	*
2. In MongoDB Atlas (the admin site for your MongoDB Atlast), click on ellipses the `...` underneath Cluster and choose `Commandline Tools`
3. Click on `Copy` underneath Data Import (it should start with `mongoimport`
4. Paste the command in terminal/cmd/powershell... replace the parts with angle brackets with appropriate values (make sure there are no angle brackets left-over) and add `--headerline` at the end
	* use `lab02` as the database name
	* use `listings` as the name of the collection
	* if you're using windows, you may have to go into the `bin` folder of your mongodb install to run `mongoimport.exe`

### Query Sample Data

1. In MongoDB Atlas, click on `Connect` (if there is no Button, click on cluster in the navigation panel)
2. Choose `Connect with the MongoDB Shell`... and then `Copy`
3. Paste into terminal/cmd/powershell
4. Use client to run the following queries... __save both the query and the first two lines of the result in a text file__:
	1. show exactly two documents from the `listings` collection in any order
	2. show all of the listings hosted by either "Kamilla" or "Sonder"
		* only show the `name`, `price`, `neighbourhood`, and `host_name`
	3. find all the unique `host_name` ([see the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))
	4. find all of the places that have more than 2 `beds` in `city` Brooklyn, ordered by `review_scores_rating` descending
		* only show the `name`, `beds`, `city`, `review_scores_rating`, and `price`
		* if you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`)... and lastly, if there's still an issue, you can set beds to exactly 2
	5. show the number of listings per host
	6. in `city`, New York, find the average `review_scores_rating` per `neighbourhood`, and only show the ones above a 95... sorted in descending order of rating ([see the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/))

## Part 2: pymongo and Dash

### Setup

Install the following libraries to connect to mongodb with Python and to create a web visualization of your data

```
pip3 install dash
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

## Submit the Lab

Turn in the lab at the end of class using this form:

[https://docs.google.com/forms/d/e/1FAIpQLSekgbADmp2eaO3EtI_pRRZFmibV5Rnalyi1UN1e4iky05dc_A/viewform](https://docs.google.com/forms/d/e/1FAIpQLSekgbADmp2eaO3EtI_pRRZFmibV5Rnalyi1UN1e4iky05dc_A/viewform)
