from PIL import Image
# don't install the library called PIL
# instead install pillow
#from PIL import Image
"""
Image.new(mode, dimensions, color)
where dimensions are a tuple
Image.open
"""
"""
img = Image.new('RGB', (800, 600), (255, 100, 155))
img.save('/tmp/only_red.jpg')
"""
"""
# 1 create new image
img = Image.new('RGB', (800, 600))

# 2 load the pixel data
# get pixel access object using load in image object
pixels = img.load()

# get width and height
# dimensions are in a tuple accessible from image object called .size
print(img.size) # (800, 600)
w, h = img.size

for x in range(w):
    for y in range(h):
        # key is actually a tuple representing coordinates of pixel
        pixels[(x, y)] = (0, 255, 0)
        # pixels[x, y] = (0, 255, 0)
        # pixels acts like a dictionary
        # read a pixel pixels[x, y]
        # write a pixel pixels[x, y] = (255, 255, 255)


#pixels[x, y] = (0, 255, 0)
img.show()
"""
"""
from PIL import Image
import random
# create an image .... that's composed of random colors for every pixel

#1. create a new image
# here... we get back an image object
img = Image.new('RGB', (600, 400))

#2. get the pixels
# from the image object, we can get a pixel access object
pixels = img.load()

#3. go through every pixel
w, h = img.size
for x in range(w):
    for y in range(h):
        # both loops will give us all coordinates for all pixels
        num = random.randint(0, 255)
        #4. set each pixel to a random color
        # pixels[x, y] = (num,) * 3 
        pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
img.show()
"""
"""
make an image
background: white
stripes every 10 pixels (each strip is 1 pixel wide)
each strip is black
"""
"""
from PIL import Image
img = Image.new('RGB', (600, 400), (255, 255, 255))
"""


"""
instead of drawing every space ... move by every space + stroke_width
either ... draw x lines from the right edge backwards or from the left edge forwards
"""
"""
def draw_stripes(img, space, stroke_width, color):
    pixels = img.load()
    w, h = img.size
    for x in range(0, w, space + stroke_width):
        # we want to repeat the drawing of a pixel line
        # as many times as there is the stroke width
        for s in range(stroke_width):
            for y in range(h):
                # prevent drawing outside of the width of the image
                if x + s < w:
                    pixels[(x + s, y)] = color 

    # not returning a value, instead changing dictionary itself
#draw_stripes(img, 10, 5, (255, 0, 0))
# draw_stripes(img, 23, (0, 0, 0))
img.show()
"""
# Image.open will take path to image
# absolute: '/Users/joe/Desktop/wallaby.jpg'
# relative: 'wallaby.jpg'
"""
img = Image.open('/tmp/wallaby.jpg')


def make_red(img):
    w, h = img.size
    pixels = img.load()
    for x in range(w):
        for y in range(h):
            color = pixels[x, y]
            pixels[x, y] = (255, color[1], color[2])

def make_gray(img):
    w, h = img.size
    pixels = img.load()
    for x in range(w):
        for y in range(h):
            color = pixels[x, y]
            pixels[x, y] = (sum(color) // len(color), ) * 3

# keyword argument
# now our function can have keyword argument
# if it's not passed in, then we have a default value
def foo(x, y=20):
    print(x, y)

#foo(100, y=-5)

def make_bw(img, thresh=255 // 2):
    w, h = img.size
    pixels = img.load()
    for x in range(w):
        for y in range(h):
            color = pixels[x, y]
            if sum(color) // len(color) > thresh:
                pixels[x, y] = (255, ) * 3
            else:
                pixels[x, y] = (0, ) * 3

def make_inverse(img):
    w, h = img.size
    pixels = img.load()
    for x in range(w):
        for y in range(h):
            color = pixels[x, y]
            pixels[x, y] = (255 - color[0], 255 - color[1], 255 - color[2])


# make a function that takes a function as an argument
# higher order function
def pixel_map(img, transform):
    w, h = img.size
    pixels = img.load()
    for x in range(w):
        for y in range(h):
            pixels[x, y] = transform(pixels[x, y])

"""

"""
def add_five(x):
    return x + 5

# anonymous function, in a single line
lambda x: x + 5
"""

"""
def to_bw(pixel):
    if sum(pixel) // len(pixel) > 255 // 2:
        return (255, ) * 3
    else:
        return (0, ) * 3
"""
"""
# make_inverse(img)
#pixel_map(img, to_bw)
# pixel_map(img, lambda pixel: (255, pixel[1], pixel[2]))
# pixel_map(img, lambda pixel: (255 - pixel[0], 255 - pixel[1], 255 - pixel[2]))
#pixel_map(img, lambda pixel: ((sum(pixel) // len(pixel),) * 3))
"""
def mix(img1, img2, w=0.5):
    #1. create a new image
    new_image = Image.new('RGB', img1.size)
    w, h = img1.size
    pixels1 = img1.load()
    pixels2 = img2.load()
    new_pixels = new_image.load()
    for x in range(w):
        for y in range(h):
            colors1 = pixels1[x, y]
            colors2 = pixels2[x, y]
            new_color = colors1[0] * w + colors2[0] * (1 - w), colors1[1] * w + colors2[1] * (1 - w), colors1[2] * w + colors2[2] * (1 - w)
            new_pixels[x, y] = new_color
    return new_image


space = Image.open('/tmp/space.jpg')
grumpy = Image.open('/tmp/grumpy.jpg')
new_img = mix(grumpy, space, w=0.5)
new_img.show()

































































































