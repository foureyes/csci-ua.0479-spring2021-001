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
# Enough Numbers and Letters. How About Some Pictures!?

</section>

<section markdown="block">
## Digital Images

__What's a digital image? What is it made of?__ &rarr;

A __digital image__ is just a collection of pixels:
{:.fragment}

* {:.fragment} pixels are arranged in a 2-dimensional grid
* {:.fragment} theses _rectangles of pixel data_ are also called __raster images__
* {:.fragment} more pixels means more detail / higher resolution
* {:.fragment} each pixel has a color... typically represented by some combination of red, green and blue

</section>

<section markdown="block">
## RGB Color Model

A pixel's __color is determined by the amounts of primary colors__ (<span style="color: red">red</span>, <span style="color: green">green</span>, and <span style="color: blue">blue</span>) that its composed of. &rarr;

* {:.fragment} __intensity__ is the amount of a particular primary color component
* {:.fragment} this value can range from 0 to 255
* {:.fragment} the primary color values are arranged as: red first, green second, and blue last
* {:.fragment} a pixel that has 0 intensity for all primary colors is black... and 255 for each is white
* {:.fragment} some additional examples of rgb combinations:
    * __red__ <span class="fragment">- 255, 0, 0</span>
    * __green__ - <span class="fragment">0, 255, 0 </span>
    * __blue__ - <span class="fragment">0, 0, 255 </span>
    * __yellow__ - <span class="fragment">255, 255, 0 </span>
</section>


<section markdown="block">
## Python and Digital Images

The __Python Imaging Module__, or __PIL__ is a popular module for working with images in Python. It allows... &rarr;

* {:.fragment} creating, loading, and saving of images
* {:.fragment} ... as well as many image processing features such as filters, transforms, etc.

Unfortunately, installing it can be a bit confusing...
{:.fragment}

* {:.fragment} the current version of PIL is _actually_ called __Pillow__
* {:.fragment} when you install via PyCharm, look for the __Pillow__ module rather than PIL
* {:.fragment} (however, in your code, the `import` will still read as if you were importing PIL!? 😬 )

</section>

<section markdown="block">
## PIL Concepts

To represent a digital image, __PIL works with the three following concepts__ &rarr;

1. {:.fragment} bands
2. {:.fragment} image mode
3. {:.fragment} size and coordinate system

The concepts above describe a digital image in PIL and its attributes.
{:.fragment}
</section>

<section markdown="block">
## Bands

In PIL, images consist of one or more __bands__ of data. 

* {:.fragment} an image can be made up of multiple bands as long as each band has the same dimensions and _depth_
* {:.fragment} it's sometimes useful to think of a pixel as having one value per band
* {:.fragment} __an example is a png image that has 4 different bands, each representing one of the following:__ &rarr;
    * red, green, blue
    * transparency
* {:.fragment} a pixel would then be composed of 4 values
* {:.fragment} operations can act on all bands simultaneously or just single bands.

__But wait, didn't we say that pixels are just made up of RGB colors?__ &rarr;
{:.fragment}
</section>

<section markdown="block">
## Modes

It turns out that there are many many other ways to represent color. We'll primarily be using RGB, but __there are several other image modes__.

An __image mode__ defines the type and depth of a pixel in an image. Some modes include:

* {:.fragment} __<code>L</code>__ (8-bit pixels, grayscale)
* {:.fragment} __<code>RGB</code>__ (3x8-bit pixels, _true color_)
* {:.fragment} __<code>RGBA</code>__ (4x8-bit pixels, _true color_ with transparency mask)
* {:.fragment} __<code>CMYK</code>__ (4x8-bit pixels, color separation)

Again, we'll be focusing on __RGB__ mode images.
{:.fragment}



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

* <code>new(mode, size, color)</code> - creates an entirely new image
    * mode - sets the new image's mode (we'll use RGB)
    * size - the image's dimensions as a 2-tuple (width, height)
    * color - the initial color of the image as an int or as a tuple (default is black)
* <code>open(fp)</code> - loads an existing image
    * fp - file object or string representing path to file

[Check out the full documentation on the Image Module](https://pillow.readthedocs.org/en/3.1.x/reference/Image.html#PIL.Image.Image)
</section>

<section markdown="block">
## Image Objects

__Image objects contain the following _properties_ / _member_ variables and methods:__ &rarr;

* `size` - the image size in pixels as a 2-tuple, (width, height)
* `show(title, command)` - display the image represented by the Image object
    * title - title to be shown in display
    * command - command used to start display application / viewer
    * usually results in the image being shown as a <code>.bmp</code> using your default system viewer for bmps (like preview on OSX or paint on windows)
</section>

<section markdown="block">
## More Image Object Methods

__Methods for saving an image or opening / loading an image__ &rarr;

* `save(fp)` 
    * fp - file object or string representing path to file
    * format used based on extension!
* `load()` - loads an image's pixels and gives back a PixelAccess object so that individual pixels can be manipulated

[For all of the methods that an Image object supports, see the docs.](https://pillow.readthedocs.org/en/3.1.x/reference/Image.html#PIL.Image.Image)
</section>
<section markdown="block">
## PixelAccess Objects

__A <code>PixelAccess</code> object is a dictionary-like object that allows read and write access to every pixel in an <code>Image</code> object.__ &rarr;

* {:.fragment} _dictionary like?_ ... under the hood it's actually just a dictionary, but it provides additional methods that a dictionary doesn't have
* {:.fragment} you can get and set a pixel by using square brackets (like a dictionary) and a 2-tuple representing the x and y coordinate of the tuple
* {:.fragment} a pixel will also be a tuple (since we're working with RGB mode images, we'll be dealing with 3-tuples)
* {:.fragment} <code>PixelAccess</code> objects also have the following methods:
    * putpixel(xy, color)
    * getpixel(xy)

[Check out the documentation for <code>PixelAccess</code> objects](https://pillow.readthedocs.org/en/3.1.x/reference/PixelAccess.html)
{:.fragment}
</section>

<section markdown="block">
## Creating a New Image

__Let's use what we know to create and display a new all black 400 pixel wide and 300 pixell tall image.__ &rarr;

<pre><code data-trim contenteditable>
from PIL import Image
img = Image.new('RGB', (400, 300))
img.show()
</code></pre>
{:.fragment}

Maybe we want red to be the default color instead. __Without using a PixelAccess object, change the color to red.__ &rarr;
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
## Green!

All green everything. __Using individual pixels__ &rarr;
<pre><code data-trim contenteditable>
from PIL import Image
img = Image.new('RGB', (400, 300))
pixels = img.load()
width, height = img.size
for x in range(width):
    for y in range(height):
        pixels[(x, y)] = (0, 255, 0)
img.show()
</code></pre>
{:.fragment}

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

__Create a new image:__ &rarr;

1. {:.fragment} make a new image with...
    * a background color of white
    * a black vertical line very 10th pixel
2. {:.fragment} try moving  your code into a function that takes an image object adds vertical lines to it
    * modify your function so that you can specify
        * how much spacing there is between lines
        * the color of the lines
    * no return value needed
    * (a `PixelAccess` object is mutable)


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

Hint: one way to do this is to change the interval to space + stroke width... and either move forwards or backwards making 1 pixel vertical lines until the desired width is reached (3 loops!)
{:.fragment}

<pre><code data-trim contenteditable>
def vertical_lines(img, stroke, width_between, color):
    pixels = img.load()
    for x in range(stroke, img.size[0], width_between + stroke):
        for s in range(stroke):
            for y in range(img.size[1]):
                if x - s >= 0:
                    pixels[x - s, y] = color
</code></pre>
{:.fragment}

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
{:.fragment}
<pre><code data-trim contenteditable>
new_img = Image.open('/tmp/wallaby.jpg')
hot(new_img)
new_img.show()
</code></pre>
{:.fragment}
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

__Here's an implementation of the above as a function__ &rarr;

<pre><code data-trim contenteditable>
from PIL import Image
def grayscale(img):
    pixels = img.load() 
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            avg = sum(pixels[i,j]) // 3
            pixels[i,j] = (avg,) * 3
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
new_img = Image.open('wallaby.jpg')
grayscale(new_img)
new_img.show()
</code></pre>
{:.fragment}

There are some tiny tricks above:
{:.fragment}

* multiplying a tuple to repeat an element
* using the built in function, `sum`
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
            new_c = [255 - c for c in pixels[i, j]]
            pixels[i,j] = tuple(new_c)

</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
new_img = Image.open('wallaby.jpg')
inverse(new_img)
new_img.show()
</code></pre>
{:.fragment}

Oh hey - remember __list comprehensions__?
{:.fragment}


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
* {:.fragment} the image and a _transform_ function
* {:.fragment} what arguments should the transform function expect, and what should it return?
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

Let's try this for hot, inverse, and grayscale:

<pre><code data-trim contenteditable>
pixel_map(new_img, lambda t: (255, t[1], t[2]))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
pixel_map(new_img, lambda t: tuple([255 - c for c in t]))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
pixel_map(new_img, lambda t: (sum(t) // 3, ) * 3)
</code></pre>
{:.fragment}
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

<section markdown="block">
## Don't Do This, But Let's Do This

__We can actually make the to-black-and-white function a one liner using special syntax__ &rarr;

<pre><code data-trim contenteditable>
res = None
if cond:
    res = val1
else:
    res = val2
</code></pre>
{:.fragment}

Can be rewritten as:
{:.fragment}

<pre><code data-trim contenteditable>
res = val1 if cond else val2
</code></pre>
{:.fragment}

Which bring us to this terrible thing:
{:.fragment}

<pre><code data-trim contenteditable>
pixel_map(img, lambda color: (255,) * 3 if sum(color) // len(color) < 150 else (0, ) * 3)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Some Fun: Combining Images

Let's use our PIL skills to try different ways of combining images:

* weighted average of colors of multiple images
* [Chromakey](https://en.wikipedia.org/wiki/Chroma_key) - remove background of an image based on color

Some images:

* [space](https://cdn.vox-cdn.com/thumbor/qjjqhTOzgsEW8UsOvVJRZLrD234=/0x0:7700x5800/1200x800/filters:focal(3234x2284:4466x3516)/cdn.vox-cdn.com/uploads/chorus_image/image/56042817/2016_01_30_The_Andromeda_Galaxy_M31_T2HM_Peter_Ilas.0.jpg)
* [grumpy cat](https://cdn.vox-cdn.com/thumbor/tQKD0HljTpEr5pl_3EtUA6yb1dw=/0x52:3000x2052/1200x800/filters:focal(0x52:3000x2052)/cdn.vox-cdn.com/uploads/chorus_image/image/44294754/grumpy_cat.0.0.jpg)
</section>

<section markdown="block">
## Weighted Average

__Create a function to mix two images using the following header: <code>def mix_img(img1, img2, w=0.5):</code>__ &rarr;

* it should create a new image
* by calculating the weighted average of the colors in img1 and img2


<pre><code data-trim contenteditable>
def mix_img(img1, img2, w=0.5):
    img = Image.new('RGB', img1.size)
    pix, pix1, pix2 = img.load(), img1.load(), img2.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            c1 = pix1[x, y]
            c2 = pix2[x, y]
            c =  [int(c1[i] * w  + c2[i] * (1 - w)) for i in range(3)]
            pix[x, y] = tuple(c)
    return img
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Chromakey

__Let's try extracting a part of an image from its background and overlaying it on another image. User this header: <code>def chromakey(src, dest, thresh=220)</code>.__ &rarr;

* source is the image where a part will be extracted from the background
* destination is is where the source image will be placed over (it serves as the new background)

<pre><code data-trim contenteditable>
def chromakey(src, dest, thresh=220):
    pix1, pix2 = src.load(), dest.load()
    for x in range(src.size[0]):
        for y in range(src.size[1]):
            c = pix1[x, y]
            if c[0] < thresh and c[1] < thresh and c[2] < thresh:
                pix2[x, y] = c
    return dest
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Now... Your Turn


1. __drawing rectangles__
2. __flip vertically__ (over the horizontal axis)

</section>

<section markdown="block">
## Draw Some Rectangles

__Create a function called <code>rectangle(img, ul_x, ul_y, width, height, color)</code> that draws a rectangle with the specified coordinates, dimensions and color.__ &rarr;

Example usage... (note that if the rectangle is off image, the part that's on the image should be displayed, but the part off image should not cause an error)

<pre><code data-trim contenteditable>
new_img = Image.new('RGB', (400, 300), (255, 255, 255))
rectangle(new_img, 20, 20, 100, 100, (255, 0, 0))
rectangle(new_img, 350, 20, 100, 100, (255, 0, 0))
new_img.show()
</code></pre>
</section>

<section markdown="block">
## Draw Some Rectangles

Some pseudocode...

* {:.fragment} determine lower right x and y
* {:.fragment} loop from upper left x to lower right x
* {:.fragment} loop from upper left y to lower right y
* {:.fragment} check if x and y values are within image dimensions

<pre><code data-trim contenteditable>
def rectangle(img, ul_x, ul_y, width, height, color):
    pixels = img.load()
    lr_x = ul_x + width
    lr_y = ul_y + height
    for x in range(ul_x, lr_x + 1):
        for y in range(ul_y, lr_y + 1):
            if x >= 0 and x < img.size[0] and\
                    y >= 0 and y < img.size[1]:
                pixels[x, y] = color

</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Flip Vertically

__Create a function called <code>flip_vertical(orig_img)</code>__ that takes an image and returns a new image flipped on the horizontal axis &rarr;

* create a new image
* go over every pixel in the new image
* determine which pixel to choose from the old image 
    * ... we want the image to be flipped on the horziontal axis
    * ... x stays the same, but what is the y of the pixel from the original image?
    * {:.fragment} the height - 1 - the current new pixel's y


</section>

<section markdown="block">
## Flip Vertically Continued

<pre><code data-trim contenteditable>
def flip_vertical(orig_img):
    width, height = orig_img.size;
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    orig_pixels = orig_img.load()
    for x in range(width):
        for y in range(height):
            clc_x, clc_y = x, height - y - 1
            t = clc_x, clc_y
            pixels[x, y] = orig_pixels[t]
    return img
</code></pre>

</section>

<section markdown="block">
## Scaling Up

The previous transformations that we implemented worked on an existing image object and modified its pixels. 

However, to scale up an image (make it larger), we'll need to create an entirely new image of different dimensions. __Let's come up with a way to go through the pixels in a source image, and create an entirely new image that's scaled up.__ &rarr;

<pre><code data-trim contenteditable>
# open an existing image
img = Image.load('foo.png')

# call a function that we create called scale...
scaled = scale(img, target_w, _target_h)

# scaled contains the newly scaled image
scaled.show()
</code></pre>

__What might the pseudocode look like for this function? Let's try to do it by going through every pixel in the original image first.__ &rarr;

</section>

<section markdown="block">
## Pseudocode for Scaling

__This is one potential way of implementing scaling__ &rarr;

1. {:.fragment} create a __new__ image with the target dimensions
2. {:.fragment} determine ratio (or factor to multiply original image dimensions by)
3. {:.fragment} go through every pixel in the original image by
    * {:.fragment} going over every x value
    * {:.fragment} for every x value, go over every possible y value
4. {:.fragment} fill in an n x n portion of the new image based on the original pixel
    * {:.fragment} the n x n portion of the new image starts at x * factor_w
    * {:.fragment} and ends at (x + 1) * factor_w
    * {:.fragment} same for y values
</section>

<section markdown="block">
## Scaling Version 1 (Original to New)

__Some setup...__ &rarr;

<pre><code data-trim contenteditable>
def scale_old_to_new(orig_img, target_w, target_h):
    img = Image.new('RGB', (target_w, target_h))
    orig_w, orig_h = orig_img.size
    pixels = img.load()
    orig_pixels = orig_img.load()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Scaling Version 1 (Original to New) Continued


__Calculate the ratios / _factors_ (round down), and go through every pixel in the original image.__ &rarr;

<pre><code data-trim contenteditable>
    factor_w = target_w // orig_w
    factor_h = target_h // orig_h
    for x in range(orig_w):
        for y in range(orig_h):
</code></pre>
{:.fragment}

__...Aaaand fill in the appropriate region of the new image__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
            for new_x in range(x * factor_w, (x + 1) * factor_w ):
                for new_y in range(y * factor_h, (y + 1) * factor_h):
                    pixels[new_x, new_y] = orig_pixels[x, y]
    return img
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Another Approach

__How could we accomplish the same thing with... ummm... less looping?__ &rarr;


* {:.fragment} go over the pixels in the new image instead
* {:.fragment} get rid of the 2 nested loops to fill the region
* {:.fragment} ... determine which pixel in the old image will provide the color info
* {:.fragment} new image's x and y divided by the factor / scale will give us the old image pixel that it's drawing the color data from

</section>

<section markdown="block">
## Scaling Again

<pre><code data-trim contenteditable>
def scale_new_from_old(orig_img, target_w, target_h):
    img = Image.new('RGB', (target_w, target_h))
    orig_w, orig_h = orig_img.size
    pixels = img.load()
    orig_pixels = orig_img.load()
    factor_w = target_w // orig_w
    factor_h = target_h // orig_h
    for x in range(target_w):
        for y in range(target_h):
            pixels[x, y] = orig_pixels[x // factor_w, y // factor_h]
    return img
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

