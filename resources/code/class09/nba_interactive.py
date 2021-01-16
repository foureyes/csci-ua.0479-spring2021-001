"""
nba_interactive.py
=====
Using the report.csv file generated from nba.py, create an interactive
program that allows a user to enter a player's name, and, in response,
the program will display that player's shooting percentage. The program
will continually ask for a player name. If the user types in q or quit 
in any casing, then the program will stop asking for names.

To write this program:

1. read the file, report.csv
2. as you read in the file, add each player's name to a dictionary as a
   key... and each player's shooting percentage as the value:
   {"Kevin Durant": 0.51, ...}
3. continually ask the user for a player name
4. if they don't enter q, look up that player in the dictionary and print
   out their shooting percentage

Example output
-----
Enter player name
> Kevin Durant
0.51


"""
