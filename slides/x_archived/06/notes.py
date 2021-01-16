# creating lists

"""
numbers = [10, 12, 5, 18, 3]
for i, number in enumerate(numbers):
  numbers[i] = number + 10
print(numbers)
"""
"""
numbers = [10, 12, 5, 18, 3]
new_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    new_numbers.append(numbers[i])
print(new_numbers)
print(numbers)
"""

numbers = [10, 12, 5, 18, 3]
print('before', numbers)
for i in range(len(numbers) // 2):
    j = len(numbers) - (i + 1)
    numbers[i], numbers[j] = numbers[j], numbers[i]
print('after', numbers)

"""
## making lists review

* list constructor
    * strings
    * any iterable
* split
* list literals
    * nested lists
    * nested tuples
    * nested dicts
    * nested strings
    * indexing into nested 
* list comprehensions
    * expression, loop, conditional

## review iteration

* regular
* with index
    * counting
    * range
    * enumerate (tuples)
#enumerate --> [(index1, value1), ... (indexn, valuen)]

## changing number of elements in list while iterating over it

adding or removing elements in a list while looping over it may yield unexpected results!

http://pythontutor.com/visualize.html#code=words+%3D+%5B'foo',+'foo',+'bar',+'baz',+'foo'%5D%0A%0A%23+maybe+this+removes+every+occurrence+of+foo%3F%0Afor+i,+word+in+enumerate(words%29%3A%0A++++print(i,+word%29%0A++++if+word+%3D%3D+'foo'%3A%0A++++++++words.remove(word%29%0Aprint(words%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=17

## iteration examples

* exercise: reverse a list in place versus return an entirely new list

    

## wait... why does in place work? (compare with string as global)
    * references
    * strings are immutable

## References

* variables - names / labels that you use to reference an object
* pythontutor

## aliasing

## multiplication

## as Arguments to Functions Again


## review Scope

* accessing global
* creating a new name in local scope (legb again)

## max, min, len, sum

* pass iterable vs separate args
    * that means it works on strings, dictionaries, etc.
* key function (do comparisons with what value?)
    * 1 argument function
    * returns a value, evaluated once, compare with that value

<pre><code data-trim contenteditable>
>>> d = {'b':24, 'c':1, 'z':15, 'h':21, 'm':100, 'y':50}
>>> d
{'y': 50, 'z': 15, 'h': 21, 'b': 24, 'c': 1, 'm': 100}
>>> max(d)
'z'
>>> max(d, key=d.get)
'm'
>>> max(5, -10, 24)
24
>>> max(5, -10, 24, key=abs)
24
>>> max(5, -10, 24, -50, key=abs)
-50
>>> def f(x):
...   return 1 / x;
...
>>> max(5, 10, 2, 1, key=f)
</code></pre>

## sorting 

* method
* write our own
* sorted

## sorted

* key again
* returns new

## selection sort

<pre><code data-trim contenteditable>
def selection_sort(li):
    for outer_index, ele in enumerate(li):
        min_index = outer_index
        for inner_index in range(outer_index + 1, len(li)):
            if li[inner_index] < li[min_index]:
                min_index = inner_index
        if min_index != outer_index:
            li[min_index], li[outer_index] = li[outer_index], li[min_index]


numbers = [64,25,12,22,11]
selection_sort(numbers)
print(numbers)
</code></pre>
 
## map and filter

* function then list
* loop over
* turn to list to see

## dictionaries

* syntax
* name value pairs
* key / index, value
    * key - immutable
    * value - any
* retrieving
    * key error
* adding a key/value pair
* removing

## looping

## methods

* keys
* values
* get
* update
* pop

## counting letters

* d[key] = d.get(key, 0) + 1
"""






