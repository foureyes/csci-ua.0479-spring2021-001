---
layout: homework
title: "Assignment #5"
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

# Assignment #5 - Database Design, Joins - Due Thursday, Nov 7th  at 11pm

In this homework, you'll:

1. Use "business" requirements to build a database 
	1. Create an ER Diagram 
	2. Write CREATE table statements 
	3. Write queries against the tables created
2. Normalize the data from previous assignments and store it in a database
	1. Normalize the data from previous assignments (or find a new data source)
	2. Create an ER diagram representing the normalized data
	3. Create the tables to support the ER diagram
	4. Import and clean the data using SQL
	5. Write queries against the imported data

## Part 1: Use "business" requirements to build a database

To save some money 💰, instead of taking an Uber/Lyft/Taxi all over the city, you and a bunch of friends decide to buy a pool of electric scooters to share!

Other students find out about your scooter scheme, and want to join in 🙌! You rent out a small store front to be the base of your _Scoot Share_ ... where people can go to to borrow or return a scooter (for a small hourly fee), 24 hours / day 🌞🌔! Now you have to keep track of an ever-growing fleet of electric scooters __and__ who's borrowed them. 

### Here's how your _Scoot Share_ works:

1. A person comes into your store to borrow a scooter...
2. You take down their name, contact information, and when they first entered your store
	* for contact information, you simply need a way to get in touch with them in case you need to track down an unreturned scooter or a damaged scooter, so the following are required:
		* email address
		* cell phone 
		* home address
	* keep track of both date and time for when they first entered / gave you their information
3. If they've borrowed a scooter before, you can just retrieve all of their previous information from the first time they borrowed a scooter
4. If they already have a scooter borrowed, but that they haven't returned it, then they can't borrow anothers scooter
5. If they've been referred by someone else that had previously borrowed a scooter, make sure to take note of that 
	* it's adequate to simply know who referred who; no additional information has to be kept about a referral
	* of course, someone can come it without having been referred
6. Then... they choose a scooter to borrow from your inventory of available scooters
	* the scooters vary, with differences in:
		* manufacturer
		* the manufacturer's country
		* model number
		* range (in kilometers)
		* weight (in kilograms) 
		* top speed (in kilometers/hour)
		* condition (new, slightly used, used)
	* you can have multiple scooters that have the same manufacturer and model number
6. They can pre-pay to borrow a scooter for a set number of hours
	* it's important to note when they actually borrow a scooter
	* and, of course, when they need to return it
	* ... and how much they paid
7. They give you their payment information so that you can charge them for the hours they book and charge them additional fees if they return the scooter late or damaged (note that you don't keep track of this on your own - you use a 3rd party service so you don't have to deal with any credit card number storage regulations)
8. When they return the scooter...
	* keep track of when it was returned
	* and determine if the return is late or not, and check for damages
	* ... add any additional fees for damage / late return as separate line items associated with the borrow / return
9. An arbitrary number of _freeform_ text notes can be added to when a person borrows a scooter
	* these notes can be used to indicate issues that come up while the scooter is being used or when it's returned (for example, the scooter may not meet its stated max range while it's out... or the scooter may be returned with handle grips missing)
	* in addition to the text, notes can be categorized as: return condition, malfunction, or other
10. Lastly, you should be able to _flag_ a user as someone that has had issues in the past

Because you're an SQL _expert_ 🤓, you decide to store all of this information in a database! 

⚠️ See [the "Write Some SQL" below](#write-some-sql) to get an idea of what queries you'd be running against this database. ⚠️


### Create an ER Diagram and write SQL to Make Tables

1. ✏️ Based on the description above, create an ER Diagram (chen, crow's foot, or even uml) to model the data
	* there are multiple ways to model the scenario described, and there are clearly __ambiguities__ in the description
	* you can use any diagramming tool to create your diagram: 
		* we used [pgmodeler](https://pgmodeler.io) in class, but you have to compile it if you want it for free (it's not the _easiest_ thing to do, but you can also get the paid version if you think you'll be using this software beyond this class)
			* you have to write your own SQL for the creation scripts (but of course, you can check against this generated sql)
		* although geared towards mysql, you can use [MySQL Workbench](https://www.mysql.com/products/workbench/)
		* you can also use non-database specific tools like:
			1. [draw.io](https://www.draw.io/) (you can start with "Software" --&rarr; "Entity Relationship", the last diagram type)
			2. use google drawings and copy symbols from [this document](https://docs.google.com/drawings/d/1hcTNp5IlnJXxLWDx5f8mptMLYDKqnJLt5fKgP4aP8e8/edit) (which sourced its symbols from [ER Diagram Symbols](https://docs.google.com/drawings/d/1IIQ6ftgPqG082JRTW7-cBzXAi_BdxrBmEncQeQETzJk/edit))
			3. Visio
			4. [Dia](http://dia-installer.de/), or any other drawing application
		* ⚠️⚠️⚠️ __see the next section, "Write Some SQL", as some of those queries may inform your design decisions__
	* ⚠️ __regardless of what tool you use, you must export to an image or pdf__ 
2. 🔑 __Use natural primary keys when possible__, but surrogate / artificial keys are ok too if the other natural keys may end up changing
3. 👀 Avoid data redundancy and update / insert/ delete anomalies by making sure your data model is minimally in 3rd normal form
4. 🤝 __maintain relational integrity and use constraints to enforce this__ 
5. 🖼 Export this as an image (any format is ok) called `er-diagram.png` (change extension appropriately)
6. Embed the image under a heading called `Scoot-Share` in your `README.md`
7. __Below the image, describe:__ 
	* your design decisions for the relationships between tables
		* if there are tables that aren't in 3rd normal form, please point them out
		* describe why you did not normalize further ...or if there are any issues that would come up due to that design decision
	* any assumptions you had to make due to the ambiguities in the description above
8. Create a a file called `part-1-scoot-share-create.sql` that contains SQL for creating all of the tables that you've modeled
9. Add a link from your `README.md` to `part-1-scoot-share-create.sql`


<a name="write-some-sql">

### Write Some SQL!

If it's relevant for your paricular data model, check out the documentation on:

* [Date/Time Types](https://www.postgresql.org/docs/current/datatype-datetime.html)
* [Date/Time Functions and Operators, such as NOW(), &gt;, etc.](https://www.postgresql.org/docs/current/functions-datetime.html)

In a file called `part-1-scoot-share-queries.sql`:

1. List all people (names are adequate) that have flags in any order
2. List all available scooters in any order
3. List all scooters (scooter model and manufacturer, along with person's name... and when they're due back) that are being borrowed in order of when they're due back ordered by when whey were due increasing (that is, earlier ones appear first, and more recent ones appear later)
4. List all scooters (scooter model and manufacturer, along with person's name) that are being borrowed and that are late in any order
5. List the top 5 people (names and number of referrals) that have the most referrals sorted by most referrals descending
6. Given a unique identifier for a person, show all of the times that person has borrowed a scooter in chronological order (from the first time they borrowed a scooter to the most recent)
7. Given a unique identifier for a particular instance of a person borrowing a scooter, show all of the damage / late related fees 
8. List all of the manufacturers of scooters in your database, __even if you don't currently have any of their scooters in your inventory__

Add a link to `part-1-scoot-share-queries.sql` in your `README.md`

## Part 2: Normalize the data form previous assignments....

1. Use the data that you've worked on in previous assignments or find a new data set:
	* create at least two tables with a foreign key relationship based on this data
	* make sure that the resulting tables are minimally in 3rd normal form
	* create a file called `part-2-normalization-create.sql`
2. Import the data into the two tables
	* you can use any method to do this
	* ...from using only SQL
	* ...to using a combination of SQL and Python (with any libraries you'd like to use)
	* save any sql or Python that you've written into a file called `part-2-normalization-import.sql` or `part-2-normalization-import.py` (or both!)
	* save the original data source an any intermediary transformations
3. Write the following queries and __describe what they do in a comment__... all within `part-2-normalization-queries.sql`:
	1. a query that involves an inner join
		* use a comment to describe the query
	2. a query that involves an outer join (left, right or full)
		* use a comment to describe the query
	3. a query that involves an inner join and an aggregate function
		* use a comment to describe the query

Under a heading called `Normalization`, add links to your:

* create statements sql
* original data and transformed/cleaned data (if relevant)
* import scripts (SQL and/or Python)
* queries

## Conclusion

At the end of the homework, your `README.md` should look like the following (with parts marked `TODO` replaced with your own written content)

```
# Homework 05

## Scoot-Share

![er diagram for scoot share](er-diagram.png)

* TODO: a list of design decisions
* TODO: a list of assumptions

Scripts

* [part-1-scoot-share-create.sql](part-1-scoot-share-create.sql)
* [part-1-scoot-share-queries.sql](part-1-scoot-share-queries.sql)

## Normalization

* [part-2-normalization-create.sql](part-2-normalization-create.sql)
* [part-2-normalization-import.sql](part-2-normalization-import.sql)
* [part-2-normalization-queries.sql](part-2-normalization-queries.sql)
```
