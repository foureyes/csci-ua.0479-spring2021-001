---
layout: homework
title: "Assignment #2"
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

# Assignment #2 - Summary Statistics and Basic Data Visualization - Due Fri, Sept 27th at 11pm

Clone the homework #2 repository when it is created for you.

## Goals

* work with numpy to calculate summary statistics
* use matplotlib for simple data visualizations

## Requirements

* 1 x notebooks:
	* homework02ipynb
* 1 x data set:
	* reuse from homework 01
	* include in repository if possible


## Overview

In this assignment, you'll create a single notebook, (`ipynb`) that contains documentation and code. 

1. reuse the data set you worked with in the first homework
	* include your previous documentation regarding the source of the data
	* if the data set does not have two numeric columns, you can use a different data set
		* (you'll have to reproduce the corresponding documentation, though)
	* include the data set in your repository so that your notebooks can be run by the graders without having to perform any setup
2. write some questions that _may_ be answered by using summary statistics on numeric columns in your data set, or by viewing visualizations
3. calculate summary statistics on both columns using numpy
4. validate calculations
	* export a csv
	* ...then import the csv into a spreadsheet 
	* confirm that your summary statistics match
	* save or export the spreadsheet as an Open Office (`.ods`) or Excel File (`.xls`) and place in your repository
5. create at least two visualizations with matplotlib
6. write a conclusion answering your questions in part 2 based on the results in parts 3 and 4
	* describe the results of your calculations and visualizations
	* describe whether or not they were able to answer your questions from part 2


## Part 1 - Reusing / Selecting a Data Set, Adding Documentation

#### Reuse your data set from homework 01

Use the data set and documentation from homework 01:

1. add the data set to the repository, if possible (again, for ease of setup for the graders; typically though, your data would not be stored in version control)
2. reuse the following parts of your previous documentation on the provenance of your data
	1. Name: (TODO: name of data set)
	2. Link to Data: (TODO: link to any documentation about the data that you've found )
	3. Source / Origin: (TODO:  discuss the origin of the data (what is it, who collected / generated it, how did they do it, etc.)
3. in addition to including the source of the data, show some of the data and document the format of the data
	1. with code, display the first few lines of the file
	2. describe the format of the data in a markdown cell
		* what are ther fields / column headers?
		* what is the _likely_ data type for each column (you can use regular python types or numpy types) of each field

If the data does not have at least two numeric columns, please work with a different data set


## Part 2 - Questions

Again, as with the previous homework, write some questions about your data. However, this time, focus on the following:

* questions that _may_ be answered by using summary statistics on numeric columns in your data set
* questions that _may_ be answered by viewing basic data visualizations, such as bar charts and scatter plots

## Part 3 - Stats and Answers

1. read the data from at two columns of your file; try to read the numeric data into a numpy array 
	* you can read the individual columns into separate arrays
	* ...or you can read all of the data as a multidimensional numpy array
	* you'll have to parse the data into a numeric type 
	* you may have to clean up the data before it can be converted into a numeric type (for example, replacing commas, removing dollar signs, etc.)
2. calculate descriptive statistics on these two columns
	* examine outliers with min and/or max
	* measure central tendency by using mean, median, and/or percentile (quantile), 
	* measure dispersion with variance, standard deviation, and/or interquartile range


## Part 4 - Visualizations

Create at least two visualizations with matplotlib.

## Part 5 - Conclusion

Write a conclusion answering your questions in part 2 based on the results in parts 3 and 4.

* describe the results of your calculations and visualizations
* describe whether or not they were able to answer your questions from part 2
