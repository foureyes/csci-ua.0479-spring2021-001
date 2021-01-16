def filter_words_from_file(fn, rules=lambda word:True):
    """Reads in file of words (assuming 1 word per ine), fn, and:

     * creates a new list to store words from the file
     * goes through every line extracting words by removing leading and
       trailing whitespace
     * if word passes test specified by function, rules, adds word to list
     * (by default, the rules function will allow all words)

    :param fn: file name that contains words
    :type fn: str
    :param rules: a function that takes one parameter, a word, and returns
    True if it should be added to the list of words; False otherwise
    :type rules: function
    :return: a list of "processed" and filtered words
    :rtype: list
    """
    print("IMPLEMENT ME!")


def combinations(words):
    """Creates a list of 2-element tuples by going through every combination
    of words in list, words. It ignores combinations where both words are
    the same word, but allows combinations of differently ordered tuples -
    ('foo', 'bar') and ('bar', 'foo') are both included. Do not use the
    itertools module to do this.

    print(combinations(['pizza', 'cookies', 'cactus']))
    # prints out the following list of tuples -->
    # [('pizza', 'cookies'), ('pizza', 'cactus'),
    #    ('cookies', 'pizza'), ('cookies', 'cactus'),
    #    ('cactus', 'pizza'), ('cactus', 'cookies')]

    :param words: list of words to make combinations of
    :type words: list
    :return: all combinations of words as 2 element tuples in list
    :rtype: list of tuples
    """
    print("IMPLEMENT ME!")


def generate_password_file(source_fn, dest_fn, rules=lambda word:true):
    """Generates a file containing usernames and passwords based on a list
    of words read in from another file. Using the other functions in this
    module this function:

    * reads in words from source_fn
    * remove leading and trailing whitespace from all words
    * filter out words that don't pass the rules function, rules
    * generate all possible combinations of words
    * writes out combinations as username password in file

    # For example using an input file called words.txt, (the format is a
    # single word on each line):

    # pizza
    # cookies
    # cactus

    # And using the following function as the rules function:

    def starts_with_c(word):
        return word[0] == 'c'

    # call generate_password_file...

    generate_password_file('words.txt', 'passwords.txt', rules=starts_with_c)

    # to produce a file called passwords.txt... that contains usernames and
    # passwords separated by a colon (:) with each pair on a its own line:

    # cookies:cactus
    # cactus:cookies

    :param source_fn: name of file that contains words to use as usernames and
    passwords
    :type source_fn: str
    :param dest_fn: name of file usernames and passwords will be written to
    :type dest_fn: str
    :param rules: function to determine what words to include
    :type rules: function
    :return: does not return a value (only writes a file)
    :rtype: None
    """
    print("IMPLEMENT ME!")


def load_password_file(pw_fn, delimiter=':'):
    """Reads in a password file in the format:

    username1:password1
    username2:password2
    username3:password3

    and gives back a list of 2 element tuples:

    [(username1:password1), (username2:password2), (username3:password3)]

    :param pw_fn:
    :type pw_fn: name of password file to read in
    :param delimiter: the character that separates a username and password in file
    (the default is colon - :)
    :return: a list of tuples with each tuple representing a username and password
    combination from the file
    :rtype: list of tuples
    """
    print("IMPLEMENT ME!")




if __name__ == "__main__":
    """
    * define the following rules function: both the username and password
      have 2 s's, they both contain at least one o, the first letter is
      either an h or a v, and each word is at least 14 characters long
    * call generate_password_file with the rules function that you've 
      defined so that it reads in the words file, and writes everything 
      out to passwords.txt
    """
    print("IMPLEMENT ME!")


