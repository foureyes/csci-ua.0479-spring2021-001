"""
from PIL import Image
img = Image.new('RGB', (400, 300))
import random
pixels = img.load()
width, height = img.size
for x in range(width):
    for y in range(height):
        pixels[(x, y)] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
img.show()
"""
"""
from PIL import Image
def add_lines(img, spacing, stroke_width, color):
    pixels = img.load()
    w, h = img.size
    for x in range(0, w, spacing + stroke_width):
        for s in range(stroke_width):
            for y in range(h):
                if x + s < w:
                    pixels[(x + s, y)] = color 

img = Image.new('RGB', (400, 300), (255, 255, 255))
add_lines(img, 20, 5, (255, 0, 0))
img.show()
"""
"""
from PIL import Image
img = Image.open('/tmp/wallaby.jpg')
img.show()
"""
from PIL import Image
from functools import partial
def pixel_map(img, f):
    pixels = img.load()
    w, h = img.size
    for x in range(w):
        for y in range(h):
            pixels[x, y] = f(pixels[x, y])

def to_bw(thresh, color):
    avg = sum(color) // len(color)
    if avg > thresh:
        return (255, ) * len(color)
    else:
        return (0, ) * len(color)


"""
img = Image.open('/tmp/wallaby.jpg')
#pixel_map(img, lambda color: (255, color[1], color[2]))
#new_to_bw = partial(to_bw, 210)
#pixel_map(img, new_to_bw)
pixel_map(img, lambda color: (255,) * 3 if sum(color) // len(color) < 150 else (0, ) * 3)
img.show()

"""
def mix(img1, img2, w=0.5):
    img = Image.new('RGB', img1.size)
    pix1, pix2, pix_new = img1.load(), img2.load(), img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            c1 = pix1[x, y]
            c2 = pix2[x, y]
            c =  (int(c1[0] * w + c2[0] * (1 - w)),
                    int(c1[1] * w + c2[1] * (1 - w)),
                    int(c1[1] * w + c2[1] * (1 - w))
            )
            pix_new[x, y] = c
    return img
def chromakey(src, dest, thresh=220):
    pix1, pix2 = src.load(), dest.load()
    for x in range(src.size[0]):
        for y in range(src.size[1]):
            c = pix1[x, y]
            if c[2] < thresh:
                pix2[x, y] = c
    return dest
space = Image.open('/tmp/space.jpg')
cat = Image.open('/tmp/grumpy.jpg')
#img = mix(space, cat, w=0.5)
#img = mix(cat, space, 0.8)
#img = chromakey(space, cat)
img = chromakey(cat, space, thresh=150)
img.show()









