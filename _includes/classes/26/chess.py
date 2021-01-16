board = ""
for number in range(8, 0, -1):
    row = ""
    for letter in "abcdefgh":
        row += letter + str(number) + " "
    board += row + "\n"
print(board)
