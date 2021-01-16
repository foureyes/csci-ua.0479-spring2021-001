"""
roommate.py
=====
Your roommate keeps on eating your food, but refuses to admit doing so! To
catch your roommate in the act, you decide to begin keeping inventory of 
all of your fruits, vegetables and other snacks. Write a short program that 
keeps track of the quantity of arbitrary foods in your house by allowing 
you to enter food items and their quantity. 

a) continually ask user to add a food and a quantity in the format: 
   item,number (comma separated: orange,3)
b) ...or enter q to quit
c) if it's not q or if it doesn't have a comma, then just ask again
d) if the food doesn't exist in the inventory yet, start keeping track of 
   it, and set its quantity to the quantity given
e) if the food already exists in your inventory, increment the quantity by 
   the quantity given
f) after a new food item is entered, print out the current inventory as: 
   [quantity] x [item]
g) hint: what data type would best be suited for storing the items and quantities of your inventory?
h) example output (text after the > symbol is user input):

Enter (food),(quantity) or (q)uit
> orange,3
3 x orange
Enter (food),(quantity) or (q)uit
> banana,1
3 x orange
1 x banana
Enter (food),(quantity) or (q)uit
> orange,5
8 x orange
1 x banana
Enter (food),(quantity) or (q)uit
> q
"""
