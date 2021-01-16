def insert_spaces(word):
    """inserts spaces after every letter in word"""
    new_word = ""
    for c in word:
        new_word += c + " " 
    return new_word
assert "f i s h " == insert_spaces("fish"), "inserts spaces after every letter"
assert "" == insert_spaces(""), "empty string if word is empty"
print(insert_spaces("fish"))
