"""
Twitter users prefix their tweets with "RT" to signify 
that they're repeating another person's tweet ("retweeting").
"""
import urllib.request, json

url = 'http://search.twitter.com/search.json?q=cats'
response = urllib.request.urlopen(url).readall().decode('utf-8')
tweets  = json.loads(response)['results']

for tweet in tweets:
    if tweet['text'].startswith('RT'):
        print(tweet['from_user'] + " retweeted somthing.")
    else:
        print(tweet['from_user'] + " said " + tweet['text'])

