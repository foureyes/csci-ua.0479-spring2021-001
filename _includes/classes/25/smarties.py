smarties = [("Mr", "Sam", "Smartypants"), ("Ms", "Nelly", "Knowitall")]

def hello_v1(t):
	for person in t:
		print("Hello %s. %s!" % (person[0], person[2]))

def hello_v2(t):
	for title, first, last in t:
		print("Hello %s. %s!" % (title, last))


hello_v1(smarties)
hello_v2(smarties)
