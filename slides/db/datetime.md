---
layout: slides
title: "Date and Time"
---

<script src="../../resources/js/table.js"></script>
<link rel="stylesheet" href="../../resources/css/data-table.css" type="text/css" media="screen" title="no title" charset="utf-8">


<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## SQL and Date/Time

Check out the [postgres docs](https://www.postgresql.org/docs/current/functions-datetime.html) for full details on manipulating dates and times.

In this set of slides, we'll cover:

1. {:.fragment} creating and retrieving dates
2. {:.fragment} extracting parts of a date
3. {:.fragment} show a couple of examples of date and time arithmetic

</section>

<section markdown="block">
## Data Source for Examples

Again, _adverse_ food events data: [CAERS](https://www.fda.gov/food/compliance-enforcement-food/cfsan-adverse-event-reporting-system-caers)

1. slides use 2014-2019 reports
2. [documentation of fields](https://www.fda.gov/media/97035/download)
3. sample data:

* {:.header} Report ID, CAERS Created Date, Date of Event, Product Type, Product, Product Code, Description, Patient Age, Age Units, Sex, MedDRA Preferred Terms, Outcomes
* 172940, 1/1/2014, , SUSPECT, DANNON DANNON LITE & FIT GREEK YOGURT CHERRY, 09,  Milk/Butter/Dried Milk Prod, , , , NAUSEA, Other Outcome
* 175277, 4/7/2014, 3/15/2013, SUSPECT, CHIA PLUS COCONUT CHIA GRANOLA, 05,  Cereal Prep/Breakfast Food, 15, year(s), F, BURNING SENSATION, Other Outcome
{:.fragment}
{:.table}

Some fields, such as `MedDRA`, contain comma separated lists.
{:.fragment}

</section>


<section markdown="block">
## Creating / Retrieving Current

* {:.fragment} `make_date(year, month, day)` &rarr; `date`
* {:.fragment} `make_time(hours, minutes, seconds)` &rarr; `time` (without timezone)
* {:.fragment} `make_timestamptz(year, month, day, hours, minutes, seconds)`; &rarr; `timestamp with timezone`
* {:.fragment} `current_date` &rarr; current `date`
* {:.fragment} `current_time` &rarr; current `time` (no timezone)
* {:.fragment} `current_timestamp` or `now()` 
	* both give back `timestamp with timezone`
	* in the context of a transaction, this time is when the transaction started

</section>
<section markdown="block">
## Extracting Parts

__If a column is a `date` or `timestamp`, individual parts of it can be extracted using `date_part__ &rarr;

* {:.fragment} `date_part(part_of_date, col_name)`
* {:.fragment} `part_of_date` is a string: `year`, `month`, `day`, `hour`, `minute`, `seconds`
	* note that `month` will give back 1 through 12
* {:.fragment} for example, to retrieve only the year from `event date`


<pre><code data-trim contenteditable>
select 
	product, description,
    date_part('year', event_date) as year,
    date_part('month', event_date) as month
from caers_event;
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Arithmetic

__Simple arithmetic can be performed with the usual operators: `+`, `-`, `*`, and `/`.__ &rarr;

* [the functionality of these operators depends on the operands](https://www.postgresql.org/docs/current/functions-datetime.html#OPERATORS-DATETIME-TABLE)
* {:.fragment} some common usage:
	* subtracting two dates yields days: `select '2019-01-05'::date - '2019-01-01'::date`;
	* (note that you can get negative results here)
	* adding an `integer` to a `date` adds days: `select '2019-01-05'::date + 35;
`

</section>

<section markdown="block">
## Arithmetic Practical Example

From our dataset, we can find out what __the average number of days is between an event occurring, and it being created in the database__ &rarr;

<pre><code data-trim contenteditable>
select round(avg(created_date - event_date), 0) as lag 
from caers_event 
where created_date > event_date;
</code></pre>
{:.fragment}

(note, there are some outliers that likely skew this calculation!)
{:.fragment}
</section>
