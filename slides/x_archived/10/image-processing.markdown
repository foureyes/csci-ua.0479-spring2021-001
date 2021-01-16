---
layout: slides
title: "Image Processing"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Digital Images

A __digital image__ is just a collection of pixels:

* pixels are arranged in a 2-dimensional grid
* theses _rectangles of pixel data_ are also called __raster images__
* more pixels means more detail / higher resolution
* each pixel has a color... typically represented by some combination of red, green and blue

</section>

<section markdown="block">
## RGB Color Model

__A pixel's color is determined by the amounts of primary colors (red, green, and blue) that its composed of.__ &rarr;

* __intensity__ is the amount of a particular primary color component
* this value can range from 0 to 255
* the primary color values are arranged as: red first, green second, and blue last
* a pixel that has 0 intensity for all primary colors is black... and 255 for each is white
* some additional examples of rgb combinations:
    * __red__ - 255, 0, 0 
    * __green__ - 0, 255, 0 
    * __blue__ - 0, 0, 255 
    * __yellow__ - 255, 255, 0 
</section>


<section markdown="block">
## Python and Digital Images

The __Python Imaging Module__, or __PIL__ is a popular module for working with images in Python.

* allows creating, loading, and saving of images
* ... as well as many image processing features such as filters, transforms, etc.
* the current version of PIL is _actually_ called __Pillow__
* when you install via PyCharm, look for the __Pillow__ module rather than PIL
* (however, you'll still need to import PIL)

(__The book uses a called cImage for working with digital images, but PIL/Pillow is more likely what you'll encounter in _real world_ programming__)
</section>

<section markdown="block">
## cImage vs PIL/Pillow

__Again, we'll be using PIL/Pillow__ &rarr;

* so... for the readings, ignore the part about <code>cImage</code>
* however, the algorithms outlined in the book still work, of course!

</section>
<section markdown="block">
## PIL Concepts

To represent a digital image, __PIL works with the follwoing concepts__ &rarr;

* bands
* image mode
* size and coordinate system

</section>
<section markdown="block">
## Bands

In PIL, images consist of one or more bands of data. 

* an image can be made up of multiple bands as long as each band has the same dimensions and _depth_
* it's sometimes useful to think of a pixel as having one value per band
* __an example is a png image that has 4 different bands, each representing one of the following:__ &rarr;
    1. red
    2. green
    3. blue
    4. transparency
* a pixel would then be composed of 4 values
* operations can act on all bands simultaneously or just single bands.

__But wait, didn't we say that pixels are just made up of RGB colors?__ &rarr;
</section>

<section markdown="block">
## Modes

It turns out that there are many many other ways to represent color. We'll primarily be using RGB, but __there are several other image modes__.

An __image mode__ defines the type and depth of a pixel in an image. Some modes include:

* __<code>L</code>__ (8-bit pixels, grayscale)
* __<code>RGB</code>__ (3x8-bit pixels, _true color_)
* __<code>RGBA</code>__ (4x8-bit pixels, _true color_ with transparency mask)
* __<code>CMYK</code>__ (4x8-bit pixels, color separation)

Again, we'll be focusing on RGB mode images.



</section>
<section markdown="block">
## Size and Coordinate System

__Of course, an image will have horizontal and vertical size in pixels.__

* In PIL, this is represented as a 2-element tuple (2-tuple)

__As for the coordinate system:__

* (0, 0) is at the upper left hand corner 
* x and y values __increase__ as you go right and down!
</section>


<section markdown="block">
## PIL API

For our work with the PIL API, we'll mostly be using these modules and objects:

1. {:.fragment} the __Image module__ - the module that we'll be importing from PIL
2. {:.fragment} __Image objects__ - the most important object in PIL; it _obviously_ represents an image
3. {:.fragment} __PixelAccess objects__ - mediates access to an images grid of pixels

</section>
<section markdown="block">
## The Image Module

__The <code>Image</code> module allows us to create objects of the same name.__ It provides a few methods for creating __Image objects__. The two that we'll be using are:

* __<code>new(mode, size, color)</code>__ - creates an entirely new image
    * mode - sets the new image's mode (we'll use RGB)
    * size - the image's dimensions as a 2-tuple (width, height)
    * color - the initial color of the image as an int or as a tuple (default is black)
* __<code>open(fp)</code>__ - loads an existing image
    * fp - file object or string representing path to file

[Check out the full documentation on the Image Module](https://pillow.readthedocs.org/en/3.1.x/reference/Image.html#PIL.Image.Image)
</section>

<section markdown="block">
## Image Objects

__Image objects contain the following _properties_ / _member_ variables and methods:__ &rarr;

* __size__ - the image size in pixels as a 2-tuple, (width, height)
* __show(title, command)__ - display the image represented by the Image object
    * title - title to be shown in display
    * command - command used to start display application / viewer
    * usually results in the image being shown as a <code>.bmp</code> using your default system viewer for bmps (like preview on OSX or paint on windows)
* __save(fp)__ 
    * fp - file object or string representing path to file
    * format used based on extension!
* __load()__ - loads an images pixels and gives back a PixelAccess object so that individual pixels can be manipulated

[For all of the methods that an Image object supports, see the docs.](https://pillow.readthedocs.org/en/3.1.x/reference/Image.html#PIL.Image.Image)
</section>

<section markdown="block">
## PixelAccess Objects

__A <code>PixelAccess</code> object is a dictionary-like object that allows read and write access to every pixel in an <code>Image</code> object.__ &rarr;

* _dictionary like?_ ... under the hood it's actually just a dictionary, but it provides additional methods that a dictionary doesn't have
* you can get and set a pixel by using square brackets (like a dictionary) and a 2-tuple representing the x and y coordinate of the tuple
* a pixel itself will also be a tuple (we'll mostly be working with RGB mode images, so we'll be dealing with 3-tuples)
* <code>PixelAccess</code> objects also have the following methods:
    * putpixel(xy, color)
    * getpixel(xy)

[Check out the documentation for <code>PixelAccess</code> objects](https://pillow.readthedocs.org/en/3.1.x/reference/PixelAccess.html)
</section>

<section markdown="block">
## Creating a New Image

__Let's use what we know to create and display a  new image - a 400 pixel wide and 300 pixel tall image of the color black.__ &rarr;

<pre><code data-trim contenteditable>
from PIL import Image
img = Image.new('RGB', (400, 300))
img.show()
</code></pre>
{:.fragment}

Hm... maybe we want red to be the default color instead. __Without using a PixelAccess object, change the color to red.__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
# we just need to modify our call to Image.new so that
# the default background color, black, is overridden 
img = Image.new('RGB', (400, 300), (200, 0, 0))
</code></pre>
{:.fragment}

Ok, now... __let's save it as <code>red.png</code>__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
img.save('/tmp/red.png')
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Accessing Pixel Data

Instead of overriding the default color, __let's try explicitly setting every pixel to a color.__ &rarr;

* using the same new image
* access every pixel, and change the color to green
* again, display the image (but don't save it)

__What's the pseudocode for this?__ &rarr;

1. {:.fragment} create a new image
2. {:.fragment} load that image's pixel data so that it can be manipulated
4. {:.fragment} for every x
5. {:.fragment} for every y
6. {:.fragment} set pixel at coordinate x, y to green
7. {:.fragment} show it!


</section>

<section markdown="block">
## Some Drawing

Ok... so filling an entire image with the same color isn't too exciting. __Let's try to do some primitive drawing.__ &rarr;

* creating color "static"
* creating black and white "static" (no gray)
* vertical lines
* stroke width
* a rectangle

</section>
<section markdown="block">
## Generate an Image That Looks Like Static

__Make this image__ &rarr;

![static color](../../resources/img/static_color.png)

</section>

<section markdown="block">
## Makin' Color "Static"

<pre><code data-trim contenteditable>
from PIL import Image
from random import randint
img = Image.new('RGB', (400, 300))
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixels[x, y] = (randint(0, 255), randint(0, 255),  randint(0, 255))
img.show()
</code></pre>
</section>

<section markdown="block">
## Make the Previous Just Black and White

__Make this image__ &rarr;

![static color](../../resources/img/static_bw.png)

</section>

<section markdown="block">
## Makin' Black and White  "Static"

<pre><code data-trim contenteditable>
from PIL import Image
from random import randint
img = Image.new('RGB', (400, 300))
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        if randint(0, 1) == 1:
            pixels[x, y] = (255, 255, 255)
img.show()
</code></pre>
</section>

<section markdown="block">
## Vertical Lines

__Create a new image with:__ &rarr;

* a background color of white
* a vertical line very 10th pixel
* try moving  your code into a function that takes an image object adds vertical lines to it
* modify your function so that you can specify
    * how much spacing there is between lines
    * the color of the lines


</section>

<section markdown="block">
## Vertical Lines

__After you've gone through all of the requirements in the previous slide, you should end up with a function that looks a little bit like this...__ &rarr;

<pre><code data-trim contenteditable>
def vertical_lines(img, width_between, color):
    pixels = img.load()
    for x in range(0, img.size[0], width_between):
        for y in range(img.size[1]):
            pixels[x, y] = color
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
new_img = Image.new('RGB', (400, 300), (255, 255, 255))
vertical_lines(new_img, 10, (0, 0, 0))
new_img.show()
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Stroke Width

__Let's try changing our previous function so that it accepts a stroke width.__ (lines are no longer just 1 pixel) &rarr;

<pre><code data-trim contenteditable>
def vertical_lines(img, stroke, width_between, color):
    pixels = img.load()
    for x in range(stroke, img.size[0], width_between + stroke):
        for s in range(stroke):
            for y in range(img.size[1]):
                if x - s >= 0:
                    pixels[x - s, y] = color
</code></pre>

</section>
<section markdown="block">
## Loading Images

Making our own images is pretty fun, but __what about bringing in existing images?__ &rarr;

We can use the <code>open</code> function instead of <code>new</code> on the <code>Image</code> module.
{:.fragment}

<pre><code data-trim contenteditable>
img = Image.open('/path/to/image.png')
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Loading an Image Example

Download [this image of a wallaby](../../resources/img/wallaby.jpg).

* put it in your project folder
* or someplace _easy_ to find / type!
* open and display the image with PIL

<pre><code data-trim contenteditable>
from PIL import Image
# assuming image is in your project folder
img = Image.open('wallaby.jpg')
img.show()
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## A Very Hot Wallaby

__Let's try to do some pixel maniuplation on our wallaby. What happens if we up every red pixel to 255?__ &rarr;

<pre><code data-trim contenteditable>
from PIL import Image
def hot(img):
    pixels = img.load() 
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            colors = pixels[i,j]
            pixels[i,j] = (255, colors[1], colors[2])
</code></pre>
<pre><code data-trim contenteditable>
new_img = Image.open('/tmp/wallaby.jpg')
hot(new_img)
new_img.show()
</code></pre>
</section>
<section markdown="block">
## Making Our Image Grayscale

In the previous class, we saw a preview of making an image grayscale. 

* essentially, we have to find a way to set the red, green and blue values of every pixel to the same intensity so that we only have grays in our color palette
* somehow, we have to translate the intensity of each color to a single one 

__How did we do it?__ &rarr;

* {:.fragment} go through every pixel
* {:.fragment} take the average of the red, green and blue value
* {:.fragment} set the pixel's color so that each primary color component is set to the average

</section>

<section markdown="block">
## Grayscale Implementation

__Here's an implementation of the above as a function (there's a tiny tricky bit for multiplying a tuple on the 2nd to laste line.__ &rarr;

<pre><code data-trim contenteditable>
from PIL import Image
def grayscale(img):
    pixels = img.load() 
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            avg = sum(pixels[i,j]) // 3
            pixels[i,j] = (avg,) * 3
</code></pre>

<pre><code data-trim contenteditable>
new_img = Image.open('wallaby.jpg')
grayscale(new_img)
new_img.show()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Black and White Only

__Hm... gray scale is just too many colors! I want my wallaby to be just black and white... how can we modify the previous function so that there are only black and white pixels in the image__ &rarr;

<pre><code data-trim contenteditable>
from PIL import Image
def bw(img, thresh):
    pixels = img.load() 
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            avg = sum(pixels[i,j]) // 3
            if avg > thresh:
                pixels[i,j] = (255,) * 3
            else:
                pixels[i,j] = (0,) * 3
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
new_img = Image.open('wallaby.jpg')
bw(new_img, 255 / 2)
new_img.show()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Inverse / Negative

To reverse the color of an image, subtract each of its component color values from 255. __Let's see what this looks like__ &rarr;
<pre><code data-trim contenteditable>
from PIL import Image
def inverse(img):
    pixels = img.load() 
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            colors = pixels[i,j]
            pixels[i,j] = tuple([255 - c for c in pixels[i, j]])

</code></pre>
<pre><code data-trim contenteditable>
new_img = Image.open('wallaby.jpg')
inverse(new_img)
new_img.show()
</code></pre>
</section>
<section markdown="block">
## Wait, Wait, Wait

__Let's look at all of those functions again: hot, grayscale, bw, and inverse. Something looks fishy here.__ &rarr;

* {:.fragment} they're all pretty much doing the same thing
* {:.fragment} __what's the main thing that's changing?__ &rarr;
* {:.fragment} the body of the inner for loop
* {:.fragment} __time for some higher order functions!__ &rarr;
* {:.fragment} (functions that take functions as arguments)

</section>

<section markdown="block">
## Pixel Mapper

__Make a generic pixel mapper function that transforms all of the pixels in an image according to a function passed in as an argument.__ &rarr;

* {:.fragment} what should the arguments be?
* {:.fragment} the image and the _callback_ or _transform_ function
* {:.fragment} what arguments should the transform function expect, and what should it return
* {:.fragment} a 3-element tuple
</section>

<section markdown="block">
## Pixel Mapper Continued

__Here's an implementation of our pixel mapper function!__ &rarr;

<pre><code data-trim contenteditable>
def pixel_map(img, f):
    pixels = img.load() 
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = f(pixels[i, j])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Using Our Pixel Mapper

__Ok... let's try turning our black and white function to our pixel mapper higher order function__ &rarr;

<pre><code data-trim contenteditable>
new_img = Image.open('/tmp/wallaby.jpg')

def to_bw_pixel(t):
    avg = sum(t) // 3
    if avg > 255 // 2:
        return (255, ) * 3
    else:
        return (0, ) * 3

pixel_map(new_img, to_bw_pixel)
new_img.show()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## In Fact, Some of Our Functions are so Small...

__We can just use one line functions called lambdas!__ &rarr;

<pre><code data-trim contenteditable>
function anonymous(x):
    return x * 2

# same as a lambda...
lambda x: x * 2
</code></pre>

Let's try this for grayscale, hot and inverse:

<pre><code data-trim contenteditable>
pixel_map(new_img, lambda t: (255, t[1], t[2]))
pixel_map(new_img, lambda t: tuple([255 - c for c in t]))
pixel_map(new_img, lambda t: (sum(t) // 3, ) * 3)
</code></pre>
</section>
<section markdown="block">
## I Think We Lost Something

So... for bw, we lost something along the way. __What was it?__ &rarr;

__The threshold was hardcoded!__
{:.fragment}

* {:.fragment} We hardcoded it because the function that pixel_map takes as its second parameter is __always__ called with only one argument
* {:.fragment} We can use <code>partial</code> from the <code>functools</code> module to fix additional arguments by "binding" a value to those arguments
* {:.fragment} changing the number of arguments that a function can take is called changing its __arity__.

</section>



<section markdown="block">
## Using Partial

__Use <code>partial</code> to bind the first parameter of to_bw_pixel to a particular threshold value.__ &rarr;

<pre><code data-trim contenteditable>
from functools import partial

def to_bw_pixel(thresh, t):
    avg = sum(t) // 3
    if avg > 255 // 2:
        return (255, ) * 3
    else:
        return (0, ) * 3

bound_to_bw = partial(to_bw_pixel, 255 // 2)
</code></pre>

<code>partial</code> returns a new function. That function is to_bw_pixel... with thresh automatically set to 255 // 2. Now you'll only need one argument for <code>bound_to_bw</code>, so you can call this:

<pre><code data-trim contenteditable>
pixel_map(new_img, lambda t: bound_to_bw(t))
</code></pre>
</section>

{% comment %}
* PIL API
* reading images
    * grayscale
    * remove red, green or blue
* pixel map
    * black and white
    * negative
* advanced
    * resizing
        * general resize function
        * smooth
    * pixelating
    * flip 
        * horizontal
        * vertical
        * mirror
    * edge detection convolution?
* more than one image
    * on same?merging two images
    * collage?
    * making an instagram filter
    * working with gifs
    * downloading images example?
* actual pil functionality
    * resize, rotate
    * filters, blur
    * thumbnailer
* drawing a circle!?
{% endcomment %}

