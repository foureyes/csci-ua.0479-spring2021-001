# The Stranger, Manufacturing Consent...
philosophers = ['Camus', 'Chomsky']
# The Art of Computer Programming,  C
famous_computer_scientists = ['Knuth', 'Ritchie']
# lambda calculus, turing machine
logicians = ['Church', 'Turing']
letters = ['a', 'b', 'c']

result_append = famous_computer_scientists.append(logicians)
result_extend = philosophers.extend(logicians)
letters.extend("xyz")

print(philosophers)
print(letters)
print(result_append)
print(result_extend)
