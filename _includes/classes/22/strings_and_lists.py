monsters = ['zombies', 'vampires', 'mummies']
oz = "lions and tigers and bears, oh my"
print(" yikes! ".join(monsters))
# probably not as readable to do this, but...
print(oz[:oz.find(',')].split(" and "))

