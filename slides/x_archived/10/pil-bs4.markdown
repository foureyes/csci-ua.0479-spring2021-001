---
layout: slides
title: "PIL, IO, Requests, DOM/HTML/CSS, BS4"
---


<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Whew - That's a lot of Tiny Acronyms

__Let's try to put together a bunch of stuff that we've learned to make some _art_ (maybe?)!__ 

__We'll try combining the images of all of the cast of a movie__ (the results will be kind of meh, but it's the _fun_ in the process that really matters!)

First will need to further explore and/or review:

1. __PIL__ - __we know this__ - Python Imaging Library
2. __IO__ - Python module for dealing with text, binary and raw input and output 
3. Requests - Making some HTTP requests!
4. DOM/HTML/CSS
5. __BS4__ - Beautiful Soup

</section>

<section markdown="block">
## PIL Can do Some Things

I'm a terrible person for making everyone manually manipulate pixels, when __a lot of what we just did is available as built in functionality in PIL__ &rarr;

* resize
* thumbnail
* filter
* transpose
* point operations
* paste
{:.fragment}

</section>

<section markdown="block">
## Filter


__<code>img.filter(filter)</code> gives back a new image after it's been enhanced by some filter (typically implemented by convolution, as described in our book.__ &rarr;

Some available filters include (use dir on <code>ImageFilter</code> to see others):

* BLUR
* CONTOUR
* DETAIL
* EDGE_ENHANCE
* EMBOSS


<pre><code data-trim contenteditable>
// assuming we have an Image object, img
from PIL import ImageFilter
out = img.filter(ImageFilter.DETAIL)
</code></pre>
</section>

<section markdown="block">
## Resizing

<code>img.resize(size)</code> __resizes the image to size__ tuple specified (width, height). There are various methods of resizing an image (that is figuring out what pixels to fill in). __What was the one we learned?__ &rarr;

Bilinear Interpolation
{:.fragment}

There are others...
{:.fragment}

* <code>PIL.Image.NEAREST</code> (use nearest neighbour)
* <code>PIL.Image.BILINEAR</code> (linear interpolation)
* <code>PIL.Image.BICUBIC</code> (cubic spline interpolation)
* <code>PIL.Image.LANCZOS</code> (a high-quality downsampling filter
{:.fragment}

<pre><code data-trim contenteditable>
scaled = img.resize((img.size[0] * 2, img.size[1] * 2), Image.BILINEAR)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Thumbnail

<code>img.thumbnail(size)</code> also __resizes an image__. However ...

* the aspect ratio (proportional relationship between width and height) will be preserved (there won't be any stretching in one axis)
* the image will be no larger than the given size
* and... it __modifies in place__!

<pre><code data-trim contenteditable>
img.resize((img.size[0] * 0.5, img.size[1] * 0.5), Image.BILINEAR)
img.show()
</code></pre>
</section>

<section markdown="block">
## Transpose

__<code>img.transpose</code> allows us to rotate or flip an image. Some possible transpose operations are:__ &rarr;

<pre><code data-trim contenteditable>
out = img.transpose(Image.FLIP_TOP_BOTTOM)
out = img.transpose(Image.ROTATE_90)
out = img.transpose(Image.ROTATE_180)
</code></pre>

</section>

<section markdown="block">
## Point Operations

__Point operations allow us to quickly modify an image's pixels with a single expression (kind of like the pixel.__ &rarr; 

It takes a function as an argument, and every color in every pixel will be transformed by that function.

<pre><code data-trim contenteditable>
new_img = im.point(lambda i: i * 2.5)
</code></pre>

</section>


<section markdown="block">
## Paste

__<code>img.paste(other_image, box)</code> allows other\_img to be pasted into img at the coordinates specified by box.__ &rarr;

(box is a tuple... with 2 elements, it represents the upper left corner of the pasted image)

<pre><code data-trim contenteditable>
>>> img1 = Image.open('/tmp/wallaby.jpg')
>>> img2 = Image.open('/tmp/raccoon.jpg')
>>> img1.paste(img2, (0, 0))
>>> img1.show()
</code></pre>

</section>

<section markdown="block">
## How Would We Create This?

__Let's use some of the built-in PIL functionality that we learned to create the following image from a single image a of a raccoon:__ &rarr;

![raccoon](../../resources/img/raccoon_repeated.jpg)

</section>
<section markdown="block">
## Four Upside Down Raccoons

<pre><code data-trim contenteditable>
>>> new_img.show()
>>> img = Image.open('/tmp/raccoon.jpg')
>>> new_img = Image.new('RGB', (img.size[0] * 4, img.size[1]))
>>> for i in range(4):
...   img = img.point(lambda p: p * (i + 0.75))
...   new_img.paste(img, (i * img.size[0], 0))
...
>>> new_img.thumbnail(((new_img.size[0] / 3), (new_img.size[1] / 3)))
>>> 
>>> new_img.show()
>>> out = new_img.transpose(Image.ROTATE_180)
>>> out.show()
</code></pre>

</section>

<section markdown="block">
## IO

__The <code>io</code> module provides tools for handling various kinds of input/output:__ &rarr;

* text i/o
* binary i/o
* raw i/o

An actual object that deals with this kind of i/o is called a __file object__. We've seen this before, of course! Some synonyms for __file object__ are:

* stream 
* file-like object.

These file / stream / file-like objects all allow some common operations, such as reading, opening in various modes, etc. ... Check out the documentation for all of the details: [https://docs.python.org/3/library/io.html](https://docs.python.org/3/library/io.html)

</section>
<section markdown="block">
## Text I/O

From the docs:

__"Text I/O expects and produces str objects."__ Encoding and decoding of bytes is done for us.

We've created text streams before! __How?__ &rarr;

<pre><code data-trim contenteditable>
f = open("myfile.txt", "r")
</code></pre>
{:.fragment}

It's also possible to an in-memory text streams by using StringIO objects (if you want to work with something _file_ like but don't want to write it to an _actual_ file... huh? what?):
{:.fragment}

<pre><code data-trim contenteditable>
f = io.StringIO("some initial text data\n")
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Binary I/O

__"Binary I/O (also called buffered I/O) expects and produces bytes objects. No encoding, decoding, or newline translation is performed."__ 

__Why would we need this?__ &rarr;

To work with non-text data, such as (you guessed it) images!
{:.fragment}

<pre><code data-trim contenteditable>
// from a file
f = open("myfile.jpg", "rb")

// in memory 
f = io.BytesIO(b"some initial binary data: \x00\x01")
</code></pre>
{:.fragment}

Hold on... what's that b-prefix about? [It's a literal __bytes__ type](https://docs.python.org/3.3/library/functions.html#bytes) - an immutable sequence of integers from 0 through 255.
{:.fragment}
</section>

<section markdown="block">
## Requests

We've seen most of what we need to know about requests:

* __response = requests.get(url)__ - ask a site for a _resource_ (like an image or web page)
* __response.text__ - the text version of the response body

So, one more thing to add:

* __response.content__  can be used to access the body of a response when it's not text (liiiiike... say an image)

</section>

<section markdown="block">
## Uh. So What?


__Where are we headed here? We saw an in-memory representation of byte i/o. What's next?__ &rarr;

We can actually create an Image object from the response of an http request:
{:.fragment}
        
<pre><code data-trim contenteditable>
img_response = requests.get('http://some.domain.foo/image.jpg')
img = Image.open(BytesIO(img_response.content))
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## HTML/CSS/DOM

__This is a broad topic outside of the scope of this class__, but I'll spend a couple of minutes doing a quick refresher. We'll need to know:

* elements, tags, attributes
* css selectors

Check out these resources if you didn't take the web design course:

* [Common terms](http://learn.shayhowe.com/html-css/building-your-first-web-page/#common-html-terms)
* [CSS](http://learn.shayhowe.com/html-css/getting-to-know-css/) and [more CSS](http://learn.shayhowe.com/advanced-html-css/complex-selectors/)
* [DOM](https://www.w3.org/TR/REC-DOM-Level-1/introduction.html)

</section>

<section markdown="block">
## Beautiful Soup

<pre><code data-trim contenteditable>
from bs4 import BeautifulSoup

// parsing html
soup = BeautifulSoup(text)

// using a selector (returns a list)
links = soup.select('.cast_list td.itemprop a')

// accessing an attribute
link['href']
</code></pre>
</section>

<section markdown="block">
## Some Imports

<pre><code data-trim contenteditable>
from PIL import Image
from bs4 import BeautifulSoup
import requests
from io import BytesIO
</code></pre>
</section>

<section markdown="block">
## Getting The Full Cast and Links to Individuals

<pre><code data-trim contenteditable>
url = 'http://www.imdb.com/title/tt0087182/fullcredits?ref_=tt_ov_st_sm'
response = requests.get(url)
#img = Image.open(StringIO(response.content))
soup = BeautifulSoup(response.text)
links = soup.select('.cast_list td.itemprop a')
</code></pre>

</section>

<section markdown="block">
## Creating a List of Lists That Contain More Lists

If we want to calculate the average, we'll want to hold all of the RGB values for every pixel.  __Uh ... this is crazy__ &rarr;

<pre><code data-trim contenteditable>
if not colors:
    colors = [[[0, 0, 0] for i in range(image.size[1])] for i in range(image.size[0])]
</code></pre>

</section>

<section markdown="block">
## Going Through Every Link We Have

Start a count... and go through every link we have...

<pre><code data-trim contenteditable>
count = 0
for link in links:
    print(link['href'])
</code></pre>
</section>

<section markdown="block">
## Getting an Individual's Page 

...(so we can get the image)

<pre><code data-trim contenteditable>
&nbsp;   try:
        detail_page_response = requests.get('http://www.imdb.com' + link['href'])
    except KeyError:
        print('skipping link', link)
        continue
    detail_page_soup = BeautifulSoup(detail_page_response.text)
    img = detail_page_soup.select('#name-poster')

</code></pre>

</section>

<section markdown="block">
## Try Retrieving Their Image

&nbsp;   try:
        img_response = requests.get(img[0]['src'])
    except IndexError:
        print('skipping image', img)
        continue
        
</section>

<section markdown="block">
## Add The New Image's Colors to Our Collection of Pixels

<pre><code data-trim contenteditable>
&nbsp;   image = Image.open(BytesIO(img_response.content))
    pixels = image.load()
    if not colors:
        colors = [[[0, 0, 0] for i in range(image.size[1])] for i in range(image.size[0])]
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            for c in range(3):
                colors[x][y][c] += pixels[x,y][c]
    count += 1

</code></pre>

</section>
<section markdown="block">
## Create a new Image

We'll just divide by the count... and use our crazy list of lists of lists to populate the pixels of a new image.

<pre><code data-trim contenteditable>
new_img = Image.new('RGB', (len(colors), len(colors[0])))
new_pixels = new_img.load()
for x in range(len(colors)):
    for y in range(len(colors[x])):
        for c in range(3):
            new_pixels[x, y] = tuple([int(c / count) for c in colors[x][y]])
new_img.show()
</code></pre>
</section>
