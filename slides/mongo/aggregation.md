---
layout: slides
title: "MongoDB Aggregation"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Example Data

__Using the [job postings data set](https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t) (sourced from the City of New York’s [official jobs site](http://www.nyc.gov/html/careers/html/search/search.shtml)), let's practice some aggregations__  &rarr;

* {:.fragment} bring the `csv` file into a collection named `jobs` in a database called `test` by using `mongoimport`;
* {:.fragment} you'll have to specify that it has a header line, that it's type is a csv, and where the import file is located
* {:.fragment} `mongoimport --headerline --type=csv --db=test --collection=jobs --file=./NYC_jobs.csv`

</section>

<section markdown="block">
## Explore the Sample Data

__Let's check out what we've imported__ &rarr;

* {:.fragment} get to the right collection
	```
use test
show collections
	```
	{:.fragment}
* {:.fragment} show the imported fields by displaying exactly one document 
	```
db.jobs.findOne()
	```
	{:.fragment}
* {:.fragment} how many documents are in the collection?
	```
db.jobs.find().count()
	```
	{:.fragment}
* {:.fragment} using [`db.collection.distinct(field)`](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/), find the distinct values for `Agency` and `Full-Time/Part-Time indicator`
	```
db.jobs.distinct('Agency')
db.jobs.distinct('Full-Time/Part-Time indicator')
	```
	{:.fragment}
	
</section>

<section markdown="block">
## Some More Exploration

__Some _warm up_ before getting into aggregation__ &rarr;

* {:.fragment} show the first three documents order by `Job ID` from least to greatest
	```
db.jobs.find().sort({'Job ID': 1}).limit(3).pretty()
	```
	{:.fragment}
* {:.fragment} using the previous query, only show the `Job ID`, `Agency`, and `Business Title`
	```
var fields = {_id: 0, "Job ID": 1, Agency: 1, "Business Title": 1};
db.jobs.find({}, fields).sort({'Job ID': 1}).limit(3).pretty();
	```
	{:.fragment}
* {:.fragment} use the same sort order and projection as above, but show all documents that have an `AGENCY` of `POLICE DEPARTMENT` (without limit)
	```
var filter = {Agency: "POLICE DEPARTMENT"};
db.jobs.find(filter, fields).sort({'Job ID': 1}).pretty();
	```
	{:.fragment}
</section>

<section markdown="block">
## Last Exercise 

__Show the top 20 jobs based on highest "to" salary (use `Salary Range To`)__ &rarr;

<pre><code data-trim contenteditable>
var fields = {
	_id: 0, 
	"Job ID": 1, 
	"Business Title": 1, 
	"Posting Date": 1, 
	"Salary Range To": 1};
var orderBy = {"Salary Range To": -1};
db.jobs.find({}, fields).sort(orderBy).limit(20).pretty();
</code></pre>
{:.fragment}

</section>



<section markdown="block">
## Aggregation

Like `GROUP BY` in relational databases and the `groupby` method in pandas, __MongoDB also supports performing aggregation functions on groups of data (documents instead of rows, of course!)__.

There are a few ways to do this in MongoDB:

1. {:.fragment} Aggregation Pipeline
2. {:.fragment} Single Purpose Aggregation Operations
3. {:.fragment} Map-Reduce

We'll focus on 1: the aggregation pipeline.
{:.fragment}

</section>

<section markdown="block">
## Aggregation Pipeline

__The aggregation pipeline is a multi-stage process that transforms documents into an aggregated result.__ &rarr;

* {:.fragment} the stages and order of execution are determined by the user
* {:.fragment} the output from one stage becomes the input for the next stage

To start an aggregation, call the `aggregate` function on a collection:
{:.fragment}

<pre><code data-trim contenteditable>
db.collectionName.aggregate(...)
</code></pre>
{:.fragment}

Pass in an Array containing a sequence of aggregation pipeline stages.
{:.fragment}

</section>

<section markdown="block">
## Aggregation Pipeline Stages Overview

__We'll use some of the following stages__ &rarr;

1. {:.fragment} `$match` - to filter documents
2. {:.fragment} `$count` - to count the number documents at this stage
3. {:.fragment} `$project` - to calculate or select fields
4. {:.fragment} `$group` - to group documents
</section>

<section markdown="block">
## Why Stages? 

__Looking at some of these stages, there's something that seems _redundant_ about some of these stages__ 😔 &rarr;

* {:.fragment} don't most of these stages have a counterpart already? 
	* `$match` is like query 
	* `$project` and `count` are like, _well_, project, and `.count`)
* {:.fragment} __however... these are stages in a pipeline of operations__ ...so they can be chained, repeated... and take advantage of aggregation / grouping!  🎆



</section>
<section markdown="block">
## Other Stages

__Additionally, there are more (perhaps not as _familiar stages)__: 
{:.fragment}

* {:.fragment} such as `$addFields` (similar to `$project`), `$bucket` (_binning values_),  and `$sample` (to select a random number of documents from its input) 
* {:.fragment} there are even your usual `$sort` and `$limit` (but for aggregation pipelines, of course)!
* {:.fragment} you can find a [full listing in the docs](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/).

</section>

<section markdown="block">
## "$fieldName" Syntax

⚠️ __You'll often see syntax that looks like this__ &rarr;

`"$fieldName"` - a field name prefixed with dollar, and quoted as a string

* {:.fragment} these dollar filed names represent the value at that `fieldName`
* {:.fragment} this syntax differentiates this from a hardcoded value...
* {:.fragment} for example `{fieldName: "foo"}` is different from `{fieldName: "$foo"}`
* {:.fragment} the first sets the value to exactly `"foo"`, but the second __sets the value to whatever is contained in the field named `foo`__


</section>

<section markdown="block">
## $match

__The `$match` operator filters documents__ &rarr;

* {:.fragment} acts like standard `find` query
* {:.fragment} similar to a combination of `HAVING` and `WHERE` in sql
* {:.fragment} value is query object

<pre><code data-trim contenteditable>
{$match: {city: "Brooklyn"}}
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## $count

__As the name implies, counts the number of documents incoming from the previous stage__ &rarr;

* {:.fragment} this actually acts a bit like `$group` and `$project` together, as we'll see those capabilities later)
* {:.fragment} value is the name of the new field that contains the count

<pre><code data-trim contenteditable>
db.jobs.aggregate([
  {$match: {"Business Title": "Policy Analyst"}}, 
  {$count: "countPolicyAnalysts"}
])
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## $project

__The [`$project` stage](https://docs.mongodb.com/manual/reference/operator/aggregation/project/) can modify the _shape_ of a document by adding, suppressing and calculating fields__ &rarr;

* {:.fragment} think of this as the `SELECT` list in sql (where you can choose columns, create calculated columns, etc.)
* {:.fragment} the value is a document that contains specifications for the transformations to be applied... it can contain:
	* `fieldName` or `_id`  as `1`, `true`, `0`, `false` for inclusion and suppression
	* `fieldName` as some expression

<pre><code data-trim contenteditable>
var fields = {_id:0, "Job ID": 1, "Business Title": 1};
db.jobs.aggregate([{$project: fields}])
</code></pre>
{:.fragment}

{% comment %}
comment_
{% endcomment %}
</section>

<section markdown="block">
## Some Operations
 
__Because a projection can result in a calculated fields there are a [large number of aggregation pipeline operators](https://docs.mongodb.com/manual/reference/operator/aggregation/) for manipulating strings, dates, performing simple arithmetic, etc.__ &rarr;

Some examples include:

* {:.fragment} [`$convert`](https://docs.mongodb.com/manual/reference/operator/aggregation/convert/) to convert from one type to another: `{$convert: {input: "$fieldName", to: "int"}}`
* {:.fragment} [`$split`](https://docs.mongodb.com/manual/reference/operator/aggregation/split/#exp._S_split) to break up a string into an array of substrings using _some_ delimiter: `{$split: ["$fieldName", ","]}`
* {:.fragment} [`$substrCP`](https://docs.mongodb.com/manual/reference/operator/aggregation/substrCP/#exp._S_substrCP) to extract a substring from another string by code point: `{$substrCP: ["$fieldName", 0, 4]} // first three characters`
</section>

<section markdown="block">
## More Operations, Expressions

__Additional operations... and expressions__ &rarr;

* {:.fragment} [`$add`](https://docs.mongodb.com/manual/reference/operator/aggregation/add/#exp._S_add), [`$subtract`](https://docs.mongodb.com/manual/reference/operator/aggregation/subtract/#exp._S_subtract), etc. ... `{$subtract: ["$field1", "$field2"]} // field1 - field2`
* {:.fragment} and [sooo may others, like `$toUpper`, `$trim`, `{$arrayElemAt: someArray, someIndex}`, etc.](https://docs.mongodb.com/manual/reference/operator/aggregation/)

Note that in most cases, the values can be arbitrary expressions that are: values at fields (`"$fieldName"`), a hardcoded value (`5`) or even the result of another operation (`{$op: [arg1, arg2}`)
{:.fragment}
</section>


<section markdown="block">
## `$project` Examples

__Uppercasing a field called business title__ &rarr;

<pre><code data-trim contenteditable>
var projection = {_id:0, "Job ID": 1, "title": {$toUpper: "$Business Title"}};
db.jobs.aggregate([{$project: projection}]);
</code></pre>
{:.fragment}

__Combining `$match` and `$project`: show jobs that have "External" `Posting Type` with a subset of fields__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
var projection = {
  _id:0, 
  "Job ID": 1, 
  ptype: "$Posting Type", 
  "title": {$toUpper: "$Business Title"}
};
db.jobs.aggregate([
	{$match: {"Posting Type": "External"}}, 
	{$project: projection}]);
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## A More Complicated `$project`

__Now let's try creating an arbitrary complex expression by nesting a split within an arrayElemenAt__ &Rarr;

The following breaks up the `Job Category` field and retrieves the first element
{:.fragment}

<pre><code data-trim contenteditable>
var extractFirstCat = {
  $arrayElemAt: [
    {$split: ["$Job Category", ","]}, 0
  ]
};
var projection = {_id:0, "Job ID": 1, 
  ptype: "$Posting Type", 
  "cat": extractFirstCat
};
db.jobs.aggregate([
  {$match: {"Posting Type": "External"}}, 
  {$project: projection}
]);
</code></pre>
{:.fragment}

{% comment %}
remove italics_
{% endcomment %}
</section>

<section markdown="block">
## $group

__The `$group` operator creates distinct groups as separate documents__ &rarr;

* {:.fragment} similar to `GROUP BY` in sql
* {:.fragment} value typically includes the field to group by and a new calculated field using an aggregate function:


<pre><code data-trim contenteditable>
// counts the number of documents per Agency
{$group: {
  _id: "$Agency", 
  listingCount: {$sum: 1}
}}
</code></pre>
{:.fragment}




{% comment %}
remove italics_
{% endcomment %}
</section>

<section markdown="block">
## $group Continued

__The fields in the value for `$group` are__ &rarr;

1. <code>_id</code> the field to group by  {% comment %}comment_ {% endcomment %}
	* ⚠️ the name of this field is __prefixed with a dollar__ sign and __quoted as a string__: `"$neighbourhood"`
	* this syntax references the _value_ in a field from the original document
2. any number of additional fields in the document
	* each field potentially has an accumulator operation:`$sum`, `$avg`, `$max`, `$last`, `$push` 

</section>

<section markdown="block">
## Accumulator Operators

__There's a [long list of accumulator operators](https://docs.mongodb.com/manual/reference/operator/aggregation/group/#accumulators-group)__ ....you'll notice the similarities between these and their corresponding aggregate functions in sql:

* {:.fragment} `$sum`: "$fieldName" / value - sums the values in fieldName
* {:.fragment} `$avg`: "$fieldName" / value - calculate the mean of the values in fieldName
* {:.fragment} `$max`: "$fieldName" / value - finds the max value in fieldName
* {:.fragment} `$last`: "$fieldName" / value - gives the last fieldName value in group
* {:.fragment} `$push`: "$fieldName"

</section>

<section markdown="block">
## $match Details

__Unlike sql `SELECT`, the order of the stages in a call to `aggregate` can be specified! 😲__ &rarr;


* {:.fragment} try to place `$match` operations earlier... __why__ &rarr;
* {:.fragment} $match reduces the total number of documents to be processed 
* {:.fragment} which means that later stages won't have to deal with large volumes of documents!

</section>


<section markdown="block">
## Match

__Make a simple aggregation pipeline that acts like find to filter such that the minimum `Salary Range From` in our results is $200,000__ &rarr;

<pre><code data-trim contenteditable>
var min_from = {$match: {"Salary Range From": {$gt: 200000}}}
db.jobs.aggregate([min_from])
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Match and Project

__For all positions that are paid annually (see `Salary Frequency`), show the top 10 positions that have the largest range of possible salaries__ &rarr;


<pre><code data-trim contenteditable>
var salaryGap = {$subtract: [
  "$Salary Range To", "$Salary Range From"]};
var fields = {$project: {
  _id: 0, "Business Title": 1, "Salary Gap": salaryGap}};
var annualExternal = {$match: {
  "Salary Frequency": "Annual", 
  "Posting Type": "External"
}};
var sortGapDesc = {$sort: {"Salary Gap": -1}};
db.jobs.aggregate([
  annualExternal, fields, sortGapDesc, {$limit: 10}]);
</code></pre>
{:.fragment}

{% comment %}
comment_
{% endcomment %}
</section>

<section markdown="block">
## Match, Project, and Match

__Same as previous: all positions that are paid annually (see `Salary Frequency`), show the difference between start and to salaries... but this time, only show the positions where the difference is lower than $5,000, but not 0__ &rarr;



<pre><code data-trim contenteditable>
var salaryGap = {$subtract: [
  "$Salary Range To", "$Salary Range From"]};
var fields = {$project: {
  _id: 0, 
  "Business Title": 1, 
  "Salary Gap": salaryGap}};
var annualExternal = {$match: {
  "Salary Frequency": "Annual", 
  "Posting Type": "External"}};
var maxDiff = {$match: 
  {"Salary Gap": {$lt: 5000, $gt: 0}}};
db.jobs.aggregate([
  annualExternal, fields, maxDiff]);
</code></pre>

{% comment %}
comment_
{% endcomment %}
</section>


<section markdown="block">
## Group by Agency

__Let's see the average each city agency pays for the low end of the salary range for `Career Level` "Entry-Level", without showing agencies with an average lower than $30,000__ &rarr;

hint: eliminate groups, like `HAVING` by using a `$match`
{:.fragment}

<pre><code data-trim contenteditable>
var matchEntryLevel = {$match: {"Career Level": "Entry-Level"}};
var avgSalaryAgencyGroup = {
	$group: {"_id": "$Agency", avgSalaryFrom: {$avg: "$Salary Range From"}}
};
var match30K = {$match: {avgSalaryFrom: {$gte: 30000}}};
db.jobs.aggregate([matchEntryLevel, avgSalaryAgencyGroup, match30K]);
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Group by Year

__Let's see how many jobs were posted for every year__ &rarr;

<pre><code data-trim contenteditable>
var extractYear = {$arrayElemAt: [{$split: ["$Posting Date", "/"]}, -1]};
var fields = {$project: {year: extractYear}};
var countByYear = {$group: {_id: "$year", count: {$sum: 1}}};
var orderByYear = {$sort: {_id: -1}};
db.jobs.aggregate([fields, countByYear, orderByYear]);
</code></pre>
{:.fragment}



</section>

{% comment %}
db.jobs.find({}, {_id: 0, "Job ID": 1, "Business Title": 1, "Posting Date": 1, "Salary Range From": 1}).sort({"Posting Date": -1}).limit(5).pretty()
{% endcomment %}
{% comment %}
<section markdown="block">
## Example Data

__Using "scraped" `listings` data from [insideairbnb.com](http://insideairbnb.com/get-the-data.html), we can practice some aggregations__  &rarr;

* {:.fragment} download the latest `listings` for New York City
* {:.fragment} `mongoimport --headerline --type=csv --db=test --collection=reviews --file=./listings.csv`
* {:.fragment} note `--headerline`  (don't need a separate headers file)
* {:.fragment} also, database and collection are `test` and `reviews` 

</section>


<section markdown="block">
## Example Query 

__Count the number of listings per neighborhood, not in the city of Brookyln. Exclude counts less than 10.__

<pre><code data-trim contenteditable>
db.reviews.aggregate([ 
	{$match: {city: "Brooklyn"}}, 
	{$group: {_id: "$neighbourhood", listingCount: {$sum: 1}}}, 
	{$match: {listingCount: {$lt: 10}}}
])
</code></pre>

</section>
{% endcomment %}
