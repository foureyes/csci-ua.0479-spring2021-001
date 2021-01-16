"""
change_puhleese.py (15 points)
=====
You're the manager of a tiny boutique that sells Python related gifts and 
knick-knacks (like plush Python stuffed animals, Guido Van Rossum bobble head
dolls, etc. ). Unfortunately, you don't have any paper bills on hand, you only 
have coins! 

To help you calculate change, you reprogram you cash register to print out the 
exact change that's needed, broken down by quarters, dimes, nickels and pennies.

Here's what your program should do:

1. Ask the cashier for information regarding the items purchased. It will 
   assume that everyone buys exactly three items (!?). For every item:
   a. ask for name of the item
   b. ask for the price (assume that users will always enter a number with a 
      decimal point)
   c. ask for quantity (assume that users will always enter a whole number)
2. Ask the cashier for how much the user paid. Assume that the amount paid
   is at least as much as the total owed (including sales tax)
3. Print out a receipt that contains the following information:
   a. name, price, quantity and total cost per item purchased
   b. the total cost of all of the items
   c. the sales tax based on the cost of all of the items - sales tax in the
      city is 8.875%
   d. the total amount owed, including sales tax
   e. the total amount paid
   f. the change owed, followed by a break down of how many quarters, dimes, 
      nickels and pennies will be given back
      * it will always print out the number of coins for each denomination, 
        even if the quantity is 0
   g. __IT IS OK IF SOME OF YOUR CALCULATIONS ARE OFF BY 1 CENT__
4. The receipt should be in the following format:
   a. the width of the receipt is 80 characters long total
   b. it has a center aligned title: PREMIER PYTHON PLAZA RECEIPT
   c. followed by a line created by equal signs that's 80 characters long (===)
      * __DO NOT TYPE OUT__ 80 ='s ... use what we learned about Python types,
        operators, etc. to do this
   d. print out the costs per item...
   e. print out another line created by equal signs
   f. print out the calculations for total item cost, sales tax, etc.
   g. print out another line created by equal signs
   h. print out the number of quarters, dimes, etc.
   i. "headings" in a line are left justified: item name x quantity ... cost
   j. prices / costs:
      * are right justified
      * have a dollar sign
      * have two decimal places
      * hint: you may have to use format more than once to get the decimal
        places... but then you'll need to add a dollar and format again!
   k. assume that all item names and costs are less than 40 characters long
   l. see the sample interaction below
      * everything after the > (greater than sign) is user input
      * the receipt is at the end
      * __YOUR OUTPUT SHOULD MATCH THE OUTPUT BELOW!__
5. __COMMENT YOUR SOURCE CODE__ by 
   a. briefly describing sections of your program (for example "# calculates the number of quarters, dimes, nickels and pennies" could go above the part of your code that runs those calculations). 
   b. include your name, the date, and your class section at top of your file (above everything else)

What is the name of the first item?
> Guido Van Rossum Bobble Head
How much does the first item cost?
> 10
How many are being purchased?
> 3
What is the name of the second item?
> Python Stuffed Animal
How much does the second item cost?
> 29.99
How many are being purchased?
> 1
What is the name of the third item?
> Hello World T-Shirt
How much does the third item cost?
> 12.50
How many are being purchased?
> 3
How much was paid?
> 150.03
....
4388
175
<class 'int'>
                          PREMIER PYTHON PLAZA RECEIPT
================================================================================
3 x Guido Van Rossum Bobble Head                                          $30.00
1 x Python Stuffed Animal                                                 $29.99
3 x Hello World T-Shirt                                                   $37.50
================================================================================
TOTAL COST OF ITEMS                                                       $97.49
SALES TAX                                                                  $8.65
AMOUNT OWED                                                              $106.14
AMOUNT PAID                                                              $150.03
CHANGE                                                                    $43.89
================================================================================
CHANGE:
175 x quarters
1 x dimes
0 x nickels
4 x pennies
"""

