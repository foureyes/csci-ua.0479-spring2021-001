import urllib.request, json

# we're going to ask tumblr for some posts ...
search_tag = 'cat'
api_key = 'XBu4Lke6Cyh2UrLFIZW0jIo79sUT8EwtruJduMAknEUNhccNwY'
post_type = 'text'
url = 'http://api.tumblr.com/v2/tagged?api_key=' + api_key 
url = url + '&tag=' + search_tag

response = urllib.request.urlopen(url).read().decode('utf-8')
posts  = json.loads(response)['response']

for post in posts:
    if post['type'] == 'photo':
        tags = post['tags']
        photo = post['photos'][0]
        number_of_tags = len(tags)
        if number_of_tags > 2:
            print(tags)
            print(photo['original_size']['url'] + "\n\n")
