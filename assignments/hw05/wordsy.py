"""
wordsy.py
=====
This file will be used as a module in another file. Implement two functions (there's a third one that's optional).

1. shuffle
2. scramble_letters
3. sort_words_by_length (optional)


shuffle(lst)
-----
parameters: 
    * lst - a list of values (any values)

return:
    * None (does not return anything)

description:

This function will shuffle the elements in a list *in place*. That is, 
the original list passed in will be modified. Do this by iterating
with indexes (for example, using a range that's defined by the length
of the list). To shuffle the list, follow these steps.

for every index in the list (except the last)
    generate a random index from all of the available indexes after the current one
    (for example, if we're at index 2 of indexes 0, 1, 2, 3, 4, 5, then the
    random index generated will be 2, 3, 4 or 5)
    swap the element at the current index with the randomly generated index...
    use idiomatic python swapping to do this: 
    some_list[i], some_list[new_i] = some_list[new_i], some_list[i] 
    remember, this will not return anything

example usage:

# note that shuffle doesn't return anything
# but instead, changes the original list
words = ['the', 'brown', 'rabbit', 'belched']
print('before', words) # before ['the', 'brown', 'rabbit', 'belched']
shuffle(words)
print('after', words) # after ['rabbit', 'belched', 'brown', 'the']


scramble_letters(word)
-----
parameters:
    * word - a string whose letters will be placed in random order

return:
    * a new string composed of all of the letters in the original string,
      but in random order

description:

scramble_letters will take a word and randomize the order of the letters in the
word. It will do this by:

1. converting the word passed in into a list of characters by using the list 
   function: list("cat") # --> ['c', 'a', 't']
2. using your shuffle function above to randomize the ordering of the characters
   in the list (remember, this doesn't return anything, it changes the list)
3. creating a string from the list of characters by putting them all together
4. returning the resulting string

# note that shuffle doesn't return anything
# but instead, changes the original list
word = 'rabbit'
scrambled = scramble_letters(word)
print(scrambled) # => 'baritb'


(OPTIONAL *CHALLENGE*) sort_words_by_length(words) 
-----
parameters: 
    * words - a list of strings
return:
    * None (instead, modifies the list in place)

description:

This is an OPTIONAL function (you can skip this and move on to the next
file)... which may be challenging to implement. This function should sort a
list of strings by their length so that the shortest string is first.

Do this by using an algorithm similar to the one described below (however
instead of sorting numbers, the function will sort strings based on their
length)

* read about this sorting algorithm in wikipedia
  wikipedia article: http://en.wikipedia.org/wiki/Bubble_sort):
	* go through every element in the list
	* compare that element to the element adjacent to it 	
	* swap the two if the second element is less than the first
	* once you reach the end, start over and do the same thing again
	* keep on repeating until you through the entire list without swapping
* test your code... for example:
	* bubble_sort([4, 5, 1]) returns [1, 4, 5]
	* bubble_sort([1, 1, 1]) returns [1, 1, 1]
	* bubble_sort([2]) returns [2]
	* bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]) 
	  returns [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

From the wikipedia article, here's an example of the algorithm at work:

First Pass:
( 5 1 4 2 8 )  ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 )  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 )  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 )  ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass:
( 1 4 2 5 8 )  ( 1 4 2 5 8 )
( 1 4 2 5 8 )  ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
Third Pass:
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
"""
