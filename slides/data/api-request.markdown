---
layout: slides
title: "Making Web Requests, Using APIs"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Web Primer

some basics

* http: client, server
* http request: GET/POST
* http response: status
* url: domain, path


</section>

<section markdown="block">
## Getting Data from a URL

Using `urllib` to __retrieve data from a url__

* {:.fragment} `urllib` is built-in to Python3; no need to install
* {:.fragment} to use ([see docs too])(https://docs.python.org/3/library/urllib.html):
    <pre><code data-trim contenteditable>
import urllib.request
with urllib.request.urlopen('http://cs.nyu.edu') as response:
   res = response.read()
</code></pre>


* {:.fragment} now we can parse res / `BeautifulSoup` or `json`! 
* {:.fragment} in some use cases (eg sending username and password... or additional request data), you'll have to write some boilerplate code
* {:.fragment} `res` is a file like object (so, iteration, `read`, etc. works)
* {:.fragment} but you can also retrieve `code` and `headers`
</section>

<section markdown="block">
## Another Option: `requests`

Using the `requests` module to __retrieve data from a url__ &rarr;

* {:.fragment} `conda`, `easy_install`, or `pip install` `requests` first...
* {:.fragment} Then:
    <pre><code data-trim contenteditable>
import requests
res = requests.get("http://cs.nyu.edu")
print(res.status_code) # http response status code (you want a 200)
print(res.text) # the contents / body of the response
</code></pre>

</section>

<section markdown="block">
## APIs

__API__  stands for __Application Programmer Interface__: basically a set of tools that help you develop an application.

In the context of the web, some sites offer an __API__ to access their data. For example &rarr;

* [tumblr api](https://www.tumblr.com/docs/en/api/v2)
* [nytimes api](https://developer.nytimes.com/)
{:.fragment}

Note that apis usually require some sort of authentication, and that authentication can be as a simple as a unique key assigned to your program
{:.fragment}

</section>

<section markdown="block">
## Using APIs

__The general steps for using an API are__ &rarr;

1. {:.fragment} read documentation
2. {:.fragment} determine authorization (usually request a token)
3. {:.fragment} make an http request to the appropriate url to retrieve data
4. {:.fragment} parse the data (usually json, but you'll also see xml... and even plain html!)

{:.fragment}
</section>


<section markdown="block">
## tumblr + `urllib` Example

Let's try `urllib` with the [tumblr api](https://www.tumblr.com/docs/en/api/v2). Let's read the docs and figure out how we can get some cat 🐈 pics!

<pre><code data-trim contenteditable>
import urllib.request, json

# we're going to ask tumblr for some posts ...
search_tag = 'cat'
api_key = 'XBu4Lke6Cyh2UrLFIZW0jIo79sUT8EwtruJduMAknEUNhccNwY'
post_type = 'text'
url = 'http://api.tumblr.com/v2/tagged?api_key=' + api_key
url = url + '&tag=' + search_tag

response = urllib.request.urlopen(url).read().decode('utf-8')
posts  = json.loads(response)['response']

for post in posts:
    if post['type'] == 'photo':
        tags = post['tags']
        photo = post['photos'][0]
        number_of_tags = len(tags)
        if number_of_tags > 2:
            print(tags)
            print(photo['original_size']['url'] + "\n\n")
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Simple NYT Search + `requests`

__Now let's try `requests`... (use `.get`, `text`, and `json`)__ &rarr;

<pre><code data-trim contenteditable>
import requests
res = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q=TODO&api-key=TODO');

data = res.json()
docs = data['response']['docs']
for doc in docs:
    print(doc['headline']['main'])
    print(docs[0].keys())
    print(len(docs))
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## Tools That Combine Requests and Scraping


__[scrapy](https://scrapy.org/) - if you want _industrial_ strength screen scraping, this it the tool to use! ... some highlights include__
{:.fragment}

* {:.fragment} "requests are scheduled and processed asynchronously" (⚡️_fast_)
* {:.fragment} but you can also throttle / reduce number of concurrent connections
* {:.fragment} _built_ for making reusable web crawlers!

__[requests-html](https://html.python-requests.org/) - built by the same person that wrote `requests`__
{:.fragment}

* {:.fragment} simple api that plays nicely with `requests`
* {:.fragment} supports rendering of `javascript` page elements! 



</section>
