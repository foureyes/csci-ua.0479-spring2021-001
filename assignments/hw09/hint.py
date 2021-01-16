"""
You have a file called zips.txt

11211|10012|11364|10457|NY
06927|06532|CT
08720|07470|07030|NJ
15042|15043|15044|15046|PA
19970|DE

Write a program that:

* reads in zips.txt
* asks for a state abbreviation by displaying the possible state abbreviations
  that can be entered (based on the contents of the file)
* and, depending on the user input...
    * will print out the zip codes for that state __in order__
    * or print out "I don't know that state" if the input doesn't match

Example Interaction 1:
-----

Please enter a state (your options are NY,CT,NJ,PA,DE)
> CT

The zip codes for CT are:

06532
06927

Example Interaction 2:
-----

Please enter a state (your options are NY,CT,NJ,PA,DE)
> CA

I don't know that state.

"""
