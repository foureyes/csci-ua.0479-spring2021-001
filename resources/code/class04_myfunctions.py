
"""
design a function that does this for us:

    determines whether or not an item is within a list
    what's the input to this function (parameters)
    what will it do (the function body)
    what does it give back (what does it return?)
"""
"""
myfunctions.py
"""
def in_list(search, lst):
    found = False
    for ele in lst:
        if search == ele:
            found = True
    return found

def foo():
    print('another function')

# am i being run as a file
# or am i being imported
if __name__ == '__main__':
    print('in module')


























