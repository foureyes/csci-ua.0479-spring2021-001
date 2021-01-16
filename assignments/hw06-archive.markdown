---
layout: homework
title: "Assignment #6"
---

<style>
img {
    border: 1px solid #000;
}

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}

.highlight {
    background-color: yellow;
    font-weight: bold;
}
</style>

# Assignment #6 - Due Friday, April 15th

* __Part 1__ readings
* __Part 2__ talk_to_me_server.py 
* __Part 3__ web_server.py, web_app.py, web_objects.py
    * extra credit for part 3
* __Part 4__ flasky.py
    * extra credit for part 4

## Part 1 - Readings

#### From our Book

You'll need to review __Chapter 10 (Astronomny)__ in {{ site.book1 }} to get a refresher on classes and objects.

#### From notes

* [definitions](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class16/sockets.md)
* [bytes](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class16/bytes_isinstance_print.md)
* [sample code for simple echo_server.py](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class17/echo_server.py)
* [a server that responds to multiplication and addition requests: math_server.py](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class16/math_server.py)
* __[a great starting point for this assignment, <span class="highlight">a sample web_server.py</span>](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class17/web_server.py)__

#### Online Resources

[Let's build a web server part 1](https://ruslanspivak.com/lsbaws-part1/)

## Part 2 - talk_to_me_server.py

You're tired of talking to _real_ people, so you decide to write a computer program that you can talk to. Over a network. Using sockets. So nerdy.

In this assignment, write a chat server. It'll accept connections... once it has a connection, it'll wait for a message. Every time it receives message, it'll send back a response, until the message that's sent to it is <code>bye</code>, <code>later</code>, or <code>ttyl</code> in any casing.

Check out the example interaction below:

![server](../resources/img/hw06_00_server.gif )

#### Setup

1. Download [talk_to_me_server.py](hw06/talk_to_me_server.py)  
2. If you're on windows, you may need to search for a windows version of __netcat__ to test your chatty server

#### Technical Requirements

1. Set up a socket for listening for connections. 
    * <span class="highlight">You can use the code examples for the [echo_server.py](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class17/echo_server.py) or the [math_server.py](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class16/math_server.py) for this part.</span>
    * specifically, create a socket
    * bind it to a port
    * start listening
    * then start looping infinitely so you can start accepting connections
    * accept any incoming connections
    * read up the first bits of data
2. <span class="highlight">From this point, your server will differ from the example code linked to above</span>
3. As long as there's data coming in from the client, keep the connection open, and keep reading the incoming messages (and decoding them into strings)
4. Depending on the message that's sent, your server will respond in different ways:
    * if the client sends <code>hi</code>, <code>hello</code>, <code>howdy</code>, <code>hey</code>, or <code>hola</code> __in any casing__, the server will:
        * respond with <code>'Hi there!'</code>
        * and grab the next data... at which point the entire process of decoding into a string and responding based on the content of that string repeats
    * if the client sends <code>bye</code>, <code>later</code>, or <code>ttyl</code> __in any casing__...
        * the server will say "Goodbye!"
        * and it will __close the connection with this particular client immediately__
    * if the client says something other than the above messages, then the chat server will reply with some random phrase of acknowledgement (like, <code>That's interesting</code> or <code>Sounds good!</code>)
5. So... this means that the general flow of your server __after it <code>accept</code>s a connection__ and __receives its first bits of data will be__:
    <pre><code data-trim contenteditable>as long as there's data (while data...)
    decode the data into a string
    remove any new lines from the data using strip
    if the client says bye
        send back "Goodbye!"
        ...and immediately disconnect (call close on the client socket)
    otherwise...
        if it's a greeting
            respond with a greeting (send)
        if it's not a greeting
            then respond with a random phrase of generic acknowledgement
        right after a reponse is sent...
        get more data from the client (recv)
</code></pre>
6. You can test interacting with the server using a program called netcat:
    1. start your server through PyCharm or the terminal
    2. open terminal.app on OSX
    3. type in <code>nc localhost 5000</code>
    4. start typing in messages to chat with your server!
    5. say <code>bye</code> to disconnect
    6. here's an example of an interaction, with the text in parentheses being the responses from the server:
        <pre><code data-trim contenteditable>nc localhost 5000
hello
(Hi there!)
I'm doing my homework
(Oh really?)
It's really fun!!!
(Uh-huh, ok.)
bye
(Goodbye!)
</code></pre>

## Part 3 - web_server.py, web_app.py, web_objects.py

Recreate the bare-bones dungeons and dragons / role playing game site from the example code in our [original version of web_server.py](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class17/web_server.py) ... by splitting up the functionality into 3 parts and creating objects that represent http requests and responses.

#### Setup

The files below are a _refactored_ (rewritten) version of the web server example from one of our previous classes. In this new version, <code>web_server.py</code> imports <code>web_app.py</code>, which imports <code>web_objects.py</code>. Each file has its own set of responsibilities:

1. Download [web_server.py](hw06/web_server.py) - this is the file you'll run to actually _serve_ the site (it's in charge of accepting and closing connections)
1. Download [web_app.py](hw06/web_app.py) - this contains all of the _routes_ of your web app, that is, what urls your site will respond to
2. Download [web_objects.py](hw06/web_objects.py) - this contains your implementations of a <code>Request</code> class and a <code>Response</code> class

<code>web_server.py</code> is complete, but parts of the other two files are missing. Follow the directions below so that your site responds to:

* <code>http://localhost:5000/</code>
* <code>http://localhost:5000/creatures</code>
* <code>http://localhost:5000/dice</code>

See the sample interaction below:

![site](../resources/img/hw06_01_overview.gif )

#### Technical Requirements

__First implement two classes that will allow you to create objects representing http requests and responses__. In <code>web_objects.py</code> ...

* <code>Request</code> class:
    * should represent an http request
    * it should have a constructor that takes a string representation of an http request ... and parses that string to fill in the properties listed below (create an <code>__init__</code> method that takes a string)
    * [read up on http](https://ruslanspivak.com/lsbaws-part1/) and [check out the class notes](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class19/http.md) and [initial server implementation](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class17/web_server.py) parse an http request
    * it should have the following properties (assuming that <code>req</code> is an instance of <code>Request</code>) once the http request is parsed:
        * <code>req.path</code> - the path requested
        * <code>req.method</code> - the request method (GET, PUT, POST, etc.)
        * <code>req.http_version</code> - the http version of the request
        * <code>req.headers</code> - a dictionary of http request headers
        * <code>req.body</code> - the body of an http request
    * __hints__:
        * remember that each line in an http request is separated a carriage return and a line feed, which, as a literal string would be: <code>\r\n</code>
        * notice that body of an http request comes after a blank line, so that would mean two consecutive <code>\r\n</code>s
    * lastly the string representation of a <code>Request</code> object (that is, implementing the special <code>__str__</code> method), __should give back the original string that the object was parsed from__
    * for example, if the http request looks like this (note that this is a GET request without a body):
        <pre><code data-trim contenteditable>GET /dice HTTP/1.1
User-Agent: p4a browser ftw! 
Host: localhost:5000
Accepts: text/html
</code></pre>
    * then the object that represents it behaves like this:
        <pre><code data-trim contenteditable>req.path --> "/dice"
req.method --> "/GET"
req.http_version --> "HTTP/1.1"
req.headers --> {
    "User-Agent": "p4a browser ftw!",
    "Host": "localhost:5000",
    "Accepts": "text/html"
}
req.body --> "" (the request did not have a body)
req --> (as a string would give back the original http request text)
    * an example of parsing an HTTP POST would look like this:
        <pre><code data-trim contenteditable>POST /login HTTP/1.1
Host: my.awesome.site
Content-Length:32
Content-Type: application/x-www-form-urlencoded
&nbsp;
username=joe&password=pizza4life
</code></pre>
    * ... and the resulting object would have similar properties as the previous example, but it would also have a body property
        <pre><code data-trim contenteditable>req.body --> username=joe&password=pizza4life</code></pre>
    * finally, using the <code>Request</code> class would look like this...
        <pre><code data-trim contenteditable># assuming that s contains a string representation
# of an http request...
req = Request(s)
</code></pre>
        <pre><code data-trim contenteditable># now... req.path can be accessed
if req.path == '/':
    # do some stuff...
</code></pre>
        <pre><code data-trim contenteditable># if you want to see the original request, simply print out the object
print(req)
</code></pre>
* <code>Response</code> class:
    * should represent an http response
    * it should have a constructor (an <code>__init__</code> method) that takes an int as a parameter; the int represents the status code that will be returned
        * for now, it's ok if the constructor does not validate the number passed in
        * (though you can implement validation in the extra credit)
    * it should have the following methods:
        * <code>set_header(header_name, header_value)</code> - set an http response header
        * <code>set_body(body)</code> - set the body of the response
        * <code>set_status(status_code)</code> - change the status code from what it was initially set as
    * it should also contain a dictionary of status code descriptions accessible via class name (a _static_ variable)
        * call the dictionary <code>STATUS_TEXT</code>
        * you can access it via class name as shown below:
            <pre><code data-trim contenteditable>print(Response.STATUS_TEXT[200])
print(Response.STATUS_TEXT[404])
# &nbsp;
# prints out:
# OK
# Page not found
</code></pre>
        * here's an example of creating static variables:
            <pre><code data-trim contenteditable>class Circle:
    PI = 3.14
# notice that we don't need to create a 
# circle instance to access PI
print(Circle.PI)
</code></pre>
    * finally implement a <code>__str__</code> method so that printing out a <code>Response</code> object gives back a text version of the http response that it represents
        * take note of what an [http response should look like (scroll down to the section on http responses)](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class19/http.md)
        * __you can make all of your http responses__ have an http version of <code>HTTP/1.1</code>
        * you can get the description of your status code from the dictionary that you created above <code></code>
    * here's an example of how the <code>Response</code> class might be used:
        <pre><code data-trim contenteditable>res = Response(200)
res.set_header('Content-Type', 'text/html')
res.set_header('Server', 'p4a server ftw!')
res.set_body('&lt;h1&gt;stuff&lt;/h1&gt;')
print(res)
</code></pre>
    * ...and this is what the above code prints out
        <pre><code data-trim contenteditable>HTTP/1.1 200 OK
Content-Type: text/html
Server: p4a server ftw!
&nbsp;
&lt;h1&gt;stuff&lt;/h1&gt;
</code></pre>

__Once you have a Request and Response class, you can test your classes by adding the following code to <code></code>__

<pre><code data-trim contenteditable>if __name__ == '__main__':
    """
    POST /stuff/add HTTP/1.1
    User-Agent: p4a browser ftw!
    Host: localhost:5000
    &nbsp;
    foo=bar
    """
    # PARSE A STRING INTO AN HTTP REQUEST OBJECT
    http_req = "POST /stuff/add HTTP/1.1\r\nUser-Agent: p4a browser ftw!\r\nHost: localhost:5000\r\n\r\nfoo=bar"
    req = Request(http_req)
    print(req.path)
    print(req.headers)
    print(req.body)
    print(req)
    # CREATE A RESPONSE OBJECT AND PRINT IT OUT
    res = Response(200)
    res.set_header('Content-Type', 'text/html')
    res.set_header('Server', 'p4a server ftw!')
    res.set_body('&lt;h1&gt;stuff&lt;/h1&gt;')
    print(res)
</code></pre>

__Once you have <code>Request</code> and <code>Response</code> working, fill in the code missing from <code>web_app.py</code>__

There are two parts missing from <code>web_app.py</code>:

1. the implementation of <code>handle_request</code>
2. the implementation of the route that handles <code>/creatures</code>

<code>handle_request</code> is called from the server... and its job is take the raw, incoming http request and turn it into a response. It should do this following these steps:

1. create a <code>Request</code> object based on the incoming http request (this argument will be passed in to <code>handle_request</code> from <code>web_server.py</code>, which is already complete and written)
2. based on the path of the http request, get the right "route" (function that will generate the appropriate response... that is one of the functions above)
3. if the route exists, call the appropriate function with the request object as a parameter... 
4. add any headers necessary to the resulting <code>Response</code> object
    * [here's a list of headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Response_fields)
    * __hint__ you'll only really need one of these headers to make sure that the browser knows what to do with the response body
5. if the route doesn't exist, create a <code>Response</code> object with a status code of <code>404</code> and a body of <code>"Not Found"<.code>
6. return the resulting <code>Response</code> object from the either of the two previous steps as a string (just use <code>return str(my_response_object)</code>)

Test that everything works by:

1. running <code>web_server.py</code> in PyCharm or terminal
2. opening <code>localhost:5000</code> in your browser
3. verifying that a page is given back!

Lastly, finish the route for <code>/creatures</code>

1. the route should return an unordered list of creatures
2. the list should have a random number of creatures in it, minimally 1... and at most 4
3. the creatures in the list should be randomly picked as well
4. check out the example interaction below:

![site](../resources/img/hw06_02_creatures.gif )

Once your done, try running <code>web_server.py</code>. You should now be able to type the following urls in your browser:

* <code>http://localhost:5000/</code>
* <code>http://localhost:5000/creatures</code>
* <code>http://localhost:5000/dice</code>

__Extra Credit__

Implement any combination of the following features for extra credit:

1. (EASY) prevent <code>Response</code> objects from being made with status codes other than <code>200</code> and <code>404</code>
    * instead, validate the status code in your <code>Response</code> object's constructor
    * default to <code>200</code> if the status code is not known / supported
2. (MEDIUM) If there's no host header, give back a <code>400</code>!
    * check out the headers dictionary on the <code>Request</code> object formed from the incoming http request
    * if it doesn't contain a <code>Host:</code> header, then give back a <code>400</code> as your response, with a body of <code>"bad request"</code>
    * this also means that:
        * you'll have to add a <code>400</code> to your dictionary of status codes and descriptions
        * ...and if you implemented extra credit #1, accept <code>400</code> as a valid status cod
3. (HARD) In addition to path, have your route decorator accept another argument representing request method:
    * <code>route('GET', '/my/path'</code>)
    * this will allow you to have different functions be called  depending on whether or not a <code>GET</code> to <code>/my/path</code> is issued ... vs a <code>POST</code>
    * of course, this means that when you retrieve your function from the <code>routes</code> dictionary, you'll have to use a tuple of the method and the path as the key!

## Part 4 - flasky.py

Create a "hello world" flask application. Flask is module for creating web applications.

This last part is simply to make sure that you're able to install flask and get it running. There's also some straightforward (maybe fun?) extra credit that you can do with it.

#### Setup

1. Install flask via PyCharm or pip
2. Create a file called __flasky.py__

#### Technical Requirements

__Create a hello world flask application__. In flasky.py, add the following code:

<pre><code data-trim contenteditable>from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

app.run()
</code></pre>

Run your program through PyCharm... and open <code>localhost:5000</code> in the browser. You should see "hello world" displayed (such exciting!).

__Extra Credit__

Make your hello world as gaudy, garrish, and glaring as you can by using flask's template and static file features. Include a css file from your <code>static</code> directory and create a template in your <code>templates</code> directory.

Here's my version of a gaudy, garrish, and glaring hello world page:

![site](../resources/img/hw06_04_hello.gif )
