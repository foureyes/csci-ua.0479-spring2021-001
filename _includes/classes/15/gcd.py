"""
Divide 990 by 210:  quotient 4, remainder 150; ignore quotient
Divide divisor from previous step by remainder from previous step
   divide 210 by 150: quotient 1, remainder 60; ignore quotient
Divide divisor from previous step by remainder from previous step
   divide 150 by 60: quotient 2, remainder 30; ignore quotient
Divide divisor from previous step by remainder from previous step
   divide 60 by 30: quotient 2, remainder 0.
"""
def gcd1(a, b):
	number_to_divide = a
	divisor = b
	remainder = a % divisor
	while remainder != 0:
		number_to_divide = divisor
		divisor = remainder
		remainder = number_to_divide % divisor
	return divisor

def gcd2(a, b):
	while a != b:
		if a < b:
			c = a
			a = b
			b = c
		else:
			a = a - b
	return a

def gcd3(a,b):
	while a != b:
		if a < b:
			a, b = b, a
		else:
			a = a - b
	
		
while True:
	a = int(input("a>"))
	b = int(input("b>"))
	print(gcd2(a, b))
	
