p = (4, 2)

p[0] <--0???


p['x']









NAME = 0
FGA = 1


line[NAME]
line[FGA]

import random

def create_thesaurus(fn):
    thesaurus = {}
    fread = open(fn, 'r')
    # go over every line in file
    for line in fread:

        # clean up the line by removing leading and trailing white space
        line = line.strip()

        # break apart line into separate words
        line_parts = line.split(',')

        # key is first word
        k = line_parts[0]

        # value is all other words after as a list
        v = line_parts[1:]

        # add new key value
        thesaurus[k] = v

    fread.close()

    return thesaurus

# accumulator... is a dictionary
# because we want to key in for easy access
# to synonyms (start as empty)
thesaurus = create_thesaurus('thesaurus.txt')

def remove_punctuation(s):
    new_s = ''
    for ch in s:
        if ch.isalnum() or ch == ' ':
            new_s += ch
    return new_s

lyrics_file = open('bad_blood.txt', 'r')
phrase = lyrics_file.read()

# maybe get rid of punctuation in input
phrase = remove_punctuation(phrase)

# break apart input into words
words = phrase.split(' ')

new_phrase = []

# go over every word
for w in words:
    # get value at key, w... if it doesn't exist, then value is just w
    # new_phrase.append(thesaurus.get(w, w))
    k = w.lower()
    if k in thesaurus:
        # choose a random word from the list
        possible_words = thesaurus[k]
        new_word = random.choice(possible_words)
        new_phrase.append(new_word.upper())
    else:
        new_phrase.append(w)

print(' '.join(new_phrase))
# add the synonym
# otherwise, add the word itself













