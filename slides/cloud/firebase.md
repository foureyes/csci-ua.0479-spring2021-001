---
layout: slides
title: "Firebase"
---

<section markdown="block">
## A Database Instance

__Where can a database server _live_ (that is, where can a DBMS be "installed")?__ &rarr;

* {:.fragment} locally (like your local install of postgres or MongoDB)
* {:.fragment} on a remote computer, your own (procure rack space, purchase and install server in cage)
* {:.fragment} on a remote computer, shared with others (shared hosting, such as MongoDB on Courant)
* {:.fragment} installed on some _virtual server_ (EC2 instance)
* {:.fragment} offered as a service / _cloud_ (MongoDB Atlas)

</section>

<section markdown="block">
## Firebase

__Popular cloud database platform; some relevant services provided include__ &rarr;

* {:.fragment} Database products
	* Cloud Firestore 
	* Realtime Database
* {:.fragment} Firebase Hosting (static resource hosting)

</section>

<section markdown="block">
## Differences

See the [docs on Firebase Realtime Database vs Cloud Firestore](https://firebase.google.com/docs/firestore/rtdb-vs-firestore) for differences between the two database products &rarr;

* {:.fragment} [StackOverflow](https://stackoverflow.com/questions/46549766/whats-the-difference-between-cloud-firestore-and-the-firebase-realtime-database) also has a good summary
* {:.fragment} collections
* {:.fragment} nested documents (nested collections)
* {:.fragment} shallow queries (allows control of nesting depth in query results)
* {:.fragment} sounds a lot like mongodb, but has a lot of interesting features not found in mongodb (such as shallow queries, realtime updates from the server built-in)


</section>

<section markdown="block">
## Start, Creating an Account

Check out the [docs for getting started](https://firebase.google.com/docs/firestore/quickstart). __Start by going to the Firebase console and sign in or create an account__. &rarr;

1. {:.fragment} Go to [the Firebase homepage at https://firebase.google.com/](https://firebase.google.com/).
2. {:.fragment} Click on the `GO TO CONSOLE` link on the upper right of the user interface.
3. {:.fragment} Create an account or sign in:
	* Create a _throw-away_ google account in incognito mode if you don't want any personally identifiable information saved with google (you don't have to fill in a phone number when prompted to do so)...
	* __Or__ sign in with your nyu google account.

Note: When you create a Cloud Firestore project, it also enables the API in the Cloud API Manager.
{:.fragment}

</section>


<section markdown="block">
## Creating a Project

Once you're in the console [https://console.firebase.google.com/](https://console.firebase.google.com/?pli=1), __create a new project__ &rarr;

1. {:.fragment} Click on `Add project` (it's the button with a plus sign)
2. {:.fragment} Fill in the fields:
	* {:.fragment} Project name: ...
	* {:.fragment} Set the "parent" org
	* {:.fragment} Follow the prompts and opt in/out to analytics
	* {:.fragment} After creating your project, you should be redirected to your project page
</section>

<section markdown="block">
## Creating a Database

Create a database

1. {:.fragment} Click on `Firstore` in the left-hand navigation bar 
2. {:.fragment} When the menu opens up, click on `Create Database`... 
3. {:.fragment} Switch to `Test Mode` (if you're not using this for testing, make sure to [read the docs on securing your database](https://firebase.google.com/docs/firestore/security/get-started))
4. {:.fragment} Click on `Next`
5. {:.fragment} Set location
6. {:.fragment} Click on `Enable`

</section>



<section markdown="block">
## Creating Documents

__Manually creating documents__ &rarr;

1. {:.fragment} Click on `Start collection`
2. {:.fragment} In the `Collection ID` field, type in the name of your collection
3. {:.fragment} Add fields... and fill with any values:
4. {:.fragment} Try creating another document, but create different keys - notice that it's ok to do this!
5. {:.fragment} Try deleting the second document
</section>

<section markdown="block">
## Python and Firestore

__Install libraries that allow access to Firestore with Python__ &rarr;

* {:.fragment} `firebase-admin` - configuration, credentials, etc.
	* `pip3 install --upgrade firebase-admin`
	* `# or just pip if pip3 is unavailable`
	* `# you may need to use sudo`
* {:.fragment} you may need to install additional libraries if there's an error later on (for example, `google-cloud-firestore` which allows client access for create, read, etc. was not installed when this lab's reference solution was created, so it had to be installed manually)
</section>

<section markdown="block">
## Authentication Prep

__Download a JSON certificate keyfile for authenticating__ &rarr;

* {:.fragment} click on the gear icon in the left-hand navigation panel and then click on `Project settings`
* {:.fragment} click on the `Service accounts` tab
* {:.fragment} click on `Generate new private key`
* {:.fragment} download the file and keep note of its location
</section>

<section markdown="block">
## Authentication, Client

__Authenticate and create a client__ &rarr;

* {:.fragment} Create a new python file called `create.py`
* {:.fragment} Drop in the following code, substituting the correct path to your json keyfile
	```
# imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# authenticate
cred = credentials.Certificate('/PATH/TO/KEYFILE.JSON')
default_app = firebase_admin.initialize_app(cred)
# create client
db = firestore.client()
```
{:.fragment}
* {:.fragment} Print out db, run your script to see display a string representation of the client (`<google.cloud.firestore_v1beta1.client.Client object at 0x10ac1ff98>`)
</section>

<section markdown="block">
## Persisting Data

__Create a document reference and use it to set some values; these will be saved to the database!__ &rarr;

* {:.fragment} create a new document by creating a document reference:
	```
doc_ref = db.collection('collectionName').document()
```
* {:.fragment} add fields and values to this new document:
	```
doc_ref.set({
    'field1': 'value1',
    'field2': someObj2
})
```
* {:.fragment} Run your script... 
* {:.fragment} Click on the `Database` link in the navigation to see if your new scooter is in the database!
</section>


<section markdown="block">
## API, Hosting Intro

__Note__ When you create a Cloud Firestore project, it also enables the API in the Cloud API Manager.

* {:.fragment} This means that you can use _client-side_ JavaScript (that is, JavaScript running in the browser) to access the data you have in Firestore.
* {:.fragment} Additionally, Firebase allows __free hosting of static files__ (like html, images, etc.)

This is kind of a __big deal__: it basically allows you to build a _"serverless"_ web app that connects to a database in the cloud - can there be _any more buzzwords?_
{:.fragment}

</section>


<section markdown="block">
## Preparing to Add an App

Create an app to "show" data. We'll use a __frontend only web app__ &rarr;

1. Start a new _hosted_ web app
	* `Project Settings`
	* In heading `Select platform to get started`...
	* select &lt; &gt; for a web app
2. Give your app a name
3. Click on the hosting checkbox
4. Finally, go to hosting &rarr; `Get Started`

</section>

<section markdown="block">
## Create Frontend Only Web App

Install and use the commandline tools to create and deploy web app &rarr;

* {:.fragment} `npm install -g firebase-tools`
* {:.fragment} `firebase login` to authenticate
* {:.fragment} login w/ google account
* {:.fragment} `firebase init`
	* choose hosting
	* choose existing project
	* choose project you just created



</section>

<section markdown="block">
## JavaScript

__Add this JavaScript to `index.html` to read date form database and log from console.__ &rarr;

```
document.addEventListener('DOMContentLoaded', async function() {
    const loadEl = document.querySelector('#load');
	const db = firebase.firestore();
	const results = await db.collection('snakes').get()
	results.forEach((doc) => {
		let d = doc.data();
		console.log(d);
	});
});
```

</section>
{% comment %}

2. Start writing JavaScript to connect to your database 
	* add the following code between the script tags in your html file:
		<pre><code data-trim contenteditable>firebase.initializeApp({
  apiKey: '',
  authDomain: '',
  projectId: ''
});
</code></pre>
		<pre><code data-trim contenteditable>// Initialize Cloud Firestore through Firebase
const db = firebase.firestore();
</code></pre>	
		<pre><code data-trim contenteditable>// Disable deprecated features
db.settings({
  timestampsInSnapshots: true
});
</code></pre>
3. Configure the JavaScript client
	* Click on `Authentication` on the left-hand navigation panel
	* Click on `Web setup` on the upper right of the user interface
	* Fill in `apiKey`, `authDomain`, and `projectId` appropriately based on the values in the modal dialog box `Add Firebase to your web app`
4. Get all of the scooters from the database:
	* use the code below to retrieve all of the documents in the `scooters` collection
		<pre><code data-trim contenteditable>db.collection("scooters").get().then((querySnapshot) => {
  querySnapshot.forEach((doc) => {
    let d = doc.data();
    console.log(d.manufacturer, d.model, d.acquired, d.retired);
  });
});
</code></pre>
	* the code within the outer curly braces (after `then`) runs once the data has been received
	* the next line loops over every document
	* ...so within the inner curly braces, you have access to each scooter by calling `.data()` on the document, `doc`
	* you can treat JavaScript objects like Python dictionaries
	* __except that you can also use a dot, `.`, to access values (not just []'s)__
	* `console.log` is similar to python's `print`
	* you can declare variables with `let varname = value`
	* `=>` are function declarations (kind of like `lambda`
5. open your `index.html` file with your browser
	* Go to `File` &rarr; `Open File`
	* browse to `index.html`
	* right click on the page, and select `Inspect`
	* click on `console` to see what gets printed out

	 

### Part 4 - D3

Include d3 by adding this tag underneath the script tags for firebase, but above the script tags that contain your code

```
<script src="https://d3js.org/d3.v5.js"></script>
```

* once you have the d3 included...
* figure out the number of each model of scooter that you have
* (for example, you may have 5 of one type, and 10 of two others... for a total of 25 scooters)
* hint 1: use JavaScript objects like python dictionaries to come up with counts
* hint 2: `Object.values(someObject)` will give you an `Array` of values (much like `.values` on a `dict`)
* hint 3: once you have the values, you can [use the notes](../d3/overview.html) to draw one of the following graphs:

<img src="../resources/img/lab01-03-graphs.png" alt="lab 1 choices">

### Part 5 (Optional) - Hosting and Deploy

Activate free hosting

* Click on `Hosting` on the left-hand navigation panel
* Click on `Get started`
* Follow on-screen instructions for deploying
	* (warning: requires node)
	* `npm install` required tools
	* `firebase login`
	* `firebase init`
	* `firebase deploy`

<section markdown="block">
## 

6. Create __at least 25 scooters__ with randomized model names, retired, acquired and manufacturer values
	* __make sure that models and manufacturers remain consistent__
	* (for example, if a scooter that is model `foo` is made by manufacturer `bar`, if another scooter is model `foo`, it should also have manufacturer `bar`)
	* hint1: `random.choice([val1, val2, val3])` will give back a random element from the list passed in as the argument
	* hint2: its ok to create documents and set values within a loop

</section>







<section markdown="block">
##  Cloud Service Acct?

Settings &rarr; Project Settings  &rarr;
Click on Service Accounts table 	
Click on Python
Generate new key

pip install --upgrade firebase-admin

pip3 install --upgrade google-cloud-firestore

</section>

<section markdown="block">
## D3 / Client Application

Include client libraries:


<pre><code data-trim contenteditable>
<script src="https://www.gstatic.com/firebasejs/5.5.5/firebase-app.js"></script> 
<script src="https://www.gstatic.com/firebasejs/5.5.5/firebase-firestore.js"></script>
</code></pre>

</section>

{% endcomment %}
