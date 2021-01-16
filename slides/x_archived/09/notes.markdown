
<section markdown="block">
## Homework

* lists
    * changing in place
    * creating new
    * not using all functions in module
* permutations / requests
    * guess the passwords
    * multi stage proc
    * get a bunch of words and filter
        * filter so that you only have:
        * words >= 14, stars with v or h, has two s's and one o
    * make every combo
    * write to a file

</section>

<section markdown="block">
## File I/O Review

* __opening__ and __closing__
* reading a file
* methods for reading
    * iterate
    * read
    * readlines
    * readline (call consecutively)
* writing to a file

</section>

<section markdown="block">
## Using a Context Manager

__Always close__ your file when you're done working with it... but what if there's an exception? <code>try/except/finally</code> works... but <code>with</code> is better. It'll automatically close any time the with expression's block is exited!

<pre><code data-trim contenteditable>
with expression as variable
    use variable
</code></pre>

<pre><code data-trim contenteditable>
with open('myfile.txt') as f:
    for line in f:
        print(line)
</code></pre>
</section>


<section markdown="block">
## File Formats

We're reading text files for now. They can come in a multitude of formats. __Why do we care?__ &rarr;

Format determines how we extract meaningful data from a file.
{:.fragment}

Yeah... great, reading files is fun and all, but it's all just a bunch of nonsense if we don't know how it's formatted, right? __What are some common text file formats?__ &rarr;

* _just text_ ... like files from project gutenberg / no standard format
* __csv__ or value separated (can have other delimiters!)
* __fixed width__
* __markdown__
* __html__
* __xml__
* oh... also json
</section>

<section markdown="block">
## Ok... How do We Deal With Diff Formats?


* text ... just read it in, that's about as good as you can do
* __csv__, split (or...)
* __fixed width__, slice maybe?
* __markdown__, uh-oh
* __html__, uh-oh
* __xml__, uh-oh
* oh... also json

We'll need to bring in some more robust tooling for those last 3.

</section>

<section markdown="block">
## The Problem With csvs

csvs seem fine. That is until... __What's tricky about using split with csvs?__ &rarr;


sometimes pesky commas are legit characters
{:.fragment}

Wait, did you know there's actual an [RFC for CSVs (like a _standard_ specification for what CSV actually is)](https://tools.ietf.org/html/rfc4180.html)
{:.fragment}
</section>

<section markdown="block">
## csv module

Ok... that seems complicated enough. Let's not write that ourselves. That's where the csv module comes in.

1. Basically... you create a reader object
2. And you just loop over it
3. Each row is a list of strings (regardless of content)
4. CSV MODULE FTW! (commas in quotes, no problem)

[Actually some more docs on this](https://docs.python.org/3/library/csv.html#module-contents)

* can specify the _dialect_
* change delimiter
* change quote char, etc.
</section>

<section markdown="block">
## csv

<pre><code data-trim contenteditable>
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        print(row[0])
</code></pre>
</section>

<section markdown="block">
## Wanna Get Fancy, Do Ya?

How about reading those rows as dictionaries instead? First row is considered the keys (they should be the headers, right?).

<pre><code data-trim contenteditable>
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        print(row['pace'])
</code></pre>
</section>

<section markdown="block">
## Fixed Width

Ok... slicing seems like it's no problem. Right? NBD.

Writing though has one minor problem. What is it?

* {:.fragment} some fields may have to be truncated (shortened, with the excess part being lopped off!)


</section>

<section markdown="block">
## Markdown, HTML, XML

You don't want to mess with these on your own. It's kind of difficult.

Some liken it to messing with Lovecraftian elder gods!

[Classic so answer](http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)


</section>

<section markdown="block">
## So How Do We Even?

Find someone that already went through the pain of doing it, and use their library.

For HTML, a commonly use library is beautiful soup 4:

[bs4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)


</section>


<section markdown="block">
## 

<pre><code data-trim contenteditable>
from bs4 import BeautifulSoup

dom = BeautifulSoup("""
<html>
<body>
<h1>foo</h1>
<p>bar
<h1 class='even-headier'>baz</h1>
</p>
</body>
</html>
""", "lxml")
headers = dom.select('h1')
print(headers)
for h1 in headers:
    print(h1.contents)
    print(h1.string)
    print(str(h1.string))

</code></pre>



</section>

<section markdown="block">
## Where Data is Sourced From

* locally (on your file system)
    * use open
* remotely... on some other server
    * use requests
    * or urllib
        * download first
        * or read directly as string


</section>

<section markdown="block">
## Which to Use and When for Remote

Download or read directly from server?

* too big?
* changes often?
* want to not hit api sooooo often

</section>

<section markdown="block">
## JSON

<pre><code data-trim contenteditable>
res = requests.get("http://data.nba.com/data/15m/json/cms/noseason/game/20160221/0021500824/boxscore.json")

j = res.json()
</code></pre>
</section>

http://ichart.yahoo.com/table.csv?s=AAPL
<section markdown="block">
## 
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code

r.headers['content-type']
lication/json; charset=utf8'
r.encoding
-8'
r.text

</section>


<section markdown="block">
## Creating an Image

<pre><code data-trim contenteditable>
from PIL import Image

img = Image.new( 'RGB', (255,255), "black") # create a new black image

pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 100) # set the colour accordingly

img.show()
</code></pre>

</section>

<section markdown="block">
## Turn this wallaby black and white?

<pre><code data-trim contenteditable>
img = Image.open('wallaby.jpg')

</code></pre>
</section>
