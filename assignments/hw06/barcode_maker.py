"""
barcode_maker.py
=====
Use the turtle module and your upc module to:

1. Ask the user for a barcode
2. Check if the barcode is valid
3. If the barcode is valid, draw a barcode!
4. If the barcode is not valid:
    * ask for another barcode
    * the text on the prompt should display an error message

You can use the Screen object's textinput method to ask for a barcode:

# Screen object
wn = turtle.Screen()

# ask for a barcode
barcode_number = wn.textinput('barcode', 'Please enter a barcode')

# or... if the previous input was not valid...
barcode_number = wn.textinput('barcode', \
    'NOT A VALID BARCODE\n\nPlease enter another barcode')

See the official documentation:
https://docs.python.org/3.5/library/turtle.html#turtle.textinput
"""
