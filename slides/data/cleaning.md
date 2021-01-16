---
layout: slides
title: ""
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## csv module continued

__Let's take a look at using the csv module...__ &rarr;
<pre><code data-trim contenteditable>
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        print(row[0])
</code></pre>

* notice that the reader object is created by calling <code>csv.reader</code> and passing in a file object
* from there, simply loop (printing the whole row shows it's a list...)
</section>

<section markdown="block">
## Wanna Get Fancy, Do Ya?

__How about reading those rows as dictionaries instead?__ First row is considered the keys (they should be the headers, right?).

<pre><code data-trim contenteditable>
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row['pace'])
</code></pre>
</section>
