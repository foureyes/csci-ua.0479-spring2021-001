---
layout: homework
title: "Assignment #1"
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

# Assignment #1 - Modules, Strings, Lists, Dictionaries, File I/O - Due Tuesday, Sep 11th at 11pm

This assignment consists of two parts:

1. Happy Birthday!
2. Oh Darcy.

Clone the homework #1 repository when it is created for you.

## Part 1 - Happy Birthday!

Apparently, in a set of 23 randomly chosen people, there's a _pretty good chance_ that two of those people will have the same birthday! Yes, it's _actually_ true, and it's called the [Birthday Problem or the Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem). [betterexplained.com](https://betterexplained.com/articles/understanding-the-birthday-paradox/) has a good write-up on why, but we'll use a computer simulation to approximate this probability. We'll create tools to randomly generate dates, and then we'll see if any month and day combinations match.

You'll be doing this in two parts:

1. write a bunch of functions to help with creating dates
2. create an interactive program that allows you to run the simulation multiple times 

1. Open `mydate.py` in a text editor of your choice
2. Write the following functions in `mydate.py` to help implement your program:
    * `is_valid_month_num(n)`
    * `month_num_to_string(month_num)`
    * `date_to_string(date_list)`
    * `dates_to_strings(date_list)`
    * `remove_years(date_list)`
    * `is_leap_year(year)`
    * `get_num_days_in_month`
    * `generate_date(start_year, end_year)`
    * you can write more functions if you want!
3. Using your previously implemented `mydate.py` as a module, import it and use it to help write `birthday.py`
    * In `birthday.py`, you'll write a simulation by generating random birthdays
    * The simulation will be an interactive program that asks the user how many trials to run... as well as other parameters for generating birthdays for a group of people
    * The percentage of times that at least one duplicate occurs should be printed out at the end

#### is_valid_month_num(n)

__Parameters__:

* `n` - an integer representing a month, with 1 being January and 12 being December

__Return Value__:

* a `boolean` - `True` if number passed in is between 1 and 12 inclusive, `False` otherwise

__Description__:

`is_valid_month_num` will take a month in numeric format and return a boolean value based on whether that number is a valid month (1 through 12, inclusive)

__Example Usage__:

<pre><code data-trim contenteditable>result1 = is_valid_month_num(3) 
print(result1) # True
result2 = is_valid_month_num(37) 
print(result2) # False
</code></pre>

<hr>
    
#### month_num_to_string(month_num)

__Parameters__:

* `month_num` - an integer representing a month, with 1 being January and 12 being December

__Return Value__:

* a `string` - the month name corresponding to the number passed in, `None` if the number passed in is invalid

__Description__:

`month_num_to_string` will take a month in numeric format and return a string representing the month's name (given a valid month number). If the month number passed in is not valid, `None` is returned (either implicitly by not returning anything or by explicitly returning `None`). 

<div class="hint" markdown="block">A simple way to implement this would be to create a list of month names within your function and send back the appropriate one based on position.
</div><br>

__Example Usage__:

<pre><code data-trim contenteditable>result1 = month_num_to_string(1) 
print(result1) # 'January'
result2 = month_num_to_string(10) 
print(result2) # 'October'
result3 = month_num_to_string(234) 
print(result3) # None
</code></pre>

<hr>

#### date_to_string(date_list)

__Parameters__:

* `date_list` - a three-element `list` containing integers representing a year, month and day; for example, `[2012, 3, 14]` represents March 14th, 2012

__Return Value__:

* a `string` - the string version of the date passed in as the original `list`; the format of the string returned is month_name day_number, year: March 14th, 2012


__Description__:

`date_to_string` assumes that it will be passed a `list` containing valid numbers for year, month and day (you will not have to check the numbers passed in). Given `[YEAR_NUMBER, MONTH_NUMBER, DAY_NUMBER]`, this function will construct a string in the format of `MONTH_NAME DAY_NUMBER, YEAR_NUMBER` where `MONTH_NAME` is determined by using one of the previous function with `MONTH_NUMBER`. 

For example, `[1979, 10, 7]` should give back `'October 7, 1979'`.

<div class="hint" markdown="block">
1. Again, use one of the previously implemented functions for this
2. No looping is required!
</div><br>

__Example Usage__:

<pre><code data-trim contenteditable>date_to_string([1979, 10, 7]) 
# returns the string: October 7, 1979
</code></pre>

<hr>

#### dates_to_strings(list_of_date_lists)

__Parameters__:

* `list_of_date_lists` - a `list` containing dates, with each date being a sub list of composed of three elements (as described in `date_to_string`)

__Return Value__:

* a `list` - a `list` of string versions of each sub list (date) from the original list passed in

__Description__:

`dates_to_strings` converts a list of lists to a list of strings. Each inner list in the list of lists is a date in the format of a three-element list (as explained in the previous function). The result is a list of strings, with each string representing one of the original dates in the list passed in. For example, `[[1979, 10, 7], [2000, 2, 20]]` should give back `['October 7, 1979', 'February 20, 2000']`.

__Example Usage__:

<pre><code data-trim contenteditable>res = dates_to_strings([[1979, 10, 7], [2000, 2, 20]]) 
print(res) # ['October 7, 1979', 'February 20, 2000']
</code></pre>

<hr>

#### remove_years(list_of_date_lists)

__Parameters__:

* `list_of_date_lists` - a `list` containing dates, with each date being a sub list composed of three elements (as described in date_to_string)

__Return Value__:

* a `list` - a new `list` with 2-element sub lists representing a month and a day (year is removed)

__Description__:

`remove_years` creates a new `list` with the year element removed for every sub list in a list of date lists. This essentially converts a list of three-element lists to a list of two-element lists.

__Example Usage__:

<pre><code data-trim contenteditable>res = remove_years([[1979, 10, 7], [2000, 2, 20]]) 
print(res) # [[10, 7], [2, 20]]
</code></pre>

<hr>

#### is_leap_year(year)

__Parameters__:

* `year` - an `int` specifying the year to check

__Return Value__:

* a `boolean` - `True` if the year, `year`, is a leap year, `False` otherwise

__Description__:

Determines whether a year is a leap year or not using [this algorithm from microsoft](https://support.microsoft.com/en-us/help/214019/method-to-determine-whether-a-year-is-a-leap-year). Returns `True` or `False` accordingly.

<div class="hint" markdown="block">
1. a lot of nested if statements may be helpful
2. after getting it to work with nested if statements, you can rewrite it more easily so that it contains no nesting!
</div><br>

__Example Usage__:

<pre><code data-trim contenteditable>for year in [1988, 1992, 1996, 1600, 2000, 2400]:
    print(is_leap_year(year)) # True for each one!

for year in [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]:
    print(is_leap_year(year)) # False for each one!
</code></pre>

<hr>

#### get_num_days_in_month(month_num, year)

__Parameters__:

* `month_num` - an `int` specifying the month number
* `year` - an `int` specifying the year to check

__Return Value__:

* an `int` - the number of days for the month represented by `month_num` at year, `year` or `None` if the `month_num` passed in is not valid

__Description__:

Determines the number of days in a month given a month (in the format of a number from 1 through 12), as `month_num` and a year as `year`. Leap years should be taken into account (February may have 28 or 29 days). You can map months with their days by storing number of days in a list. The position of the number of days in the list will help determine what month it's in. If the month number passed in is not between 1 and 12, inclusive, then give back `None` (this could be done implicitly by no having a `return` or by explicitly returning `None`).

<div class="hint" markdown="block">
1. A list that just stores days for every month may help
    * the number at index 0, or the first element, will store the number of days for January
    * the number at index 11, or the last element, will store the number of days for December
    * `[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`
    * note that February has 28 by default, but that could change depending on whether or not it's a leap year
2. Using `month_num` to generate the appropriate index, pull out the correct number of days
3. Watch out for February and invalid month numbers, though!
</div><br>

__Example Usage__:

<pre><code data-trim contenteditable>get_num_days_in_month(2, 1988) # 29
get_num_days_in_month(2, 1900) # 28
get_num_days_in_month(11, 1900) # 30
get_num_days_in_month(12, 1900) # 31
get_num_days_in_month(1, 1900) # 31
get_num_days_in_month(30, 1999) # None
</code></pre>

<hr>

#### generate_date(start_year, end_year)

__Parameters__:

* `start_year` - an `int` specifying the minimum year that the randomly generated date may have
* `end_year` - an `int` specifying the maximum year that the randomly generated date may have

__Return Value__:

* a `list` - a new `list` consisting of 3 `int`s: a year, month number, and a day

__Description__:

`generate_date` creates a date with random, month, day and year using other functions from this module. The date generated must have a year that falls within `start_year` and `end_year`. It must also generate a valid month number (1 through 12)... and lastly a valid number of days (including a valid number of days for February during leap years).

<div class="hint" markdown="block">
</div><br>

__Example Usage__:

<pre><code data-trim contenteditable>date = generate_date(2015, 2017) 
print(date) # a random 3 element list, like: [2017, 9, 5]
</code></pre>

<hr>


#### Interactive Program (`birthday.py`)

Once you've finished your functions, write an interactive program that simulates creating a group of people, each with a random birthday. To do this:


1. Open `birthday.py` if you haven't done so already
2. Using your `mydate` module 
3. First, ask how many times the simulation should be run
    <pre><code data-trim contenteditable>How many times should I run the simulation?
</code></pre>
4. Then, ask wow many birthdays should be generated 
    <pre><code data-trim contenteditable>How many birthdays should I generate per trial?
</code></pre>
5. Once you have the user input...
6. __repeat the following based on the number of trials specified by the user__:
    1. generate the number of birthdays specified (you can use and start and end year to create these dates)
    2. remove the years from the dates
    3. find the dates that occur more than once
    4. print out the following:
        * the trial number
        * the number of dates that occur more than once
        * and a comma separated list of the duplicate dates, in parentheses
    5. here's some example output:
        <pre><code data-trim contenteditable>Trial #1: 2 dates occur more than once! (August 2, April 24)
Trial #2: 1 date occurs more than once! (September 16)
How many times should I run the simulation?
Trial #3: No dates are the same.
.
.
.
</code></pre>
7. After running all of the trials specified...
    * calculate the probability that there will be duplicates by...
    * taking the count of trials where at least one date occurred more than once
    * ...and dividing that by the number of trials specified
    * output the resulting number as a percentage with the following information:
        * the total number of trials
        * the total number of trials that had a birthday that occurred more than once
        * the probability of a duplicate
        * the number of birthdays generated for every trial
    * for example:
        <pre><code data-trim contenteditable>Results:
=====
Out of 7 trials, 4 had dates that were repeated
We can conclude that you have a 57.14% chance of sharing a birthday with someone if you are in a group of 23 people
</code></pre>
8. An example of a full run of the program is below:
<pre><code data-trim contenteditable>How many times should I run the simulation?
>7
How many birthdays should I generate per trial?
>23
Trial #1: 2 dates occur more than once! (August 2, April 24)
Trial #2: 1 date occurs more than once! (September 16)
Trial #3: No dates are the same.
Trial #4: 2 dates occur more than once! (February 4, July 21)
Trial #5: No dates are the same.
Trial #6: 1 date occurs more than once! (September 14)
Trial #7: No dates are the same.

Results:
=====
Out of 7 trials, 4 had dates that were repeated
We can conclude that you have a 57.14% chance of sharing a birthday with someone if you are in a group of 23 people
</code></pre>

<hr>

## Part 2 - Oh Darcy

Using a book from [project Gutenberg](https://www.gutenberg.org/):

1. download a `txt` version of any book you like
2. in jupyter lab, edit the notebook `book.ipynb`
3. in a markdown cell, write a question you'd like answered about the book that might require some programming... for example:
	1. who was the most frequently mentioned character in Pride and Prejudice?
	2. are the pronouns in Frankenstein predominantly male or female?
	3. etc. .... (feel free to use either of the above questions, or come up with your own!)
4. open the `txt` version of the book that you downloaded through code
5. use jupyter notebook code cells to analyze the text in your file...and come up with an answer
	*  __a dictionary__ must be part of your analysis
6. document your steps in markdown cells
7. your answer does not have to be correct (or even exact!)... as long as you have some description of your analysis
8. include the txt file in your repository

