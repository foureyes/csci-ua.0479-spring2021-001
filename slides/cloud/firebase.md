---
layout: slides
title: "Firebase"
---

<section markdown="block">
## Firebase

* Cloud Firestore (database)
* Firebase Hosting (static resource hosting)

</section>

<section markdown="block">
## Difference Between Firebase

* [Docs on Firebase Realtime Database vs Cloud Firestore](https://firebase.google.com/docs/firestore/rtdb-vs-firestore)
* [StackOverflow summary](https://stackoverflow.com/questions/46549766/whats-the-difference-between-cloud-firestore-and-the-firebase-realtime-database)

* collections
* nested documents (nested collections)
* ordered queries
* shallow queries
* {:.fragment} sounds a lot like mongodb, but has a lot of interesting features not found in mongodb (such as shallow queries)


</section>

<section markdown="block">
## Start

Check out the [docs for getting started](https://firebase.google.com/docs/firestore/quickstart)
* sign in to your nyu google account and go to [this url](https://console.firebase.google.com/)
* go through prompts
* set up authentication
* allow anonymous authentication
* go to database &rarr; create a database 
	* choose test mode for now
Note: When you create a Cloud Firestore project, it also enables the API in the Cloud API Manager.

</section>

<section markdown="block">
## D3 / Client Application

Include client libraries:


<pre><code data-trim contenteditable>
<script src="https://www.gstatic.com/firebasejs/5.5.5/firebase-app.js"></script> 
<script src="https://www.gstatic.com/firebasejs/5.5.5/firebase-firestore.js"></script>
</code></pre>

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
