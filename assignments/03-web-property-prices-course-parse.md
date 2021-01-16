---
layout: homework
title: "Assignment #3"
---
<style>
.hl {
	background-color: yellow;
}
img {
    border: 1px solid #000;
}

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}

.hidden {
    display: none;
}

.hintButton {
    color: #7788ff;
    cursor: pointer;
}
</style>
<script>
document.addEventListener('DOMContentLoaded', hideHints);

function hideHints(evt) {
    document.querySelectorAll('.hint').forEach((ele, i) => {
        const div = document.createElement('div');
        div.id = 'hint' + i + 'Button';
        ele.id = 'hint' + i;
        ele.classList.add('hidden');
        div.addEventListener('click', onClick);
        div.textContent = 'Show Hint';
        div.className = 'hintButton';
        ele.parentNode.insertBefore(div, ele);
    });

}

function onClick(evt) {
    const hintId = this.id.replace('Button', '');
    const hint = document.getElementById(hintId);
    hint.classList.toggle('hidden');
    this.textContent = this.textConent === 'Show Hint' ? 'Hide Hint' : 'Show Hint';
}
</script>

# Assignment #3 - Preparing and Combining Data, Data from the Web - Due Tuesday, Oct 8th at 11pm

## Goals

* importing data with pandas
* cleaning / preparing data with pandas
* using pandas for basic data analysis
	* displaying summary statistics
	* value counts
* consuming data from the web
* merging / joining data

## Overview

This homework consists of three parts:

1. Analyzing Manhattan properties sold in 12-month time period
2. Combining tabular NYU CS course info data from the web into a single table
3. A data cleaning / transformation project of your choice with pandas

## Part 1 - Manhattan Properties Sold Sep 2018 to Aug 2019

```
       _
     _|=|__________
    /              \
   /                \
  /__________________\
   ||  || /--\ ||  ||
   ||[]|| | .| ||[]||
 ()||__||_|__|_||__||()
( )|-|-|-|====|-|-|-|( )
^^^^^^^^^^====^^^^^^^^^^^

```
[ASCII art source](https://www.asciiart.eu/buildings-and-places/houses)

### Prep

* Download [a csv of rolling sales data from Manhattan from Sep 2018 - Aug 2018](./hw03/rollingsales_manhattan.csv)
from September 2018 to August 2019".
	* this data was sourced from [NYC Department of Finance’s Rolling Sales data for Manhattan](https://www1.nyc.gov/site/finance/taxes/property-rolling-sales-data.page) 
	* save the `csv` file into your repository
	* read the [companion "Data Dictionary"](https://www1.nyc.gov/assets/finance/downloads/pdf/07pdf/glossary_rsf071607.pdf) for information on the data stored in the columns

### Starting a Notebook and General Requirements

* open up the empty notebook, `rollingsales.ipynb`, in jupyterlab / jupyter notebook
* go through the instructions below... and make sure that...
* ⚠️ for each numbered instruction, insert a markdown cell before your code that has the first line of the instruction ⚠️
	* (the number and the accompanying line of text) 
	* (no need to include bulleted list underneath single instruction)

### Instructions

1. import `rollingsales_manhattan.csv` as a `DataFrame`
	* bring in the excel file by using read_csv from pandas; don't use any keyword arguments initially
	* compare the resulting `DataFrame` against opening the spreadsheet in Excel, LibreOffice or Google Sheets
	* you _should_ immediately see an issue with the import
	* use a keyword argument [from the docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) to fix the issue
	* __in a markdown cell after the import, describe what fix had to be made to make the initial import usable__
2. display columns and row samples
	* show only the names of the columns 
	* show the first 5 rows
	* show a random sampling of 5 rows
	* show the last 5 rows
3. describe the rows and data types
	* use any method to show:
		* each column 
		* the type of each column
		* the number of non-missing values in each column
	* __in a markdown cell after displaying the column info__: 
		* list out the columns that look like they have the "wrong" (or _too wide_) type
		* and next to the column name, specify what type the column should probably be
		* lastly, preview the remainder of the instructions and write out any data transformations or cleaning that you think will be necessary to complete this part of the homework
4. initial column (or row) clean-up
	* remove at least two columns
		* in a markdown cell describe why the columns should be removed
		* show evidence (with code) of why each column should be removed
	* rename or transform at least one column
		* in a markdown cell describe why the column(s) should be renamed
	* (optional) do any other clean up you deem necessary to make the following work easier
5. determine the top three neighborhoods that had the most properties sold
	* it's ok to show more than 3 neighborhoods
	* show the name and the number of properties sold for each neighborhood
	* ⚠️ document every step that you use to do this, including how the data was cleaned and/or transformed
6. describe the kind of buildings that were sold
	* ⚠️ show a visualization that allows comparison of the number of the following kinds of units sold:
		* one family homes
		* office buildings
		* condominiums
		* everything else can fall under "other" (including missing values)
	* ⚠️ document every step that you use to do this, including how the data was cleaned and/or transformed
	* hint, read the accompanying data dictionary / glossary
7. calculate summary statistics for the prices of properties sold for all of Manhattan and for a couple of select neighborhoods
	* use any method to calculate mean, median, percentiles (25 and 75), max, and min
	* pick two neighborhoods 
		* calculate summary statistics for each neighborhood: use any method to calculate mean, median, percentiles (25 and 75), max, and min
		* ⚠️ in a markdown cell below the calculations, compare the results
	* ⚠️ document every step that you use to do this, including how the data was cleaned and/or transformed
8. bin the prices of properties sold  
	* use the results from the summary statistics calculated in the previous steps to come up with minimally 5 bins to fit the prices in
	* ⚠️ bin the prices and create a visualization that compares the bins
	* use chapter 7 in Data Analysis in Python to do this... or use [the slides on binning](../slides/python/pandas-clean.html#12) and/or the docs on [`pd.cut`](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.cut.html) 
	* hint: the `sort_index` method, and the keyword argument, `asecending` = `True` or `False` may be helpful
	* in a markdown cell below this, describe:
		* what is unusual about the dataset's prices?
		* how might this affect the earlier calculations
		* what can you do to "fix" this
9. create a visualization the shows the relationship (if any) between the price sold and the number of square footage of all the areas of a property __within__ a building or a structure
	* knowing some information about the prices, feel free to use a trimmed down dataset that deals with the issue in price found above
	* ⚠️ document every step that you use to do this, including how the data was cleaned and/or transformed
10. which month did the least amount of sales occur
	* ⚠️ document every step that you use to do this, including how the data was cleaned and/or transformed
	* the [`calendar` module and `month_abbr`](https://docs.python.org/3/library/calendar.html#calendar.month_abbr)  may be useful for labels
	* it's ok to show more than one month
	* optionally, visualize this data instead of simply listing the counts
	* in a markdown cell, what can you conclude about when property sales reaches a lull?

## Part 2 - Combine Sp20 Course Info with Requirements

```
           ///////|
          /////// |
         ///////  |
        |~~~~~|   |
        |=====|   |
        |  D  |   |
        |  A  |   |
        |  T  |   |
        |  A  |   |
        |  B  |   |
        |  A  |   |
        |  E  |   |
        |     |   '
    jgs |=====| /
        '-----'`
```
[ASCII art source](http://www.oocities.org/spunk1111/school.htm), with modifications

### Prep

In this part of the assignment, you'll work on parsing html with a library and regular expressions to extract course information data. Additionally, you'll use the `merge` function to put together data from two different DataFrames based on key. 

1. Download the [Spring 2020 CS course schedule](https://cs.nyu.edu/dynamic/courses/schedule/?semester=spring_2020) by right-clicking and choosing "Save As". Save this in the root of your project repository; give it a short, but descriptive file name.
2. Download the [Spring 2020 CS course catalog](https://cs.nyu.edu/dynamic/courses/catalog/) by right-clicking and choosing "Save As". Save this in the root of your project repository; give it a short, but descriptive file name.
3. Make sure to install any modules necessary for working with html 
	* check out the slides on...
	* [data formats on the web](https://cs.nyu.edu/courses/fall19/CSCI-UA.0480-003/_site/slides/data/web-data.html)
4. Open up the empty notebook, `courses.ipynb` to work on this part of the assignment

### Instructions

#### 1. Read the 2020 course schedule into a DataFrame

* the frame should have the following columns:
	* Number-Section: the course number and section number
	* Name: the name of the course
	* Instructor: the name of the professor
	* Time: the day(s) and time(s) the course meets
	* (once you read in the data, you'll add a couple of rows)
* [here's an image of some sample rows](../resources/img/hw03-courses/courses-rows.png)
* once you've read in your data, break apart the `Number-Section` column into two separate columns: `Number` and `Section`
	* `Number` is something _like_ `CSCI-UA.0480`
	* `Section` is something _like_ `001`
	* __use regular expressions with groups to do this__
	* the `str` accessor method to use is `extract`
	* [check out the end of the regex slides](../slides/python/regex.html) or the [official pandas docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extract.html)
* show:
	* `info` to show the data types and counts
	* the first 5 rows
	* the last 5 rows
	* a random sampling of 5 rows
* hints: you'll have to...
	* read in the html file
	* parse the html
	* pick out /extract the data
	* it's very useful to use your browser's web inspector tools (right-click on element and inspect to see html and parent, sibling, and cild elements
	* ⚠️ [see this guide on using web inspector tools for chrome](https://developers.google.com/web/tools/chrome-devtools/dom/)
	* note that in the parsing library we cover in the slides...
	* `select` can be called on an element to find elements within it
	* if a collection of elements is returned, you can index into it
	* if you just one the first nested element, you can . the parent eleemnt, and use the name of the nested element next
	* `.text` returns all of the text within an element (even nested elements!)
	* pay attention to patterns in data (what _makes_ a course number, what element is a course number usually in?)
	* also helpful to print out elements themselves (without using `.text`) to see what element was actually selected 
	* some example markup and parsing code:

~~~
<section class='container'>
  <div class='row'>
    <p>Course Name: <a href="cs123.html">CS-123<a/></p>
    <p>Alice Ahn</p>
  </div>
  <div class='row'>'
    <p>Course Name: <a href="cs456.html">CS-456</a></p>
    <p>Bob Bernstein</p>
  </div>
</container>
~~~

~~~
# get every element in the section element with class container
# that has the class attribute, row
rows = rom.select('section.container .row')
for row in rows:
    # looping over this selection gives us each div element

    # within each div element, find the paragraphs
    paragraphs = row.select('p')

    # show ALL text in first paragraph in current div
    print(paragraphs[0].text) # on 1st iteration: Coure Name: CS-123

    # dotting an element with a tag name retrieves the
    # first nested element with that tag name
    print(paragraphs[0].a.text) # on 1st iteration: CS-123

    print(paragraphs[1].text) # on 1st iteration: Alice Ahn
~~~

#### 2. Read the 2020 course catalog into a DataFrame

* the frame should have the following columns:
	* Number: the course number 
	* Prereqs: a text description of the prerequisites
	* Points: the number of credits
* [here's an image of some sample rows](../resources/img/hw03-courses/catalog-rows.png)
* show:
	* `info` to show the data types and counts
	* the first 5 rows
	* the last 5 rows
	* a random sampling of 5 rows
* use a similar parsing strategy as above to read in this DataFrame

#### 3. Put together both DataFrames


* create a new DataFrame by....
* finding a way to show all scheduled classes in spring 2020 along with their points and prereqs
* only show the following columns, in this order:
	* Number: course number
	* Name: course name
	* Instructor: professor's name
	* Time: meeting time
	* Prereqs: course prerequisites
	* Points: number of credits
* hints:
	* use [`pd.merge` to do this](../slides/python/pandas-join-combine.html)
	* `how=left` will keep all rows in the first DataFrame
* can you spot any anomalies or discrepancies?
	* if so, in a markdown cell, describe any problem(s) you see
	* additionally, describe how you might fix them
	* lastly, based on the resulting DataFrame, describe the behavior of `how=left` on these particular DataFrames
	* if you need to see all rows, use `pd.set_option('display.max_rows', 200)`

## Part 3 - Freeform Pandas Project

```

                              _,add8ba,
                            ,d888888888b,
                           d8888888888888b                        _,ad8ba,_
                          d888888888888888)                     ,d888888888b,
                          I8888888888888888 _________          ,8888888888888b
                __________`Y88888888888888P"""""""""""baaa,__ ,888888888888888,
            ,adP"""""""""""9888888888P""^                 ^""Y8888888888888888I
         ,a8"^           ,d888P"888P^                           ^"Y8888888888P'
       ,a8^            ,d8888'                                     ^Y8888888P'
      a88'           ,d8888P'                                        I88P"^
    ,d88'           d88888P'                                          "b,
   ,d88'           d888888'                                            `b,
  ,d88'           d888888I                                              `b,
  d88I           ,8888888'            ___                                `b,
 ,888'           d8888888          ,d88888b,              ____            `b,
 d888           ,8888888I         d88888888b,           ,d8888b,           `b
,8888           I8888888I        d8888888888I          ,88888888b           8,
I8888           88888888b       d88888888888'          8888888888b          8I
d8886           888888888       Y888888888P'           Y8888888888,        ,8b
88888b          I88888888b      `Y8888888^             `Y888888888I        d88,
Y88888b         `888888888b,      `""""^                `Y8888888P'       d888I
`888888b         88888888888b,                           `Y8888P^        d88888
 Y888888b       ,8888888888888ba,_          _______        `""^        ,d888888
 I8888888b,    ,888888888888888888ba,_     d88888888b               ,ad8888888I
 `888888888b,  I8888888888888888888888b,    ^"Y888P"^      ____.,ad88888888888I
  88888888888b,`888888888888888888888888b,     ""      ad888888888888888888888'
  8888888888888698888888888888888888888888b_,ad88ba,_,d88888888888888888888888
  88888888888888888888888888888888888888888b,`"""^ d8888888888888888888888888I
  8888888888888888888888888888888888888888888baaad888888888888888888888888888'
  Y8888888888888888888888888888888888888888888888888888888888888888888888888P
  I888888888888888888888888888888888888888888888P^  ^Y8888888888888888888888'
  `Y88888888888888888P88888888888888888888888888'     ^88888888888888888888I
   `Y8888888888888888 `8888888888888888888888888       8888888888888888888P'
    `Y888888888888888  `888888888888888888888888,     ,888888888888888888P'
     `Y88888888888888b  `88888888888888888888888I     I888888888888888888'
       "Y8888888888888b  `8888888888888888888888I     I88888888888888888'
         "Y88888888888P   `888888888888888888888b     d8888888888888888'
            ^""""""""^     `Y88888888888888888888,    888888888888888P'
                             "8888888888888888888b,   Y888888888888P^
                              `Y888888888888888888b   `Y8888888P"^
                                "Y8888888888888888P     `""""^
```



Find a JSON data source accessible via web from a source that has some information regarding the provenance of the data (_where did it come from!?_). Check out some [sources here](../data-sets.html). It can be an API or a simple JSON file. 

1. <span class="hl">don't use the dog bites data set</span> (or _really_, any other data set that we've used in class, because, uh... we already cleaned it 🙁)
2. (for the next part) write <span class="hl">code that's different from the programs that we've done in class</span> (it's not adequate to simply use class sample code with a different data set 🙅)

### 1. Write some documentation 

1. Open up the empty notebook, `project.ipynb`, in jupyterlab / jupyter notebook
2. In a markdown cell, describe the data that you've selected
	* link to any documentation about the data that you've found 
	* discuss the origin of the data (what is it, who collected / generated it, how did they do it, etc.)
3. Document the format of the data in a markdown cell
	* it's a JSON file, so describe the keys / general structure (is it a list of objects, is it a single object per API call, etc.)
	* determine the _likely_ data type (you can use regular python types or numpy types) of each field

### 2. Retrieve the data, create a DataFrame

Use any method to retrieve your json data and put it into a DataFrame. Some options are:

* `urllib`
* `requests` (must be installed)
* `read_json` from `pandas`
* a library made specifically for the API you're using

In a markdown cell below your code, describe your methodology for retrieving the data and putting it into a DataFrame.

### 3. Using the Data

In a markdown cell, describe what you'd like to use the data for:

* perhaps you would simply like to clean it up for further analysis later
* maybe you have a hypothesis that can be backed by some basic data analysis

Write code to achieve what you've written out above. The code should contain at least 4 (repetition is allowed) of the following:

* 1 filling in missing values
* 1 type conversion
* 1 transform a column
* 1 create a new calculated column
* 1 visualization
* 1 calculate summary statistics
* 1 calculate value counts

In a markdown cell above your code, write out which of the above requirements you're implementing. As you write your code, document your process in an accompanying markdown cell.
