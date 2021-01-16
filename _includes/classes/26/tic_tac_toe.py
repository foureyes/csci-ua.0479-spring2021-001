tic_tac_toe = [[" ", " ", " "],[" ", "x", " "],["o", "o", "x"]]
s = "-------\n"
for inner in tic_tac_toe:
    row = "|"
    for letter in inner:
        row += letter + "|"
    row += "\n-------\n"
    s += row
print(s)
