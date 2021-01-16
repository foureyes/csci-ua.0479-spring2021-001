---
layout: slides
title: "Conditional Expressions"
---

<script src="../../resources/js/table.js"></script>
<link rel="stylesheet" href="../../resources/css/data-table.css" type="text/css" media="screen" title="no title" charset="utf-8">


<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Data Source for Examples

_Adverse_ food events data: [CAERS](https://www.fda.gov/food/compliance-enforcement-food/cfsan-adverse-event-reporting-system-caers)

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
## CREATE

<pre><code data-trim contenteditable>
drop table if exists staging_caers_event;
create table staging_caers_event (
	-- artificial primary key
    caers_event_id serial primary key,
	-- note that there are dup report_id's
    report_id varchar(255),
    created_date date,
    event_date date,
    product_type text,
    product text,
    product_code text,
    description text,
    patient_age integer,
    age_units varchar(255),
    sex varchar(255),
    terms text,
    outcomes text);
</code></pre>

</section>

<section markdown="block">
## Import

<pre><code data-trim contenteditable>
copy staging_caers_event (
	report_id, created_date, event_date,
	product_type, product, product_code,
	description, patient_age, age_units,
	sex, terms, outcomes)
    from '/path/to/CAERSASCII 2014-20190331.csv'
    (format csv, header, encoding 'LATIN1');
</code></pre>
</section>

<section markdown="block">
## A Closer Look at Patient Age

If we want query sorted by oldest to youngest, we _might_ use a simple `ORDER BY` &rarr;

<pre><code data-trim contenteditable>
select * from caers_event order by patient_age;
</code></pre>
{:.fragment}

Easy enough! __But wait... a closer look at age shows us there are two age related columns__ &rarr;
{:.fragment}


* {:.header} Patient Age, Age Units
* 15, year(s)
* null, null 
* 72, year(s)
* 16, month(s)
{:.fragment}
{:.table}



</section>


<section markdown="block">
## Patient Age and Age Units

__A patient's age can be in different units:__ &rarr;

<pre><code data-trim contenteditable>
select distinct age_units from caers_event;
</code></pre>
{:.fragment}

...shows us that the possible values for `age_units` are: `year(s)`, `month(s)`, `day(s)`, and `null`.
{:.fragment}

Additionally, we can see that if we have `null` value for `age_units`, then `patient_age` must be `null` too:
{:.fragment}

<pre><code data-trim contenteditable>
select patient_age, age_units from caers_event where age_units is null and patient_age is not null;
</code></pre>
{:.fragment}

One way to sort by age with age unit taken into account is to __normalize the patient age to some unit__. We'll do this with simple numeric operations rather than date/time, and we won't handle leap years. 
{:.fragment}

</section>

<section markdown="block">
## Naive Patient Age Normalization

__As mentioned in the previous slide, we can simply normalize to a unit:__ &rarr;

* {:.fragment} let's make everything years:
* {:.fragment} if the column is `month(s)`, divide `patient_age` by 12
* {:.fragment} if the column is `day(s)`, divide `patient_age` by 365

However, to do this, we'll need to perform a calculation conditionally based on the value of another field. __SQL supports conditional expressions to achieve this__ ...
{:.fragment}
</section>

<section markdown="block">
## CASE

`CASE` is like an `if` statement in other languages. The general syntax is: &rarr;

<pre><code data-trim contenteditable>
CASE WHEN condition_1 THEN result_1
  WHEN condition_2 THEN result_2
  ELSE result_default
END
</code></pre>
{:.fragment}

* {:.fragment} `CASE` can be used anywhere an expression is valid (`SELECT` list, `WHERE` clause, etc.)
* {:.fragment} `condition` is a boolean expression
* {:.fragment} `result_*` is the value that the expression evaluates to
* {:.fragment} there can be one or more `WHEN`/`THEN` pairs
* {:.fragment} `ELSE` is optional
* {:.fragment} as always, whitespace can be added for readability
</section>
<section markdown="block">
## Order By Normalized Age

__And now for our _actual query_.__ &rarr;

<pre><code data-trim contenteditable>
select product, terms, CASE
    WHEN age_units like 'year%' THEN patient_age
    WHEN age_units like 'month%' THEN round(patient_age:: decimal / 12, 2)
    WHEN age_units like 'day%' THEN round(patient_age:: decimal / 365, 2)
    ELSE null
END AS age, patient_age, age_units
FROM caers_event
WHERE patient_age is not null
ORDER BY age DESC;
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Dates

__There are two dates associated with our event data...__ (from the CAERS readme) &rarr;

1. {:.fragment} `created_date`: The date on which the data were first entered into CAERS from an adverse event report.
2. {:.fragment} `event_date`: The reported date on which the consumer
first experienced the adverse event.

We can see that `created_date` is always present, while only just under 40% of events recorded have an _actual_ `event_date`: 
{:.fragment}

<pre><code data-trim contenteditable>
-- (without subqueries)
select count(*) from caers_event where created_date is null;
select count(*) from caers_event where created_date is not null;

select count(*) from caers_event where event_date is null;
select count(*) from caers_event where event_date is not null;
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Assigning a Date 

__Perhaps you want to have _some sort of date_ assigned to an event, even if it's a year off (!)__ &rarr;

Let's see what happens if we examine the relationship between the `event_date` and `created_date` a little further to determine if this is possible...

<pre><code data-trim contenteditable>
-- were all entries created after the event occurred?
select * from caers_event where event_date > created_date;
</code></pre>
{:.fragment}

Seems like this database can predict the future! 🔮
{:.fragment}

<pre><code data-trim contenteditable>
--  what's the largest difference in days between these two dates?
select max(event_date - created_date) from caers_event;
</code></pre>
{:.fragment}

Still under a year 😅.
{:.fragment}

</section>

<section markdown="block">
## `COALESCE`

If we want to use either date, we have to __choose the first one that's not null__. The `COALESCE` function lets us do this:

* it can be given an arbitrary number of arguments
* it gives back the first non-null argument 
* ...or `null` if all of the arguments are `null`
* `SELECT COALESCE(null, '🐘', '🐍')`
{:.fragment}

In our case we could use `COALESCE` to use `event_date`, but fall back to `created_date`:
{:.fragment}

<pre><code data-trim contenteditable>
select 
	description, 
	coalesce(event_date, created_date) as created_or_event 
from caers_event;
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## An Aside on Ordering

__Let's try ordering by `patient_age` descending__ &rarr;

<pre><code data-trim contenteditable>
select patient_age, age_units from caers_event order by patient_age desc;
</code></pre>
{:.fragment}

Uh... it looks like it orders `null` values first!? 😐
{:.fragment}

* {:.fragment}`null` values are sorted last when ascending
* {:.fragment}`null` values are sorted first when descending

</section>

<section markdown="block">
## Two Ways to Solve This

__If you want `null` values sorted last even when order by is descending...__ &rarr;

* {:.fragment} `NULLS LAST`
	<pre><code data-trim contenteditable>
select patient_age, age_units from caers_event order by patient_age desc nulls last;
</code></pre>
* {:.fragment} use `COALESCE`
	<pre><code data-trim contenteditable>
select patient_age, age_units from caers_event order by coalesce(patient_age, 0) desc;
</code></pre>
	* this is particularly useful if you want to assign a specific value to what otherwise would have been `null` for the purposes of ordering

</section>
<section markdown="block">
## `NULLIF`

`NULLIF` is a function that...

* {:.fragment} can take two values as arguments...
* {:.fragment} it gives back `null` if two values are equal
* {:.fragment} otherwise, it returns only the first value
* {:.fragment} `select nullif(1, 1)` &rarr; `null`
* {:.fragment} `select nullif(1, 0)` &rarr; `1`

But y tho? 🤔
{:.fragment}

* {:.fragment} useful to mark a value as missing (`null`) if it has some _other_ value that _should_ be treated as null
* {:.fragment} treat the string, `N/A`, as `null`: `nullif(col_name, 'N/A')`


</section>
