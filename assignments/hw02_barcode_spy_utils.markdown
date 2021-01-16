---
layout: homework
title: "Assignment #2"
---

<style>
img {
    border: 1px solid #000;
}
</style>

# Assignment #2 - Due Friday, February 12th

(Since the assignment was posted later than last weeks', it's due a day later... and I can extend the open date for NYU Classes further upon request)

## Part 1 - Readings

Check out __Chapter 3, Codes and Other Secrets__ in {{ site.book1 }}.  This chapter provides background information for Parts 2, 3, 4 and 5.

## Part 2 - Spy Tools

#### Setup

* [Download spytools.py](../assignments/hw02/spytools.py)

#### Complete Missing Function Definitions

You're an undercover, and you just received an urgent encrypted message. 
You'd like to figure out what the message says, and reply to it using
the same encryption scheme. You decide to use a python module that you
found online... called spytools.py. Unfortunately, the module only supports 
encryption (with simple ciphers at that, but whatevs!). Bummer. You'll 
have to write the decryption functionality yourself. At least there's
already some code there for you!

4 of the functions defined in the file are missing from spytools.py. 
implementations. Finish the implementations of these functions according 
to the instructions in the file and the docstrings for each function:

1. <code>gen_consecutive_chars()</code>
2. <code>gen_key(password)</code>
3. <code>sub_decrypt(password, ciphertext)</code>
4. <code>vig_decrypt(key, message)</code>

## Part 3 - Such Secret

#### Setup

* [Download secret_message.py](../assignments/hw02/secret_message.py)

#### Create an Interactive Console Application

Write an interactive console program that allows a user to encrypt or
decrypt a message using either a substitution cipher or the vigenère
cipher. Use the <code>spytools</code> module you modifed to encrypt and decrypt
messages.

1. Continually ask the user if they want to <code>(e)ncrypt, (d)ecrypt or
(q)uit</code>.
2. If the user types in <code>e</code>, ask which cipher they would like to use:
<code>(s)ubstitution cipher or the (v)igenère cipher</code>
    * if the user picks <code>(s)ubstitution</code>:
        * ask for the password and the message
        * encrypt the message and print out the ciphertext
    * if the user picks <code>(v)igenère</code>:
        * ask for the key and the message
        * encrypt the message and print out the ciphertext
    * if the user does not pick <code>s</code> or <code>v</code>
        * print out an error message
        * ask for a new command, encrypt or decrypt
3. If the user types in <code>d</code>, ask which cipher the message was encrypted in
<code>(s)ubstitution cipher or the (v)igenère cipher</code>
    * if the user picks <code>(s)ubstitution</code>:
        * ask for the password and the encrypted message
        * decrypt the message and print out the plain text
    * if the user picks <code>(v)igenère</code>:
        * ask for the key and the encrypted message
        * decrypt the message and print out the plain text
    * if the user does not pick <code>s</code> or <code>v</code>
        * print out an error message
        * ask for a new command, encrypt or decrypt
4. If the user types in <code>q</code>, end the program
5. If the user types in any other letter
    * print out and error message
    * ask for a new command, encrypt or decrypt

__Example Interaction__

<pre><code data-trim contenteditable>TOP SECRET SPY STUFF!
Hi... would you like to (e)ncrypt or (d)ecrypt a message.. or (q)uit?
> e
What cipher would you like to use: (v)igenère or (s)ubstitution)
> v
Enter a key to encrypt your message with
> DAVINCI
Enter a message to encrypt
> the eagle has landed
whz rcooe pnu oailrf
Hi... would you like to (e)ncrypt or (d)ecrypt a message.. or (q)uit?
> d
What cipher would you like to use: (v)igenère or (s)ubstitution)
> v
Enter a key to decrypt the ciphertext
> DAVINCI
Enter the cyphertext to decrypt
> whz rcooe pnu oailrf
the eagle has landed
</code></pre>

## Part 4 - UPC Functions

#### Setup

* [Download upc.py](../assignments/hw02/upc.py)

#### Write Functions

Create a program that will generate a UPC barcode. In this part, you'll
write some helper functions for your program. (Part 5 will use these
functions to _actually_ generate a barcode based on user input). __We'll
be using UPC-A__, which consists of 12 digits.

It'll be helpful to read up a little bit on UPC barcodes. Some resources 
that you may find useful include:

* [The wikipedia article on UPC](https://en.wikipedia.org/wiki/Universal_Product_Code#Encoding)
* [A page on howstuffworks that has a mapping of numbers to bar widths](http://electronics.howstuffworks.com/gadgets/high-tech-gadgets/upc3.htm)
* [A guide on UPC barcodes from www.adams1.com](http://www.adams1.com/upccode.html)

In this part, implement the following two functions as specified in the 
docstrings in <code>upc.py</code>:

1. <code>generate_bar_widths(s)</code>
2. <code>valid_barcode(s)</code>

## Part 5 - Barcode Maker

#### Setup

* [Download barcode_maker.py](../assignments/hw02/barcode_maker.py)

#### Create a Program That Generates a UPC-A Barcode

Using the <code>turtle</code> module and your <code>upc.py</code>, 
create a program that:

1. Asks the user for a barcode
    * You can use the <code>Screen</code> object's <code>textinput</code> method to ask for a barcode:
    <br>
    <pre><code data-trim contenteditable># Screen object
wn = turtle.Screen()
barcode_number = wn.textinput('barcode', 'Please enter a barcode')
</code></pre>
    * See the [official documentation](https://docs.python.org/3.5/library/turtle.html#turtle.textinput)
2. Checks if the barcode is valid (use the appropriate function from <code>upc.py</code>)
3. Draws a barcode if the barcode entered is valid
    * __writing out the numbers of the barcode is optional__
    * the examples below treat a single width bar as 3 pixels, but you can use whatever dimensions work best for you
    * check out the animated gif for entering a valid barcode
    <br>
    ![valid](../resources/img/hw02_valid.gif)
4. If the barcode is not valid:
    * asks for another barcode
    * with the text on the prompt displaying an error message
    <br>
    <pre><code data-trim contenteditable># if the previous input was not valid...
barcode_number = wn.textinput('barcode', \
    'NOT A VALID BARCODE\n\nPlease enter another barcode')
</code></pre>
    * check out the animated gif that shows an error message:
    <br>
    ![not valid](../resources/img/hw02_not_valid.gif)
5. You can try out your barcode by getting a barcode scanning app for your phone!
    * [For iphone, you can try](http://www.igeeksblog.com/best-barcode-qr-code-scanning-apps-for-the-iphone/)
    * [One of these might work if you're on Android](http://www.androidheadlines.com/2015/02/featured-top-10-barcode-qr-scanner-apps-android.html)
    * I used QR Scanner for iPhone in the screenshots below:
    <br>
    ![scan](../resources/img/hw02_scan_small.png)
    <br>
    ![scan result](../resources/img/hw02_scan_result_small.png)




{% comment %} 
![valid](../resources/img/hw02_valid.gif)
{% endcomment %} 


