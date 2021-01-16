"""
clicky.py (5 points)
=====
Create a turtle program that draws circles every time you click on the screen.
Each circle will be a different color based on where the screen is clicked:

http://foureyes.github.io/csci-ua.0002-spring2015-008/resources/img/click-circles.gif

Check out the animated gif!

The program is already half written for you. However, there are 7 parts 
missing. The first part is the function definition. The remaining 6 parts
take you step-by-step on how to create a program that responds to clicks (you
just need to write the appropriate code below each comment).

Each step is numbered accordingly.
"""

import turtle
t, wn = turtle.Turtle(), turtle.Screen()

# turn animation of turtles off
t.hideturtle()
wn.tracer(0)

# set the width and height of our screen
width, height = 500, 500
wn.setup(width, height)

# 1. Create a function called get_quadrant_color:
#    a. it should have two parameters, click_x and click_y
#    b. the parameters represent the coordinates of where the mouse was when
#       when the screen was clicked
#    c. the function should return a string representing one of the following
#       four colors: red, green, blue and yellow
#    d. determine what color to give back based on what quadrant the user
#       clicked on:
#       * red - upper right
#       * green - lower right
#       * blue - upper left
#       * yellow - lower left
#  
# =====================================

# (define get_quadrant_color here!)


def handle_click(x, y):
    # 2. pick your pen up
    # =====================================


    # 3. move your turtle to the x and y coordinates that are the parameters
    #    of this function
    # =====================================


    # 4. put your pen back down
    # =====================================


    # 5. call your get_quadrant_color function here and save save the result 
    #    in a variable called quadrant_color
    # =====================================


    # 6. set the turtle's drawing color to the quadrant_color variable that 
    #    you created above
    # =====================================


    # 7. draw a filled circle by calling the following methods on your
    #    *turtle object* in order:
    # 
    #    begin_fill()
    #    circle() <--- circle has radius as a parameter
    #    end_fill()
    # =====================================


# when the screen is clicked, call the handle_click function (and pass it the
# x and y coordinates
wn.onclick(handle_click)

wn.mainloop()
