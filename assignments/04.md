---
layout: homework
title: "Assignment #4"
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

# Assignment #4 - Preparing and Combining Data, Data from the Web - Due Thursday, Feb 27th at 11pm

## Goals

* importing data with pandas
* cleaning / preparing data with pandas
* using pandas for basic data analysis
	* displaying summary statistics
	* value counts
* consuming data from the web
* merging / joining data

## Overview

This homework consists of two parts:

1. Analyzing Manhattan properties sold in 12-month time period
2. A data cleaning / transformation project of your choice with pandas

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

* Download [a csv of rolling sales data from Manhattan from Sep 2018 - Aug 2019](./hw03/rollingsales_manhattan.csv)
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
	* bring in the csv file by using read_csv from pandas; don't use any keyword arguments initially
	* compare the resulting `DataFrame` against opening the spreadsheet in Excel, LibreOffice or Google Sheets
	* you _should_ immediately see an issue with the import
	* use a keyword argument [from the docs](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to fix the issue
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
5. determine the top three neighborhoods that had the most properties sold (no need to calculate units, the actual number of properties is adequate)
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


## Part 2 - Freeform Pandas Project

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



Find a data set that has missing values or values that need to be transformed.  

1. <span class="hl">don't use the dog bites data set</span> (or _really_, any other data set that we've used in class, because, uh... we already cleaned it 🙁)
2. (for the next part) write <span class="hl">code that's different from the programs that we've done in class</span> (it's not adequate to simply use class sample code with a different data set 🙅)

### 1. Write some documentation 

1. Open up the empty notebook, `project.ipynb`, in jupyterlab / jupyter notebook
2. In a markdown cell, describe the data that you've selected
	* link to any documentation about the data that you've found 
	* discuss the origin of the data (what is it, who collected / generated it, how did they do it, etc.)
3. Document the format of the data in a markdown cell
	* the data can be in any format (`csv`, `json`, etc.)
	* determine the _likely_ data type (you can use regular python types or numpy types) of each field

### 2. Retrieve the data, create a DataFrame

Include the data for the graders by either:

1. downloading it and placing it into your repository
2. linking to it in a markdown cell

Create a data frame from the data; use any method to do this (for example `read_csv`)

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
