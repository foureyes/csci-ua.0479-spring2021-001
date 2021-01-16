---
layout: slides
title: "Advanced Image Processing"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Quick Review

__Let's go through a quick review of doing the following__ &rarr;

* {:.fragment} creating an entirely new image
* {:.fragment} opening an image
* {:.fragment} displaying an image
* {:.fragment} saving an image
* {:.fragment} reading an image's size
* {:.fragment} accessing an image's pixels
* {:.fragment} setting an image's pixels

[Check out the previous class slides on image processing for full details!](../09/image-processing.html)
{:.fragment}
</section>

<section markdown="block">
## Some Fun: Combining Images

Let's use our PIL skills to try different ways of combining images:

* weighted average of colors of 2 images
* [Chromakey](https://en.wikipedia.org/wiki/Chroma_key) - remove background of an image based on color

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

Some activities [from the previous class](https://docs.google.com/a/nyu.edu/forms/d/1zkCnVU_26wtBy6ZCMynyX0u2xwHT8fySuG8OzutAZZM/viewform):

(just copy and paste your code)

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

__Create a function called <code>flip_vertical(orig_img)</code>__ that takes an image and returns a new image flipped on the horizontal axis__ &rarr;

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

<section markdown="block">
## Such Pixels

__Something looked a little bit off with our scaling methods. What happened to the new image?__ &rarr;

* {:.fragment} the resulting scaling is a bit blocky and pixelated
* {:.fragment} that's great if you want that effect.... but...
* {:.fragment} maybe we can find a better way to fill in the missing pixels rather than just repeating a pixel

</section>
<section markdown="block">
## Another Look at Scaling Up

One way to approach scaling is to consider it as...

* adding a bunch of unknown colored pixels to an existing image
* previously, we just chose the color of the closest color in the original image(sort of), and repeated it
* maybe what we really want to do is find a better way of choosing those colors so that there's a smoother transition
* that's where __bilinear interpolation__ comes in!

</section>

<section markdown="block">
## Linear Interpolation

Before we even talk about __bilinear interpoloation__, we should probably talk about plain 'ol __linear interpoloation__.

You can think of linear interpolation as a way of solving this problem:

* we have 2 pixels with two different, but known, colors some distant apart...
* and we have 1 pixel between the two 
    * we know the distance it is from the other pixels
    * but we don't know its color!
* how do we figure it out?
* below... we're trying to figure out what color C is if the colors of C1 and C2 are known

<pre><code data-trim contenteditable>
+---+---+---+---+---+---+---+---+
|C1 |   |   |C  |   |   |   |C2 |
+---+---+---+---+---+---+---+---+
</code></pre>


</section>

<section markdown="block">
## Linear Interpolation Continued

So... one way to figure out the missing color is to use the following formulas. 

* basically, the distance of C from C1 or C2 determines _how much color_ is contributed from each
* the closer color will contribute more!

<pre><code data-trim contenteditable>
distance = c2_pos - c1_pos
ratio1 = (new_pos - c1_pos) / distance
ratio2 = (c2_pos - new_pos) / distance
multiple each color compontent of the known colors by these ratios
</code></pre>



</section>

<section markdown="block">
## Linear Interpoloation Function

<pre><code data-trim contenteditable>
def linear_interpolation(c1, c2, c1_pos, c2_pos, new_pos):
    new = [0, 0, 0]
    distance = c2_pos - c1_pos
    ratio1 = (new_pos - c1_pos) / distance
    ratio2 = (c2_pos - new_pos) / distance
    for i in range(len(new)):
        new[i] = int(ratio1 * c2[i] + ratio2 * c1[i])
    return tuple(new)
</code></pre>
</section>

<section markdown="block">
## Usage

__What do you think this will display?__ &rarr;

<pre><code data-trim contenteditable>
img = Image.new('RGB', (10, 1))
pixels = img.load()
pixels[0, 0] = (255, 0, 0)
pixels[9, 0] = (0, 255, 0)
for i in range(1, 9):
    pixels[i, 0] = linear_interpolation(pixels[0, 0], pixels[9, 0], 0, 9, i)
img.show()
</code></pre>
</section>

<section markdown="block">
## Bilinear Interpolation

__To translate that to two dimensions, repeatedly apply linear interpoloation. Check out the following articles.__ &rarr;

* [Bilinear Image Scaling from tech algorithm](http://tech-algorithm.com/articles/bilinear-image-scaling/)
* [Obligatory stackoverflow explanation](http://stackoverflow.com/questions/8808996/bilinear-interpolation-to-enlarge-bitmap-images)
* [Another take from superocmutingblog.com's bilinear-interpolation article](http://supercomputingblog.com/graphics/coding-bilinear-interpolation/)
</section>

<section markdown="block">
## Wait... How Does This Fit In With???

__Great... but how does this help with scaling?__ &rarr;

1. will take 2 x 2 samples of the original image
2. create a region in the target image based on the scaling factor
3. with the corners populated by the corresponding pixels in the original image
4. use linear interpolation to fill in the pixels between

__Let's see some code!__ &rarr;

</section>

<section markdown="block">
## Bilinear Interpolation

__Setup and begin looping over pixels in new image...__ &rarr;

<pre><code data-trim contenteditable>
def scale(orig_img, target_w, target_h):
    img = Image.new('RGB', (target_w, target_h))
    orig_w, orig_h = orig_img.size
    pixels = img.load()
    orig_pixels = orig_img.load()

    # determine scaling factors...
    factor_w = target_w // orig_w
    factor_h = target_h // orig_h
    for x in range(target_w):
        for y in range(target_h):
</code></pre>
</section>

<section markdown="block">
## Bilinear Interpolation Continued

__Figure out the beginning of the source 2x2 sample__ &rarr;
<pre><code data-trim contenteditable>
&nbsp;           orig_x, orig_y = min(x // factor_w, orig_w - 2), \
                    min(y // factor_h, orig_h - 2)
</code></pre>


__The upper bit's color...__ &rarr;

<pre><code data-trim contenteditable>
&nbsp;           # upper
            ul = orig_pixels[orig_x, orig_y]            
            ur = orig_pixels[orig_x + 1, orig_y]
            ul_x = orig_x * factor_w
            ur_x = (orig_x + 1) * factor_w
            c_top = linear_interpolation(
                    ul, ur, ul_x, ur_x, x)
</code></pre>

            

</section>
<section markdown="block">
## Bilinear Interpolation Continued

__The bottom part's color__ &rarr;

<pre><code data-trim contenteditable>            
&nbsp;           # bottom
            bl = orig_pixels[orig_x, orig_y + 1]            
            br = orig_pixels[orig_x + 1, orig_y + 1]
            bl_x = orig_x * factor_w
            br_x = (orig_x + 1) * factor_w
            c_bottom = linear_interpolation(\
                    bl, br, bl_x, br_x, x)
</code></pre>

__Now handle verticle...__ &rarr;

<pre><code data-trim contenteditable>
&nbsp;           c = linear_interpolation(c_top, c_bottom, \
                    orig_y * factor_h, \
                    (orig_y + 1) * factor_h, y)
</code></pre>

__Assign and return__ &rarr;

<pre><code data-trim contenteditable>
&nbsp;           pixels[x, y] = c
    return img
</code></pre>
</section>

<section markdown="block">
## Or Use Built in PIL

Of course, PIL can do this for you!

<pre><code data-trim contenteditable>
scaled = img.resize((target_x, target_y), Image.BILINEAR)
</code></pre>


</section>
