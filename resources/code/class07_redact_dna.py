"""
redact(words, illegal_words)
word is a list of strings
illegal_words also a list of strings

if one of the strings in words exists in illegal words
then "replace" the first three letters with dashes
otherwise, word stays the same
if less than 3, then all chars

returns an entirely new list composed of censored words
"""
"""
def redact(words, illegal_words):
    new_words = []
    for word in words:
        if word in illegal_words:
            if len(word) <= 3:
                redacted_word = len(word) * '-'
            else:
                redacted_word = '---' + word[3:]
            new_words.append(redacted_word)
        else:
            new_words.append(word)

    return new_words
print(redact(['a', 'very', 'delicious', 'cake', 'for', 'me'], ['delicious', 'cake', 'me']))
"""
"""
codons
3 of ACTG

 |
\/
AAG-CCA-ATG

CAG-TCA
"""
"""
import random
def gen_dna(codons):
    dna = ''
    for i in range(codons):
        # if we are on the last index....
        dna += gen_codon()
        if i < codons - 1:
            dna += '-';
    return dna

def gen_codon():
    letters = 'ACTG'
    codon = ''
    for i in range(3):
        n = random.randint(0, 3)
        letter = letters[n]
        codon += letter
    return codon
    
print(gen_dna(3))
print(gen_dna(7))
"""
"""
# split and join
# split turn string into list
# join turn list into string
# both are called as methods on a string

names = 'alice and bob and carol'
names_as_list = names.split(' and ')
print(names_as_list)
print('---'.join(names_as_list))
"""





















