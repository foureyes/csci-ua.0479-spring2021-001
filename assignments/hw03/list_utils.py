def shift_left(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the left, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)  # no return value
    print(numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    print("IMPLEMENT ME!")


def shifted_left(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the left, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_left(numbers, 2)
    print(shifted_numbers) # --> [3, 4, 0, 0]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """
    print("IMPLEMENT ME!")


def shift_right(lst, n, fill_value=0):
    """Shifts all elements in a list n places to the right, and fills in the
    vacant list positions with fill_value. This should not return a new
    list; instead it should change the incoming list, lst, in place.

    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)  # no return value
    print(numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    print("IMPLEMENT ME!")


def shifted_right(lst, n, fill_value=0):
    """Creates a new list in which all elements from the original list
    passed in are shifted n places to the right, with the remaining vacant
    list positions filled in with fill_value. The new list is returned

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_right(numbers, 2)
    print(shifted_numbers) # --> [0, 0, 1, 2]

    :param lst: list to be shifted
    :type lst: list
    :param n: the number of places to shift each element
    :type n: int
    :param fill_value: the value filled in for the vacant spaces left after
    the shift
    :type fill_value: any
    :return: new list with values shifted
    :rtype: list
    """
    print("IMPLEMENT ME!")



def fill(lst, fill_value=0):
    """Fills an existing list, lst, with the value, fill_value.

    numbers = [1, 2, 3, 4]
    fill(numbers)
    print(numbers) # [0, 0, 0, 0]

    :param lst: the list to be filled with values
    :type lst: list
    :param fill_value: the value to fill the list with
    :type fill_value: any
    :return: does not return a value
    :rtype: None
    """
    print("IMPLEMENT ME!")



def filled(lst, fill_value=0):
    """Creates a new list with the same length as the list passed in, lst,
    and fills it with the value, fill_value.

    numbers = [1, 2, 3, 4]
    filled_list = fill(numbers)
    print(filled_list) # [0, 0, 0, 0]

    :param lst: the list to use as the basis for the length of the new list
    :type lst: list
    :param fill_value: the value to fill the new list with
    :type fill_value: any
    :return: the new list filled with fill_value
    :rtype: list
    """
    print("IMPLEMENT ME!")



def mean(lst):
    """Calculates and returns the average of all numbers in incoming list, lst.

    print(mean([12, 4, 14])) # --> 10

    :param lst: list of numeric types
    :type lst: list
    :return: the average of all numbers in lst
    :rtype: float
    """
    print("IMPLEMENT ME!")


def median(lst):
    """Calculates the median of incoming list, lst.

    :param lst: list of numeric types
    :type lst: list
    :return: the median of all numbers in lst
    :rtype: int or float
    """
    print("IMPLEMENT ME!")


def std_dev(lst):
    """Calculates the standard deviation of the sample for the incoming list, lst.

    :param lst: list of numeric types
    :type lst: list
    :return: the standard devation of numbers in incoming list, lst
    :rtype: float
    """
    print("IMPLEMENT ME!")


if __name__ == '__main__':
    print("put your test cases here")


