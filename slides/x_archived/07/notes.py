"""
what does pop return tuple or value?
multiple charts

## file and open
* file object
* open
* r, w, a
* remember to close

## read
* reading 
* for loop
* readlines
* readline
* read

## write
with open('foo.txt', 'w') as f:
    f.write("bar")


urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)



## split

## csv
import csv
with open('survey-results.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

response = request.urlopen('http://data.nba.com/data/15m/json/cms/noseason/game/20121126/0021200013/boxscore.json')
response.read()
json.dumps
json.loads

>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()



"""

word = input("gimme word>\n")
# keys are letters
# values are going to be counts
d = {}
for ch in word:
    #value if condition else other_value
    d[ch] = 1 if ch not in d else d[ch] + 1
    d[ch] = d.get(ch, 0) + 1
    # d.get(k, [d])
    """
    try:
        d[ch] += 1
    except KeyError:
        d[ch] = 1
    """

for k in sorted(d, key=d.get):
    print(k, d[k])




















