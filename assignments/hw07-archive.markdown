---
layout: homework
title: "Assignment #7"
---

<style>

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

# Assignment #7 - Due Monday, April 25th

In this assignment, you'll be building a single web application in flask (which you'll upload to NYU Classes as a zip file). The web application will will allow users to:

* submit final project proposals
* view final project proposals
* ...and view a report that counts the modules used on all of the proposals

Although this is a single project, it's broken down into multiple parts. Each part builds off of the previous, so try to avoid skipping parts. There's also some extra credit available at the end of the assignment. __To submit the project, you'll have zip up the directory that all of your files are in, and upload that to NYU Classes__.

* __Part 1__ - readings
* __Part 2__ - images/css, common markup, homepage
* __Part 3__ - view projects
* __Part 4__ - add project
* __Part 5__ - report
* __Project Submission__ 
* __Extra Credit__ 
    * (easy / medium) report visualization
    * (medium) checkboxes
    * (hard) report detail

Here's what it'll look like when you're done!

![all animated](../resources/img/hw07-07-all.gif)

## Part 1 - Readings

#### Online Resources


* skim through [flask's quickstart guide](http://code-maven.com/using-templates-in-flask) to get an idea of what it can do!
* you might want to check out [handling forms in flask](http://code-maven.com/using-templates-in-flask) for a more complete tutorial of dealing with forms
* the [jinja2 docs](http://jinja.pocoo.org/docs/dev/templates/) are a good reference for templating

#### From notes

* [flask examples from class 20](https://github.com/jversoza/p4a-spring-16-examples/tree/master/p4a-class20)
* [flask examples from class 21](https://github.com/jversoza/p4a-spring-16-examples/tree/master/p4a-class21) (this contains a very simple form example!)


## Part 2 - images/css, common markup, homepage

In this part, you'll set up your flask project, create a directory for css and images, create a template, and add content for your homepage. The links in the instructions take you to the relevant documentation.

#### Setup

1. install flask
2. create a [minimal flask application](http://flask.pocoo.org/docs/0.10/quickstart/#a-minimal-application) in a file called <code>app.py</code> (it should have a single route that responds to <code>/</code> or just <code>localhost:5000</code>)
3. __make sure to set <code>app.debug = True</code>__ as shown in the [documentation on turning on debug mode](http://flask.pocoo.org/docs/0.10/quickstart/#debug-mode)
4. test your homepage by:
    * running your application in PyCharm (simply run... and make sure there are no other instances running by pressing stop before running again) or through terminal
    * opening <code>http://localhost:5000/</code> in your browser

#### Technical Requirements

The homepage responds to <code>http://localhost:5000/</code> or just <code>/</code> for short (we'll ignore the domain and port when we discuss paths).

1. modify your route for <code>/</code> (root) so that it [renders a template](http://flask.pocoo.org/docs/0.10/quickstart/#rendering-templates) instead of returning a string (ignore passing a keyword argument to the template for now)
    * create a <code>templates</code> directory in the same directory as your <code>app.py</code>
    * create a template file within that directory, name it whatever you like
    * <code>import</code> and <code>return</code> the result of calling the <code>render_template</code> function (you can skip passing in keyword arguments... just the template name will suffice for now: <code>render_template("my_tepmlate.html")</code>)
2. common markup, such as navigation, <code>html</code>, <code>head</code>, a <code>link</code> tag for css, etc. can be included using a _parent_ template, which is covered [the documentation on template inheritance](http://flask.pocoo.org/docs/0.10/patterns/templateinheritance/) 
    * create a parent template 
    * in the parent template...
        * add a header that contains a title for the entire site
        * create  basic markup for an html document
        * add navigation to link to the following urls:
            * <code>/</code> (home)
            * <code>/projects</code> (add / view projects)
            * <code>/report</code> (summary of modules used)
    * in your child template...
        * inherit from the parent using a combination of <code>extends</code> and <code>block</code> 
        * add text that explains that the site is for adding and viewing project proposals
        * add another link to <code>/projects</code>
        * add another link to <code>/report</code>
3. add styles to your page by using the [static directory to server images, css, etc.](http://flask.pocoo.org/docs/0.10/quickstart/#static-files) (you can ignore the part about using <code>url_for</code>, but feel free to use it if you like!)
    * create a <code>static</code> directory
    * within that directory, add your css file (you can add a subdirectory if you like)
    * change your parent template so that it has a <code>link</code> tag that references your css
    * for example, if your css is in <code>static/styles.css</code> your <code>link</code> tag should include the attribute: <code>href="/static/styles.css"</code>



Here's what the homepage could look like (you can style it however you like, and your content can be slightly different, as long as it includes a header, navigation and links in the body):

![home](../resources/img/hw07-01-home.png)

## Part 3 - view projects

Now that you've created a home page with links to other parts of the site, it's time to start implementing those _other pages_. Let's start with the page to view and add projects.


#### Setup

* make sure that part 1 is complete...
* which includes a <code>templates</code> and <code>static</code> directory
* a base / parent template file
* common elements across all pages, such as navigation, a reference to css, etc.
* with __debug mode turned on__

#### Technical Requirements

In our application, we'll simply store all of the project proposals in a global variable. The global variable will be a list. Each project proposal will be represented by a dictionary in that list. A project proposal dictionary will have the following keys:

* <code>netid</code> - a string representing the netid of the person submitting the proposal
* <code>title</code> - a string representing the project's title
* <code>description</code> - a string representing the project's description
* <code>modules</code> - a list of strings that represents the modules that will be used for the project

Of course, this has the downside of the project list disappearing every time the server restarts. Because of this, we'll start off with _pre-populating_ our global variable of project proposals with some submissions to make testing easier. Once we have some proposals to view, we'll create another template to go through every project proposal and show some information about it.

The page that displays projects will be accessible at <code>/projects</code>.

1. create a global variable called <code>project_proposals</code>; you'll use this hold all project proposals submitted:
    <pre><code data-trim contenteditable>project_proposals = [
    {
        "netid": "abc123",
        "title": "Pizza on U",
        "description": "A site that adds a slice of pizza to images",
        "modules": ["flask", "pil"]
    },        
    {
        "netid": "xyz789",
        "title": "Catfinity",
        "description": "Creates a collage of random cat images",
        "modules": ["pil", "requests"]
    },        
    {
        "netid": "ynot42",
        "title": "hippost",
        "description": "An image board for hippo enthusiasts",
        "modules": ["flask", "pil"]
    }        
]
</code></pre>
2. create a route to handle requests to <code>/projects</code>
3. in the function that handles requests to <code>/projects</code>...[ render a template and pass some variables to the template](http://flask.pocoo.org/docs/0.10/quickstart/#rendering-templates)
    * again, this means using <code>render_template</code>
    * however, this time around, pass variables to your template using keyword arguments: <code>render_template('a_template_with_variables.html', variable_name_1="some value")</code>

    * the variable that you'll pass should be the global variable (the list of dictionaries) or projects, <code>project_proposals</code>
3. display the contents of the variable that you pass into the template by using [for loops](http://jinja.pocoo.org/docs/dev/templates/#for) (you can remove the <code>|e</code> part from the examples) and accessing [dictionary values through keys](http://jinja.pocoo.org/docs/dev/templates/#variables)
    * use curly braces and percent symbols (<code>&123;% ... %&125;</code>) to use templating control structures, like loops
    * use curly braces to output the contents of a variable <code>&123;&123; ... &125;&125;</code>
    * loop through all of the projects
    * output the <code>netid</code> and <code>title</code> of the project (dot notation will be useful here, as outlined in the linked documentation: <code>&123;&123; my_dictionary.some_key &125;&125;</code>)
    * put this information in a table or unordered list
    * note that __tags within a for loop will be reapeated__ (_nice!_)

Here's what the project list page could look like (you can style it however you like, but make sure that it lists all of the pre-populated project proposals):

![project list](../resources/img/hw07-02-list.png)

### Part 4 - add projects

In the same page that you view projects, you should also be able to add projects. To do this you'll have to work with forms.

#### Setup


* make sure that part 3 is complete...
* which includes a route that handles the url <code>/projects</code>
* ...and a global variable that contains project proposals as a list of dictionaries
* ...and, of course, a page that shows the list of project proposals

#### Technical Requirements

In this part, you'll add a project proposal to your list of proposals by using forms! 

* we did quick [example in class](https://github.com/jversoza/p4a-spring-16-examples/tree/master/p4a-class21/flask-form)
* ...and there's [this tutorial](http://code-maven.com/using-templates-in-flask) too

Basically, you'll need to create a form on your <code>/projects</code> page. All of the fields are text inputs. __Note that the list of modules is sent as a comma separated list of modules__.

![project add](../resources/img/hw07-03-add.png)

When you click on the submit button of the form, it'll send a <code>POST</code> to your web application. The function that handles <code>/projects</code> will see <code>POST</code> and add the data by [accessing request attributes through the <code>request</code> object](http://flask.pocoo.org/docs/0.10/quickstart/#the-request-object). The function should finish up by redirecting back to <code>/projects</code> using [flask's <code>redirect</code> function](http://flask.pocoo.org/docs/0.10/quickstart/#redirects-and-errors).

1. modify the template that you render for <code>/projects</code> by adding a form to it:
    * add a form above your list of projects
    * the form should have a <code>method="POST"</code> and <code>action=""</code>
    * this means that pressing the submit button will issue a <code>POST</code> to <code>/projects</code> (if action is empty string, it defaults to the same page that the form is on, which is <code>/projects</code>)
    * you can make all of your form elements <code>input</code>s, with <code>type="text"</code>
    * for example: <code>&lt;input type="text" placeholder="" name="netid" value=""&gt;</code>
    * the new <code>/projects</code> page with both the form and list of projects should look like this (again, you can style it however you like):
        <br>
        ![project list and add](../resources/img/hw07-04-list-add.png)
2. in your <code>app.py</code> modify the function that gets called for <code>/projects</code> so that it looks at incoming <code>POST</code> requests and adds a new project based on that request
    * make sure to <code>import</code> request
    * examine <code>request.method</code> to determine if the request is a <code>POST</code> or a <code>GET</code>
    * if it's a <code>GET</code> render the template that contains your form and list of projects like usual
    * however, if it's a <code>POST</code> [access the data that was sent via the form using the <code>request</code> object](http://flask.pocoo.org/docs/0.10/quickstart/#the-request-object)
    * create a dictionary with the appropriate keys using the data above...
    * note that the input for modules is a single comma separated list of module names... so you'll have to convert that to a list!
    * add the dictionary to your global list of projects
    * __the most recently added projects should show up at the top of your list of projects__
    * once you've done that, the client should get back some sort of response...
    * instead of rendering a template, send back a redirect so that the browser issues another <code>GET</code> to <code>/projects</code>
    * to do this, <code>import</code>  <code>redirect</code> [and use to send back a redirect response](http://flask.pocoo.org/docs/0.10/quickstart/#redirects-and-errors)
    * it should look something like <code>return redirect('/projects')</code>
    * so... the pseudocode for all of this looks like:
        <pre><code data-trim contenteditable>if request method is GET
    render your template
else... if request method is GET
    create a new dictionary
    pull data from the form submissions (via request.form)
    add dictionary to global list of project submissions
    return a redirect to /projects
</code></pre>
    * by the way, if you're curious, a redirect looks just like any other http response (flask's <code>redirect</code> function will send this back):
        <pre><code data-trim contenteditable>HTTP/1.1 303 See Other
Location: /projects
</code></pre>
* he screen capture below shows a new project being added... with __the last project added being shown at the top__ of the table of projects after the form is submitted
    <br>
    ![project list and add animated](../resources/img/hw07-05-list-add.gif)


### Part 5 - report

Your last page will be a report showing the number of times a python module was submitted as part of a project. 

#### Setup

* make sure that part 4 is complete...
* which is the complete implementation of the <code>/projects</code>
    * viewing projects
    * adding projects
* this part requires that you've completed the previous parts as well... to ensure that there's some data for the report to display

#### Technical Requirements

1. add another route that renders a template
2. this time, instead of passing in the list of <code>project_proposals</code> ... you'll have to pass in the counts of all the modules used in all of the proposals
    * the order of the modules doesn't matter, so a dictionary is ok
    * iterating over a dictionary is [covered in the templating docs](http://jinja.pocoo.org/docs/dev/templates/#for) (that is, use <code>iteritems()</code>
3. here's what the report may look like:
    <br>
    ![project report](../resources/img/hw07-06-report.png)

### Submitting Your Project

__Zip up the directory that your project is in, and upload it to NYU Classes__

### Extra Credit

Add one or more of the following features for extra credit:

1. (easy-medium) add a visual component to the report
    * you can implement the visualization any way you like
    * (so it can be as easy or complex as you make it!)
    * the example image below was implemented by using a div with a green background color and with space for text... that's sized based on the number of times a module appears in the list of globals
    * (but you can use any visualization you want... like an svg pie chart, sure! ...an interactive canvas tag, ok!)
        <br>
        ![ec report](../resources/img/hw07-08-report-ec.png)
2. (medium) use checkboxes instead of a single text field for modules 
    * you'll have to research how checkboxes are created
    * ...and how the values appear in <code>request.forms</code>
    * (it's ok to just use a preset number of modules/checkboxes) 
    * here's what the new version of your form may look like:
        ![ec checkbox](../resources/img/hw07-09-checkbox-ec.png)
3. (hard) create a detail page that displays __all of a project's information__
    * the detail page should be linked to for every project listed in <code>/projects</code>
    * the url of the detail page should be <code>/projects/<title></code> where title is the lowercase version of the title with all spaces substituted with underscores
    * for example <code>/projects/pizza-on-u/</code> would pull up a project titled <code>pizza-on-u</code>
    * capture the last part of the url in your route's function
    * the docs on [variable rules](http://flask.pocoo.org/docs/0.10/quickstart/#variable-rules) show how to do this
    * retrieve the project with that title from your gobal list of <code>project_proposals</code>
    * pass the project to your template
    * display the <code>title</code> and <code>netid </code>as a header
    * display the remainder of the details, <code>description</code> and <code>modules</code> in any way you like
    * here's an example of what the detail page may look like (note the url!)
        <br>
        ![ec detail](../resources/img/hw07-10-detail-ec.png)
