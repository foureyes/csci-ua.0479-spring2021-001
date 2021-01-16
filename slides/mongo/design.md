---
layout: slides
title: "Data Modeling in MongoDB"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Designing a Document Database

__When working with a relational database, we saw that normalization helped__:

1. {:.fragment} reduce insert, update, and delete anomalies
2. {:.fragment} _extend_ or expand the database with minimum impact on existing design
3. {:.fragment} in general, make the database easier to understand

Keeping these design goals in mind, let's see how we can achieve this with a document database like MongoDB... &rarr;
{:.fragment}


</section>
<section markdown="block">
## Defining Relationships / Data Models

In relational databases, __referential integrity__ between two tables is maintained via __foreign key constraints__. __In Mongo DB, however...__  &rarr;

* {:.fragment} we'll likely still _want_ documents to be related to each other in some way, but we don't have foreign keys 😲!
* {:.fragment} instead, in MongoDB, relationships between documents can be set up by: &rarr;
	1. embedding (that is, one document contains one or more other documents)
	2. linking (...one document references another document by id)

</section>

<section markdown="block">
## Embedded Documents

__Instead of having two separate documents, we may have one _sub-document_ (or sub-documents) embedded in another:__

Assume that a movie has the following fields: 

* {:.fragment} `title` (Blue Velvet) 
* {:.fragment} `year` (1986)
* {:.fragment} `directorFirstName` (David)
* {:.fragment} `directorLastName` (Lynch)

__Try to model a movie with one or more documents.__ &rarr; 
{:.fragment}
</section>

<section markdown="block">
##  Using Embedded Documents to Handle a One-to-One Relationship

__Here's example of a one-to-one relationship implemented as an embedded document:__ &rarr;

* {:.fragment} a `movie` document...
* {:.fragment} with a `director` document embedded within it

<pre><code data-trim contenteditable>
{
  title: "Blue Velvet",
  year: 1986
  director: {
    first: "David",
    last: "Lynch"
  }
}
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Another Scenario

__Let's create a document database for a web site that allows users to post images and captions to images__ &rarr;

We'll store the following data in our document database:

* {:.fragment} a `username` (memelord3000)
* {:.fragment} the `path` to an image (puppers.png)
* {:.fragment} a `caption` for the image (who's a good boi?)
* {:.fragment} there can be any number of paths and captions associated with a username

__What would a sample document look like?__ &rarr;
{:.fragment}

</section>

<section markdown="block">
##  Modelling a One-to-Many with Embedded Documents

__This relationship can be modeled by embedding several `post` documents in an `Array` within a `user` document__ &rarr;

<pre><code data-trim contenteditable>
{
  username: "memelord3000"
  posts: [
    {path: "ok.jpg", caption: "OK!"},
    {path: "puppers.png", caption: "Who's a good boi?"}
  ]
}
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Compared to Relational Databases

__Embedded documents give some sembelance of maintaining a consistent relationship between documents__ 

However...

* {:.fragment} the embedded documents aren't required to have the same fields
* {:.fragment} there's a possibility of duplicating data

</section>

<section markdown="block">
## One-to-Many Continued

__Let's try to model the following data about schools and students: one school to many students__ &rarr;

* {:.fragment} `schoolName` (New York University)
* {:.fragment} `city` (New York)
* {:.fragment} `first` (Meredith)
* {:.fragment} `last` (Memelord)
* {:.fragment} `major` (Meme Posting)
</section>

<section markdown="block">
## One-to-Many - Which to Embed?

__Because we have one school to many students, we _could_ embed student documents into a school document...__ &rarr;


<pre><code data-trim contenteditable>
{
  schoolName: "NYU",
  city: "New York",
  students: [
    {first: "Beth", last: "Boolean", major: "CS"},
    {first: "Alice", last: "Algo", major: "CS"},
    {first: "Ben", last: "Bio", major: "Biology"}
    // so many more...
  ]
}
</code></pre>
{:.fragment}

__That seems like _a lot_ of embedded documents, no?__
{:.fragment}
</section>

<section markdown="block">
## One-to-Many - Embedding Continued

__An alternative is to store a `school` document in a `student` document__ &rarr;

<pre><code data-trim contenteditable>
{ 
  first: "Beth", 
  last: "Boolean", 
  major: "CS",
  school: {name: "NYU", city: "New York"}
}
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
{ 
  first: "Ben", 
  last: "Bio", 
  major: "Biology",
  school: {name: "NYU", city: "New York"}
}
</code></pre>
{:.fragment}

__Buuuut, what might be an issue here?__  <span class="fragment">Duplicate data for school</span>
{:.fragment}
</section>

<section markdown="block">
## Many-to-Many

__Can many-to-many be implemented using embedded documents? For example, can a many-to-many relationship between `movies` and `documents` be modeled?__ &rarr;

* {:.fragment} YES 👍
* {:.fragment} ... but you'll have duplicate data

<pre><code data-trim contenteditable>
{
	title: 'Blue Velvet'
	actors: ['Laura Dern', 'Dennis Hopper', ...]
}
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
{
	title: 'Wild at Heart'
	actors: ['Laura Dern', 'Nicolas Cage', ...]
}
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## References

__An alternative to embedding is using references (linking by id)__

* {:.fragment} this is similar to a foreign key, but there are _no actual_ constraints (an id can point to a non-existent document) 
* {:.fragment} the earlier example of a `student` document containing and embedded `school` document can be re-designed to use references instead
* {:.fragment} (this is a bit familiar, as it mimics the _normalized_ data models that we created with relational databases)

{:.fragment}

</section>

<section markdown="block">
## References Example

__Here is our `student` and `school` documents... related with references rather than embedding__ &rarr;

<pre><code data-trim contenteditable>
{ 
  first: "Ben", 
  last: "Bio", 
  major: "Biology",
  school_id: 23
}
{  
  _id: 23,
  name: "NYU", 
  city: "New York"
}
</code></pre>
{:.fragment}

{% comment %}
remove italics_
{% endcomment %}

</section>
<section markdown="block">
## References and Many-to-Many

__How might many-to-many relationships be modeled in a document database?__ &rarr;

* {:.fragment} documents in two separate collections may have references to each other
* {:.fragment} the references are stored in an `Array`

<pre><code data-trim contenteditable>
{ // a single movie document
  _id: 1
  title: "Blue Velvet"
  actors: [27, 39, 103, ...]
}
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
{ // a single actor document
 _id: 27	
 first: "Laura",
 last: "Dern",
 movies: [1, 300, 301, ...]
}
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## How to Join?

__🕵️ ... So how do we get referenced documents... for example, if we want all of the names of the actors in "Blue Velvet"__ &rarr;

__Typically, references to other documents are resolved simply by issuing multiple successive queries__ &rarr;
{:.fragment}

* {:.fragment} get a set of documents with `find`
* {:.fragment} use the ids in those documents to get related documents with another call to `find`

<pre><code data-trim contenteditable>
var m = db.movies.findOne({title: "Blue Velvet"});
db.actors.find({_id: {$in: m.actors}});
</code></pre>
{:.fragment}

Note that as of MongoDB 3.2 (~2015), the `$lookup` aggregate operator is available to mimic a left outer join.
{:.fragment}

{% comment %}
remove italics_
{% endcomment %}
</section>



<section markdown="block">
## Use Embedded

__What are some use cases for embedded documents?__ &rarr;

* {:.fragment} contains relationship: one-to-many or one-to-one
* {:.fragment} fast reads are important / read performance is a priority
	* {:.fragment} documents and collections are typically contiguous on disk
	* {:.fragment} number of database queries are reduced (no joins)
* {:.fragment} perhaps fewer updates (update related data in single operation)?
</section>

<section markdown="block">
## When to Avoid Embedded Documents

__Of course, using embedded documents is not always the best solution. You may want to avoid sub-documents if__ &rarr;

* {:.fragment} maybe u don't want everything at once! (high bandwidth)
* {:.fragment} you're trying to model complex relationships __and__ avoid redundant data

</section>

<section markdown="block">
## Use References

__References use cases__ &rarr;

* {:.fragment} many to many
* {:.fragment} want to reduce redundant data (and performance gain from embedding is not important)
* {:.fragment} need full query access to related document

But...
{:.fragment}

* {:.fragment} as u no... such complexity!
* {:.fragment} more queries
* {:.fragment} referential integrity must be enforced by the application (since the db won't do it 4 u! 🤷)
</section>

<section markdown="block">
## Normalized vs Non-normalized

__Finally, why use MongoDB (or any document store) over a relational database__ &rarr;

* {:.fragment} ease of use
* {:.fragment} incredibly flexible data model
* {:.fragment} rapid read performance
* {:.fragment} horizontal scaling is easier 
* {:.fragment} (adding more servers instead of investing in a single large server)

Some downsides:
{:.fragment}

* {:.fragment} lack of constraints (um... this is what makes it easy to use, tho... and constraints can be added in application layer)
* {:.fragment} no transactions (because some data can be modeled as embedded, a single atomic operation _can_ work on documents and sub-documents)
</section>
