
def contact_as_string(contact):
	s = ''
	for attribute, value in contact.items():
		s += '%s - %s\n' % (attribute, value)
	return s

def print_all_contacts(contact_list):
	for c in contact_list:
		print(contact_as_string(c))

def find_contact(contact_list, attribute, value):
	for c in contact_list:	
		if c[attribute] == value:
			return c
	return None

def find_contact_by_first(contact_list, first):
	return find_contact(contact_list, 'first name', first)

contacts = [{'first name': 'tabitha', 'last name': 'test', 'room': 100}]
while True:
	command = input('(a)dd contact, (p)rint all contacts, (f)ind contact, (q)uit \n>')
	if command == 'a':
		first = input('first name plz \n>')
		last = input('last name plz \n>')
		room = input('room # plz \n>')
		contacts.append({'first name': first, 'last name': last, 'room': room})
	elif command == 'p':
		print_all_contacts(contacts)
	elif command == 'f':
		name_to_find = input('what\'s the firs name of the person you\'d like to find? \n>')
		c = find_contact_by_first(contacts, name_to_find)
		if c != None:
			print(contact_as_string(c))
		else:
			print('Contact not found')
	elif command == 'q':
		break
