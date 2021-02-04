---
layout: homework
title: "Homework #1"
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


# Assignment #1 - BitList and Book(s) - Due Wednesday, Feb 10th at 11pm

## Overview

1. __Part 1__: `BitList` Class
2. __Part 2__: Books

## Preparation 

###  Use Git to Clone the Repository

Use the commandline (MacOS has git bundled, use GitBash or WSL for windows) git client to:

`git clone $YOUR_REPO_URL`

Alternatively, you can download a git client

* [SourceTree](https://www.sourcetreeapp.com/) - advanced graphical git client; featureful, but steeper learning curve
* [GitKraken](https://www.gitkraken.com/) - free, open source, and well-designed graphical git client for multiple platforms

You can then go through the following steps to clone your repository and commit your first changes. __Note that your repository is private!__

1. make sure you've accepted the invite from GitHub from the previous section on joining the course organization on GitHub
2. login to GitHub if you haven't already done so
3. go to the [class github page]({{site.vars.github_org}})
4. find the repository that starts with your github username and ends with `homework01` (for example, `mygithubusername-homework01`) 
5. on the repository's page, use the green "Code" button on the right side of the screen to copy the `Clone with HTTPS` to _clone_ (download) the starter files for the homework
	* use a git client to clone the homework... for example, you can use one of the following:
		1. the [GitHub graphical desktop client](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-a-repository-from-github-to-github-desktop) (click on the tab with the appropriate platform, such as Mac or Win)
		2. or you can use the commandline client (with `GITHUB_REPOSITORY_URL` being the url you copied from the green button):
    <pre><code data-trim contenteditable> git clone GITHUB_REPOSITORY_URL
</code></pre>
6. once downloaded, go to the project directory (using Finder, Windows Explorer) and open the `README.md` file... edit it with a text editor of your choice (notepad, TextEdit, Visual Studio Code, Sublime, etc.) so that it includes:
	* your netid (if you're comfortable with identifiable information on GitHub's servers)
	* your github username
	* the homework number:  `Homework #NN`
	* all together: `abc123 myusername Homework #01`
7. save your file in your local repository
	* if you're using the GitHub Desktop client, [add and commit your file using the graphical user interface](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/committing-and-reviewing-changes-to-your-project) (when selecting a branch, use the "current branch")
	* if using the commandline client
		1. in the same project directory, run <code>git add README.md</code> to let git know that you're ready to "save"
		2. then save your work locally by running <code>git commit -m "add homework meta information"</code> (everything within the quotes after <code>-m</code> is any commit message you'd like)
	* regardless of which client you use, please make your commit messages descriptive
	* (what features have been added, what bug has been fixed, etc.)
8. finally, send your work to github
	* if you're using the GitHub Desktop client, [push to GitHub simply by pressing the `Push origin` button](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/pushing-changes-to-github)
	* if you're using the commandline client, run <code>git push</code> 

## Part 1: `BitList` Class

In a file called `bits.py`, create a class, `BitList`, that represents a series of bits. The class and instances of the class will have methods representing operations that can be performed on those bits.

You can test your class implementation by running the __unit tests__ in `bits_test.py`. These unit tests will check that your class and methods behave (_mostly_) as specified by the requirements below.

### Running Tests 

 ⚠️ ⚠️ ⚠️  First , __there's an error in  `test_bits.py` , please correct  the line `from bits import BitList, DecodeError, ChunkError` by removing `, DecodeError, ChunkError`.__


1. ⚠️  Make sure to name your classes and methods exactly as they appear in the instructions below
2. Once you've implemented at least one requirement, try running `test_bits.py` to run automated tests (you can view the code in `test_bits.py` to see what features of your class are being tested
	* note that in some editors, like PyCharm, this may show up as `Run Unittests in...`
3. If your class fulfills the requirements, you should get output similar to this:
	```.........................
----------------------------------------------------------------------
Ran 25 tests in 0.002s
&nbsp;
OK
&nbsp;
Process finished with exit code 0
```
4. If there are errors or test failures, your output will look like this: 
	<pre><code data-trim contenteditable>
F.E......................
======================================================================
ERROR: test_arithmetic_shift_right_0 (__main__.TestBitList)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/joe/homework/01/test_bits.py", line 33, in test_arithmetic_shift_right_0
    1 + "2"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
&nbsp;
======================================================================
FAIL: test_and (__main__.TestBitList)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/joe/homework/01/test_bits.py", line 45, in test_and
    self.assertEqual(b1.bitwise_and(b2), BitList('0b10000001'))
AssertionError: <bits.BitList object at 0x7f7a205c1970> != <bits.BitList object at 0x7f7a205c19d0>
&nbsp;
----------------------------------------------------------------------
Ran NN tests in 0.002s
&nbsp;
FAILED (failures=1, errors=1)
</code></pre>
	* an `F` in the first line represents a failure (the test expected a certain result, but the method, function, or other implemented code gave back a different result)
	* an `E` means there was an exception - a runtime error
	* an `.` means that the test passed
	* below the first line, each error or failure is detailed
5. of course, your goal is to get zero errors or failures
	* just because your class passes all of the tests, it doesn't mean it's working perfectly, as the tests are not comprehensive
	* it's best to test often and build incrementally so that you don't end up with a large implementation that has fundamental flaws that may have been caught by earlier testing

### The `BitList` class should support the following behavior:


#### `BitList(s)`

Create a new series of bits from a string that represents a binary number:

* the string must start with `0b`
* the remainder of the string should only consist of 0's and 1's
* if the string entered in the format above, `raise` a `ValueError`
* if the string entered is valid, find some way to retain the bits 
	* ave the data entered on `self`
	* choose a data type for the value that will best serve you

Example Usage:

```
b = BitList('0b10000011')
```

```
try:
    b = BitList('10000011')
except ValueError:
    print('Format is invalid; does not start with 0b')
# Format is invalid; does not start with 0b
```

```
try:
    b = BitList('0bFE02)
except ValueError:
    print('Format is invalid; does not consist of only 0 and 1')
# Format is invalid; does not consist of only 0 and 1
```
<hr>

#### `BitList.from_ints(b1, b2, ...bN)`

A new series of bits can also be created by supplying integers directly to a `@staticmethod` `from_ints`:

* `raise` a value error there are digits other than 0 and 1
* notice that `from_ints` is called from the class itself (rather than an instance); it's a static method, so decorate with `@staticmethod`
* calling `from_ints` returns a new `BitList`.

```
b = BitList.from_ints(1, 1, 0, 0, 0, 0, 0, 1)
print(type(b)) # <class 'bits.BitList'>
print(b) # 11000001
```

```
try:
    b = BitList.from_ints(1, 2, 3, 4)
except ValueError:
    print('Format is invalid; does not consist of only 0 and 1')
```
<hr>

#### Converting to a `str`

Implement the appropriate method on the `BitList` class such that converting to a list (such as when using `str` or printing out a value) a `BitList` instance displays every bit in the series of bits:

* the prefix `0b` is not shown
* there are no spaces between each bit

```
b = BitList('0b10000011')

str(b)   # 10000011
print(b) # outputs 10000011
```

<hr>

#### `.arithmetic_shift_left()` and `.arithmetic_shift_right()`

This method __has no parameters__ and __it does not return a value__.

The bits in the series can be shifted to the left or right by one.

1. for shift left
	* the left most bit should be discarded
	* a zero should be added to the right
	* `0110` &rarr; `1100`
2. for shift right
	* the right most bit should be discarded
	* the left most bit should be duplicated
	* `1100` &rarr; `1110`

Note that the internal representation of bits should change. That is, there is no return value; instead, the actual `BitList` instance changes:

```
b = BitList('0b10000010')
b.arithmetic_shift_right()
print(b) # 11000001
```

<hr>



#### `==`

If both `BitList` instances contain the same series of bits, then they're equal:

```
b1 = BitList('0b11000001')
b2 = BitList.from_ints(1, 1, 0, 0, 0, 0, 0, 1)
print(b1 == b2) # True!
```

<hr>

#### `.bitwise_and(otherBitList)`


This method has __one parameter, another instance of `BitList`__, and it returns a new `BitList` instance.

A bitwise and can be performed with an _incoming_ `BitList`:

* a bitwise and can only be performed if both sequences of bits are of equal length
* for every position, use a logical `and` to produce a new bit
	* treat `1` as `True`
	* treat `0` as `False`
	* use these boolean values with a logical `and` evaluate to either `True` or `False`
	* consequently, performing a bitwise and on `1110` and `1011` produces `1010`
		```
1110 (TTTF) - Operand 1
1011 (TFTT) - Operand 2
1010 (TFTF) - Result
```
	* optionally, simply multiplying each position also works!
* again, the method itself has one parameter, the other `BitList` instance
* it returns a new `BitList` instance

```
b1 = BitList('0b10000011')
b2 = BitList('0b11000001')
b3 = b1.bitwise_and(b2)
print(b3) #1 0000001
```

<hr>

#### `.decode(encoding)`

__⚠️⚠️⚠️ If you are not implementing the optional portion for this method (utf-8) you can comment out the last 4 tests ⚠️⚠️⚠️__

This method has a __single parameter__, the encoding (a `str`), and it __returns a string__:

1. the encoding can only be `us-ascii` or `utf-8` (see optional section on `utf-8` below)
2. it returns a string 

An instance of `BitList` can be decoded. In the example below, the bits are treated as 7-bit ASCII (`us-ascii`):

```
bits = BitList.from_ints(1, 1, 0, 0, 0, 0, 1)
ch = bits.decode('us-ascii')
print(ch) # a
```

This should work if there are multiple characters encoded:

```
new_bit_list = BitList('0b11000011000001')
s = new_bit_list.decode('us-ascii')
print(s) # aA
```

One way to implement this is to:

1. calculate the decimal value from the bits
2. convert the decimal value into a character with `chr`

__Optional__ If you're looking for a challenge, you could add support for decoding `utf-8`.

This is a little tricky, as chunking bits into equivalent lengths isn't adequate:

* `utf-8` is variable length
* the "leading byte" must be examined to determine how many bytes total are required
* for example, encountering the byte `11101010` means that there should be three bytes total (there are 3 1's)
* the continuation bits are all prefixed with `10`
* see the slides / notebook on `unicode` for more details

```
b = BitList('0b11110000100111111001100010000010111000101000001010101100')
s = b.decode('utf-8')
print(s) # 😂€

```

## Part 2: A Little _Bit_ of Decoding

Write an interactive program that:

1. asks the user for a series of 0's and 1's: `Give me some bits!` 
	* if the input does not consist only of 0, 1 and / or space, ask again
	* if there are spaces in the input, they can be removed	
	* 01110000 01100011 can be treated as 0111000001100011 
2. ask for an encoding: `Give me an encoding!`
	* if you only implemented `us-ascii` in part 1...
	* this question should still be asked, but assume that the user will enter `us-ascii`
3. if the user had entered the bits and encoding previously, skip to step 6 where the user is asked if they'd like to continue
4. based on the input, display the following:
	1. the original input without spaces: `Input: 0111000001100011`
	2. the code points, in binary: `Code Points Binary: 0111000 1100011 1111001` 
		* based on the encoding (default to `us-ascii` if you did not ask for an encoding as detailed in the previous requirement)... group the bits
		* if the original input was `011100011000111111001` and the encoding was `us-ascii` (which is a 7-bit encoding)
		* then simply show groups of 7 bits: `0111000 1100011 1111001` 
		* ⚠️ this is much trickier with `utf-8` 
			* breaking the input into equal groups isn't adequate
			* `utf-8` is variable width, so it can be 1, 2, 3 or 4 bytes (8, 16, 24 or 32 bit groups)
		* no input validation is needed to determine if the correct number of bits were entered for the encoding specified
	3. the code points, in decimal: `Code Points Decimal: 128013 8364`
		* you'll have to find some way to convert the bits entered into decimal values
	4. the decoded string: `Decoded String: 🐍€`
5. find some way to "save" all of the bits, encodings, and corresponding decoded string
6. ask the user if they'd like to continue `Type Y to enter more bits?`
	* if they answer with a `Y`, then start at step 1 again
7. if a user does not continue, show all bits entered, encodings and their related decoded string
	```
Thanks, these were all the bits you entered!
utf-8-11110000100111111001000010001101111000101000001010101100 >>> 🐍€
us-ascii-1000001 >>> A
```

Example Run:

```
Give me some bits!
> 11110000 10011111 10010000 10001101 11100010 10000010 10101100
Give me an encoding!
> utf-8
Input: 11110000100111111001000010001101111000101000001010101100
Code Points Binary: 000011111010000001101 0010000010101100
Code Points Decimal: 128013 8364
Decoded String: 🐍€
Type Y to enter more bits?
> Y
====================


Give me some bits!
> 1000001
Give me an encoding!
> us-ascii
Input: 1000001
Code Points Binary: 1000001
Code Points Decimal: 65
Decoded String: A
> Type Y to enter more bits?
Y
====================


Give me some bits!
> 11110000 10011111 10010000 10001101 11100010 10000010 10101100
Give me an encoding!
> utf-8
you already entered those bits and encoding: 🐍€
Type Y to enter more bits?
> nope
====================


Thanks, these were all the bits you entered!
utf-8-11110000100111111001000010001101111000101000001010101100 >>> 🐍€
us-ascii-1000001 >>> A
```
