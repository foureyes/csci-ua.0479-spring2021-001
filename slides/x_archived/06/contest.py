contest = [
        {'name':'alice', 'jelly':9, 'plain':3}, 
        {'name':'bob', 'jelly':1, 'plain':14},
        {'name':'carol', 'jelly':12, 'plain':0},
        {'name':'dan', 'jelly':1, 'plain':2},
        {'name':'eve', 'jelly':4, 'plain':12},
        {'name':'faythe', 'jelly':0, 'plain':5},
        {'name':'mallory', 'jelly':0, 'plain':1},
]
# who ate the most doughnuts?
def total_eaten(person):
    return person['jelly'] + person['plain']

print(max(contest, key=total_eaten))

def most_jelly(person):
    return person['jelly'] if  person['jelly'] >= 1 and person['plain'] else 0

print(max(contest, key=most_jelly))

