---
layout: slides
title: "Basic Regular Expression Syntax"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Regular Expressions

A __regular expression__ is a series of characters that define a pattern. These patterns can be made up of:

* {:.fragment} __simple characters__ - characters that you want to match directly
* {:.fragment} __special characters__ - characters that specify some a pattern rather than a direct match

(special characters are also referred to as _metacharacters_)
{:.fragment}

👀 The pattern essentially describes __rules for matching text__. 
{:.fragment}

</section>

<section markdown="block">
## Regular Expression Usage

__This regular expression pattern can be used to:__ &rarr;

* {:.fragment} test if a string or part of string matches
* {:.fragment} _capture_ the parts of a string that matches
* {:.fragment} find and replace based on matches
* {:.fragment} split based on matches

__In Python, a regular expression pattern can be represented by:__ 
{:.fragment}

* {:.fragment} a string
* {:.fragment} a "raw string" 
	* {:.fragment} a raw string is a string literal prefixed with an `r`
	* {:.fragment} `r"see \ behavior"` 
	* {:.fragment} in a raw string, escape characters are literal!
* {:.fragment} a "compiled" regular expression

</section>

<section markdown="block">
## The `re` Module

__In "plain" Python, regular expression functionality can be found in the `re` module__ &rarr;

* {:.fragment} `import re` first
* {:.fragment} it may be useful to "compile" a regular expression
	* {:.fragment} `re.compile(some_pattern)`
	* {:.fragment} useful if you're planning on using the same pattern repeatedly
	* {:.fragment} (otherwise a regular or raw string is adequate)
* {:.fragment} the `re` module contains various methods for working with regular expressions (RE)

</section>

<section markdown="block">
## `re` Module Methods

__The `re` module supports the following methods:__ &rarr;
{:.fragment}

* {:.fragment} `match()` and `search()`: match the RE once at the beginning of the string and anywhere in the string, respectively
* {:.fragment} `findall()`: find all substrings where the RE matches, returned as a list
* {:.fragment} `split()`: split a string based on pattern
* {:.fragment} `sub()`: find all RE matches, and replace 

</section>

<section markdown="block">
## Match Objects

__`match` and `search` both return `None` if there's no match for the pattern provided... but if there is a match, then a `Match` object is given back__ 

* {:.fragment} see the [docs on Match Objects](https://docs.python.org/3/library/re.html#match-objects)
* {:.fragment} a match object always has a boolean value of `True` 
* {:.fragment} the `.group()` function and the index/`__getitem__` (`[]`) returns the entire match or a partial match based on the argument / index:
	* {:.fragment} 0 - the entire matched string
	* {:.fragment} 1 - the first part of the match within parentheses
	* {:.fragment} 2 - the second part of the match within parentheses
</section>

<section markdown="block">
## Simple Matching

__Here are some examples of "simple" matching (but at this point, you can just use `in`, amirite? 🤷‍♀️)__ &rarr;

Let's try `match` and `search` where we match the simple pattern 🍌:
{:.fragment}

```
re.match('ban', 'banana boat') # Match (True-ish)
re.search('boa', 'banana boat') # Match (True-ish)

re.search('orange', 'banana boat') # None (False-ish)
```
{:.fragment}

Using a match object:
{:.fragment}

```
m = re.search('o(a(t))', 'banana boat')
m.group(0) # oat
m.group(1) # at (first group in parens)
m[2] # t (indexing works too 👌)
```
{:.fragment}


</section>

<section markdown="block">
## Match vs Search vs Findall

__`match` only matches from the beginning... and both `match` and `search` find just one match, whereas `findall` gives back all matches__ &rarr;

* {:.fragment} `match` only matches at beginning, soooo...
	* {:.fragment} `re.match('boa', 'banana boat') # None (False-ish)`
* {:.fragment} `match` and `search` just retrieve one match:
	* {:.fragment} `re.search('an', 'banana boat')`
	* {:.fragment} `re.findall('an', 'banana boat')`
	* {:.fragment} `# findall returns ['an', 'an']`

</section>

<section markdown="block">
## Split and Replace


`split` takes a split pattern and a string and gives back a list of strings extracted from the original string using the pattern as a boundary:

```
re.split('a', 'banana boat')
```
{:.fragment}

```
['b', 'n', 'n', ' bo', 't']
```
{:.fragment}

`sub` takes a pattern, replacement and a string... and gives back all instances of pattern replaced by replacement in the string
{:.fragment}

```
re.sub('an', 'or', 'banana boat')
```
{:.fragment}


```
# 🚢
'borora boat'
```
{:.fragment}
</section>

<section markdown="block">
## Metacharacters

__Ok... so all of that wasn't that useful, as regular string methods would have worked just fine. 🤦‍♂️__ &rarr;

So... the real power in regular expression patterns comes from metacharacters
{:.fragment}

These are characters with special meaning... and they fall into some broad categories:
{:.fragment}

* {:.fragment} character types/classes
* {:.fragment} location
* {:.fragment} quantifiers

</section>
<section markdown="block">
## Character Classes

__Instead of matching _literal_ characters, these metacharacters match a specific type or class of character:__ &rarr;

* {:.fragment} `.`- any character
* {:.fragment} `[]` can define a set of characters
	* `[xyz]` - one of any of these characters
	* `[a-z]` - any character in this range
	* `[A-Za-z0-9_]` - any character in these ranges or specific character
	* `[^xyz]` - any character that's not in this set of characters
* {:.fragment} __\w__ - any _word_ character (alphanumeric and underscores, like `[A-Za-z0-9_]`)
* {:.fragment} __\d__ - any digit character (`[0-9]`)
</section>

<section markdown="block">
## Metacharacters in Action 🏃‍♀️

__What are the results of these regular expressions?__ &rarr;

```
re.findall('a\w', 'a banana boat')
```
{:.fragment}

```
['an', 'an', 'at']
```
{:.fragment}

```
re.findall('a.', 'a banana boat')
```
{:.fragment}

```
# note that a's with space is included!
['a ', 'an', 'an', 'a ', 'at']
```
{:.fragment}

```
# note that the character class contains a space
re.findall('a[^n ]', 'a banana boat')
```
{:.fragment}

```
['at']
```
{:.fragment}

```
# note that findall doesn't allow overlapping matches
# so it just finds the first, but ignores the second
re.findall('.an', 'a banana boat') # just ['ban']
```
{:.fragment}

```
['ban']
```
{:.fragment}
</section>


<section markdown="block">
##  Location and Quantifiers

__Where should we anchor the match?__ &rarr; 

* {:.fragment} __^__ - beginning of line
* {:.fragment} __$__ - end of line

__How many?__ &rarr; 

* {:.fragment} __{n}__ - n of the preceding
* {:.fragment} __{n,m}__ - at least n and at most m of the preceding
* {:.fragment} __?__ - 0 or 1 of the preceding
* {:.fragment} __*__ - 0 or more of the preceding
* {:.fragment} __+__ - 1 or more of the preceding

</section>

<section markdown="block">
## Location Quantifier Examples

```
re.search('(an)*a', 'ana nab a banana')
```

```
ana
```
{:.fragment}

```
re.search('(an){2}a', 'ana nab a banana')
```
{:.fragment}

```
anana
```
{:.fragment}

```
re.findall('a\w.', 'ana nab a banana')
```
{:.fragment}

```
['ana', 'ab ', 'ana']
```
{:.fragment}

```
re.findall('^a\w.', 'ana nab a banana')
```
{:.fragment}

```
['ana']
```
{:.fragment}
</section>

<section markdown="block">
## Some More Examples!

__A few more regular expressions... describe the following patterns__ &rarr;

* {:.fragment} <code>\d\d\d</code> or <code>\d{3}</code> 
	* {:.fragment} exactly 3 digits
* {:.fragment} <code>h.*$</code> 
	* {:.fragment} h followed by 0 or more of any character up to the end of the line
* {:.fragment} <code>^\w\d?\d?$</code> 
	* {:.fragment} one letter at the beginning of a line followed by exactly 0, 1 or 2 digits
</section>


<section markdown="block">
## Escaping Special Characters

__If you want to match a literal character that's the same as a metacharacter, you have to escape it.__ &rarr;

For example...
{:.fragment}

* {:.fragment} `.` means any character... 
* {:.fragment} but maybe you _actually_ want to match for a `.` only
* {:.fragment} escape it with a backslash: `\.`

```
re.findall('a\.', 'banana.')
['a.']

re.findall('a.', 'banana.')
['an', 'an', 'a.']
```
{:.fragment}
</section>

<section markdown="block">
## Grouping with Parentheses

__Parentheses are actually special characters too. They specify grouping__ &rarr;

* if you want to match actual parentheses, they must be escaped
* surrounding with parentheses allows you to match sub-patterns
* remember - this works with `match` and `search` as both functions return match objects

```
# matches a date
# contains sub groups for month and day
re.search('(\w{3}) (\d{2})', 'The date is Jan 23')
```
```
# entire match
m[0] # 'Jan 23'
```
{:.fragment}

```
# first subgroup
m[1] 'Jan'
```
{:.fragment}

```
# second subgroup
m[2] '23'
```
{:.fragment}

</section>
<section markdown="block">
## pandas and Regex

__Regular expressions can be used through the `str` accessor:__ &rarr;

* `str.match(pattern)`
	* gives back Series of booleans
	* True if string in Series matches pattern
	* False otherwise
* `str.extract(pattern)`
	* `pattern` __must__ contain subgroups
	* will extract subgroup into new Series!
	* _useful_ for pulling out a substring from another using a pattern

</section>

<section markdown="block">
## Extract Example

__The following code extracts a single letter followed by a period from each element in the Series below.__ &rarr;

```
s = pd.Series([
			'aa.) yes', 
			'bbb.) no', 
			'c.) maybe'
]);
```

Notice the subgroups used in the pattern with `extract`...
{:.fragment}

```
s.str.extract('\w*(\w\.)\)')
```
{:.fragment}

```
	0
0	a.
1	b.
2	c.
```
{:.fragment}
</section>


