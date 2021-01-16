---
layout: slides
title: "Data Formats on the Web"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Markdown, HTML, XML, JSON

We've done _a lot_ of work with `csv` data, and it translates well to tabular data. However most data on the web is hierarchical: `html`, `xml`, and `json`. While simple `csv` files can be parsed by hand (or by `pandas`!)...  

__You don't want to mess with `html`, `xml`, and `json` on your own. It's actually quite difficult to get exactly right.__ &rarr;
{:.fragment}

* {:.fragment} some liken it to dealing with Lovecraftian elder gods!
* {:.fragment} [check out the classic stack overflow answer](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)
* {:.fragment} it also likely means you'll have to use lots of complicated regular expressions
* {:.fragment} [...and, of course, regular expressions: now you have two problems](http://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)

</section>

<section markdown="block">
## So How Do We Even?

__Find someone that already went through the pain of doing it, and use their library__.

* {:.fragment} again, html is difficult to parse
* {:.fragment} find an html parser already built for you
* {:.fragment} for example you can use [beautiful soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to easily find elements within an html document using some simple methods
* {:.fragment} some other libraries for parsing html:
	* {:.fragment} [scrapy](https://scrapy.org/) - specialized for scraping data off of web-pages
	* {:.fragment} [requests-html](https://html.python-requests.org/) - simple api built by author of popular library, `requests`


</section>


<section markdown="block">
## Beautiful Soup 4

Here's a quick demonstration of how BeautifulSoup works...

<pre><code data-trim contenteditable>
from bs4 import BeautifulSoup

dom = BeautifulSoup("""
&lt;html&gt;
&lt;body&gt;
&lt;h1&gt;foo&lt;/h1&gt;
&lt;p&gt;bar
&lt;h1 class='even-headier'&gt;baz&lt;/h1&gt;
&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
""", "lxml")
</code></pre>
<pre><code data-trim contenteditable>
print(dom.select('h1'))
print(dom.select('.even-headier'))
</code></pre>
</section>

<section markdown="block">
## Beautiful Soup 4

__Here's a quick demonstration of how BeautifulSoup works...__ &rarr;

1. {:.fragment} First, start off with installation:
    * use PyCharm to install `beautifulsoup4`
2. {:.fragment} Then... the usual import
    * `from bs4 import BeautifulSoup`

This gives you a __constructor__ that you can use to create an object that represents an __html document__. Just pass an html string to it...
{:.fragment}

</section>

<section markdown="block">
## BeautifulSoup Constructor

__Note the 2nd argument determines what you'll use to _parse_ the html__ (html.parser should be fine) &rarr;

<pre><code data-trim contenteditable>
dom = BeautifulSoup("""
&lt;html&gt;
    &lt;body&gt;
        &lt;h1&gt;foo&lt;/h1&gt;
        &lt;p&gt;bar
        &lt;h1 class='even-headier'&gt;baz&lt;/h1&gt;
        &lt;a href='http://cs.nyu.edu'&gt;cs!&lt;/a&gt;
        &lt;/p&gt;
    &lt;/body&gt;
&lt;/html&gt;
""", "html.parser")
</code></pre>


</section>

<section markdown="block">
## Beautiful Soup Continued

Now... __you can use css selectors to retrieve specific html elements... by using the `select` method!__ &rarr;

<pre><code data-trim contenteditable>
# get the elements with class .even-headier
print(dom.select('.even-headier'))

# get all h1's ... show the text of the first one
print(dom.select('h1')[0].get_text())

# show the href attribute of the first link
print(dom.select('a')[0]['href'])
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## JSON

Aaaand. Lastly, JSON. __Use the <code>json</code> module to convert to and from Python dictionaries and JSON strings__ &rarr;

<pre><code data-trim contenteditable>
import json
# dumps <-- creates a string from a python dict... as json format
# loads <-- reads a string into a python dict (assuming string is json)

s = '{"first":"joe", "last":"versoza"}'
d = json.loads(s)
print(d)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Pandas and JSON

__Of course, you can also use `pandas` to work with `json`:__ &rarr;

To create a `DataFrame` from a `json` string:
{:.fragment}

<pre><code data-trim contenteditable>pd.read_json('[{"city": "Ithaca", "state": "NY"}, 
	{"city": "Atlanta", "state": "GA"}]')
</code></pre>
{:.fragment}

Keys are columns, but they can be adjusted using the `orient` keyword argument 
{:.fragment}

* {:.fragment} [check the docs for _sooo many options_](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html) 
* {:.fragment} (for example, `orient=split` will expect separate keys for `index`, `columns` and `data`)
</section>

<section markdown="block">
## Nested JSON

__What do you think will happen here?__ &rarr;

<pre><code data-trim contenteditable>
s = '''
  [{"title": "Dune", 
    "author": {"first": "Frank", "last": "Herbert"}}, 
   {"title": "Handmaid\'s Tale", 
    "author": {"first": "Margaret", "last": "Atwood"}}]
'''
pd.read_json(s)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
                                    author            title
0    {'first': 'Frank', 'Last': 'Herbert'}             Dune
1  {'first': 'Margaret', 'last': 'Atwood'}  Handmaid's Tale
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Nested JSON Continued

__How do we _flatten_ the json?__ &rarr;

* {:.fragment} by hand (this. is. going. to. be. ugly.):
	<pre class="fragment"><code data-trim contenteditable>
[{'title': d['title'], 
  'first': d['author']['first'], 
  'last': d['author']['last']} for d in json.loads(s)]
</code></pre>
* {:.fragment} oh yeah, pandas can do that
	<pre class="fragment"><code data-trim contenteditable>
from pandas.io.json import json_normalize
json_normalize(json.loads(s))
</code></pre>
	<pre class="fragment"><code data-trim contenteditable>
# ✨
  author.first author.last            title
0        Frank     Herbert             Dune
1     Margaret      Atwood  Handmaid's Tale
</code></pre>
{:.fragment}

</section>



