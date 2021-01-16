"""
keys (properties) will be double quoted
values can be arrays (python lists) other objects (dictionaries), numbers
{"key":"val", "key2": [1, 2, 3], "key3": {"yes":"ok"}}
"""
"""
import json
with open('/tmp/me.json', 'r') as f:
    result = f.read()
    print(result)
    d = json.loads(result)
    print(d)
    print(d['first'])
    s = json.dumps(d)
    print('this is a string of json' + s)
"""


