thesaurus = { 
    "happy": "glad",
    "sad"  : "bleak" 
}

def remove_punctuation(s):
    new_s = ''
    for ch in s:
        if ch.isalnum() or ch == ' ':
            new_s += ch
    return new_s

# ask for input
phrase = input('give me a phrase\n>')

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
        new_phrase.append(thesaurus[k].upper())
    else:
        new_phrase.append(w)

print(' '.join(new_phrase))
# add the synonym
# otherwise, add the word itself












