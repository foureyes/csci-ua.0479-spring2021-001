---
layout: homework
title: "Assignment #6"
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
</style>
<script>
document.addEventListener('DOMContentLoaded', hideHints);

function hideHints(evt) {
    document.querySelectorAll('.hint').forEach((ele, i) => {
        const div = document.createElement('div');
        div.id = 'hint' + i + 'Button';
        ele.id = 'hint' + i;
        ele.classList.add('hidden');
        div.addEventListener('click', onClick);
        div.textContent = 'Show Hint';
        div.className = 'hintButton';
        ele.parentNode.insertBefore(div, ele);
    });

}

function onClick(evt) {
    const hintId = this.id.replace('Button', '');
    const hint = document.getElementById(hintId);
    hint.classList.toggle('hidden');
    this.textContent = this.textConent === 'Show Hint' ? 'Hide Hint' : 'Show Hint';
}
</script>

# Assignment #6 - Due Monday, November 25th at 11pm


In this homework, you'll:

1. Bring csv data into postgresql and create a normalized data model representing the data
2. Create and populate new tables to hold the original data
3. Run queries against your new tables

## Part 1: Import and Data Model

### Download / Documentation

Download and read documentation about the .csvs linked to from [the FDA CAERS website](https://www.fda.gov/food/compliance-enforcement-food/cfsan-adverse-event-reporting-system-caers):

* Download the most recent file...
* [2014 - 2019](https://www.fda.gov/media/128562/download)
* Read the [documentation about the fields contained in these files](https://www.fda.gov/media/97035/download)

### Create a Staging Table

Write a short `.sql` script to create a temporary staging table called `staging_caers_events` to store the data from both .csvs. This will house your initial data import, but you'll eventually create new tables to store this same data.

* In `part1-01-create-staging.sql`...
* Write a `DROP TABLE IF EXISTS staging_caers_events` statement
* Then write a `CREATE TABLE staging_caers_events` with appropriate columns
	* The types can be loose... for example, using `text` rather than `varchar`; you can fix these later
	* 👀 It will be __extremely__ helpful to immediately add an artificial primary key to the rows right on import 
	* If you need some help with this, [you can grab the `CREATE` statement from the slides on conditionals](../slides/db/conditionals.html) (just make sure the table name being created is prefixed with `staging_`
* Finally, in `part1-02-import.sql` add a `COPY` statement that actually adds the data to the staging table from the downloaded csv

### Exploring the Data

In `part1-03-explore.sql` write at least 4 sql statements to explore the data that you have to:

* Reveal how columns may be related to each other
* View the kinds of values that exist in each field
* Determine what column or combination of columns provide unique values / candidate keys

Write statements and comments in `part1-02-explore.sql`, and document their output in `report.md`

* Add a comment above each query describing what the query is trying to achieve.  <pre><code data-trim contenteditable>-- 2. this query tries to determine whether or not report id is unique	
YOUR QUERY UNDERNEATH;
</code></pre>
* In `report.md`:
	* Under a header called `## Exploring Data`...
	* Paste the output of each query; try to limit the queries to under 10 rows (or truncate what you've pasted), and be judicious about which columns you include
		* If you're using DataGrip to do this, then you'll have to:
			1. go to the upper right of the markdown window
			2. click on the dropdown to the left of the down and up arrow icons
			3. select `Markdown-Groovy.md.groovy`
			4. copy the output table
			5. paste into `report.md`
			6. for example, the clipboard may contain (which should render as a markdown table):
				```
| term | count\_term |
| :--- | :--- |
| FOO | 20169 |
| BAR | 6520 |
| BAZ | 5837 |
```
		* Of course, if using psql, you can simply copy and paste from the commandline into a markdown code black (fence with 3 backticks)
	* Write a sentence interpreting the results of your queries underneath the pasted output (in `report.md`)

### Normalization, ER Diagram 

Using the results of your data exploration, as well as the documentation ont he data set...

Create an ER Diagram showing a normalized data model to store the same data in the staging table.

* Each table must be in third normal form
* Some design decisions are based on _your_ interpretation of the data, so there may be multiple solutions
* For practicality, allow nulls where appropriate despite what some resources dictate for normalization

The ER digaram can be created in any tool that you'd like.

* Export it to an image (`png`, `jpg`, etc.)
* Add the image to your repository
* Underneath a header `## Database Design`, show the image in your `report.md` using markdown
* Underneath the image, add an unordered list in markdown that describes some of your design decisions

## Part 2: Creating New Tables and Populating Them

### Creating New Tables

Your data model should eventually lead you to the following __entities__ and relationships:

1. `caers_event`
2. `symptoms` (or `terms`)
3. `product`

* A product may have many events associated with it
* An event may be related to many symptoms
* A symptom can occur in many vents

If your model does not have these entities, then add some rationale to your ER Diagram documentation to explain your design decisions.

⚠️ __Regardless of your ER diagram, use the entities above to come up with the appropriate number of `CREATE` statements__. Although there are __only 3 entities listed, there may be more than 3 tables__:

* In `part2-01-create.sql`, add your `CREATE` table statements
	* Try to use types that best capture the _actual_ data as seen from the staging table
	* Prior to each `CREATE` statement, add a `DROP TABLE IF EXISTS tablename`
* Run your create statements; you should have at least 3 tables (as there are only that many entities)... again, to correctly convert these entities to tables, you may have to create additional table(s)
* Try rerunning everything in `part2-01-create.sql` again - all at once - to confirm that tables are _actually_ dropped

### Populating New Tables

In `part2-02-populate.sql`, using only SQL, populate the tables that you created.

The entire `sql` file should contain all of the queries necessary to use the data from your `staging_caers_table` to the other tables created. 

* Prior to each set of queries, add a comment specifying which table is being populated
* Additionally, if there are queries that are complex, add a comment explaining what the query is meant to do

⚠️ __All of the queries in this file should be executable in the order that they appear to produce populated tables__.

Some __important hints__:

* `TRIM` and `UPPER` will be very helpful in normaling names
* Using the artificial id in your staging table will be __very__ helpful
* The [`UNNEST` function](https://www.w3resource.com/PostgreSQL/postgresql_unnest-function.php) might be helpful if you want to turn an Array into a list
	* Combine this with `string_to_array`, and you can turn a string delimited by a character into multiple table rows
	* Alternatively [`regex_split_to_table`](https://www.postgresql.org/docs/9.1/functions-string.html) can do the same thing in a single function call
* You'll definitely be using a lot of `INSERT` statements with subqueries

## Part 3: Queries

Finally, once you've created and populated your tables, write queries in  `part3-queries.sql`, create queries based on the specifications below. The query specifications are divided into two groups: Views and Index and General Queries. For each set of specifications under each group:

* Prior to each query, write out the number of the query you're implementing in a comment.
* In a markdown code block copy and paste the results. If you're using DataGrip, make sure to choose markdown as the copy format (similar to the first part)

### Views and Index

You may want to come back to this part after you've warmed up with some queries.
1. __Add an index on a column...__ 👉
	* come up with a query (one that returns a small number of rows works best)...
	* add `EXPLAIN` and `EXPLAIN ANALYZE` queries to your sql file
		* document the results in `report.md`
	* add an index on column that you think may help the query run more quickly 
	* again, add `EXPLAIN` and `EXPLAIN ANALYZE` queries to your sql file
		* again, document the results in `report.md`... but this time add a sentence describing if the index "worked" and why (or why not!)
2. __It's been pretty annoying continually joining on product or symptoms...__ 👓
	* create a view that reconstitutes the original staging table
	* query the view to show a few columns and rows
	* the total number of rows in the view should be the same as your staging table (or at least nearly the same)
		* if you're off, or if there are some parts you can't reconstitute...
		* in `report.md` describe why you think your results may be inconsistent with the original table

### General Queries

⚠️ __Do 5 out of 8 of these in order__. Any additional queries will be counted as extra credit towards homework.

1. __How afraid should you be of yogurt?__ 🙀
	* list the product name and patient age of all incidents that involved yogurt
	* only include events that have an actual patient age in years
	* sort the results by the patient's year age from oldest to youngest
	* only show the first 5 results
	* it's ok to hardcode strings that help your query filter for a product name _like_ yogurt and an age that's in years
	* ... but don't hardcode any other values
	* hint: some kind of join may be useful here
2. __Find the name and product code of all of the products (no duplicates) that give you nightmares__ 😱
	* again, it's ok to hardcode the part of your query that searches for nightmares
	* do not hardcode anything else, though
	* only show the first 5 results
	* hint: there's probably a lot of joins involved in this one!
3. __Show a comma separated list of symptoms / terms for every event__ 📝
	* include the artificial key of the event and the list of terms order by the key ascending and show only 5 results
	* for example: 
		* id: `123`
		* symptoms: `DIZZINESS,RASH,FEVER`
	* hint: [`string_agg`](http://www.postgresqltutorial.com/postgresql-aggregate-functions/postgresql-string_agg-function/) may be useful here
	* hint: `group by` may also be helpful
4. __Create a list of event dates, report ids and product, regardless of whether or not there's a product name__ ☑️
	* sort by the report id ascending
	* for all events in september of 2013
5. __The date of most recently entered event(s)__ 📅 
	* this is actually two queries:
		1. find the date of the most recently entered event(s) (there can be more than 1)
    	2. then display the report id, product name, and the date of the most recently entered event(s)
	* do not hardcode a limit
	* hint: a subquery may be useful for the second query
6. __Find the event that had the most symptoms (there could be a tie)__ 🤒
	* show the primary key for the event, the created date, event date, product, description, patient_age, sex, and all symptom terms, along with the count of symptoms
	* do this for all non exempt products (`EXEMPT 4`)
7. __What are the 3 most common symptoms__ 🤮 
	* include the name of the symptom and the count 
	* sorted by the count from greatest to least
	* as secondary sort order, sort in alphabetical order of the name of the symptom
8. __Find the incident reported that dealt with the youngest patient__ 👶
	* show the report id, age, product and product code (associated with the youngest person)
	* create a function to help do this
	* normalize dates as we did in class / in the slides
	* if there's more than one person, show the details for each event per person

### Conclusions

Lastly, under a `## Conclusions` header in `report.md`, write a few sentences that discuss:

1. why this semi-normalized form is better
2. why this semi-normalized form is worse / difficult to use?

\* for each, give at least 1 practical example...

{% comment %}
Requirements
-----
* X create tables
* X specify action on delete (cascade for example)
* X do you _really_ need a separate table for each patient
* X trim is really useful
* X consider immediately giving an id on initial import
* you should be able to reconsitute the original table with a view
	* but no more insert, update, and delete anomalies
	* possible to query into something like terms
* unnest may be helpful to create a table
* trim on a table works!?
* union, except, intersect
* there are some unexpected issues with the data in terms of uniqueness

* duplicate terms in same cell
* casing and spacing issues
* some products have same name, but different product code
{% endcomment %}
