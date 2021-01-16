from bs4 import BeautifulSoup
s = """
<html>
    <body>
	<h1>foo</h1>
	<p>bar
	<h1 class='even-headier'>baz</h1>
	<a href='http://cs.nyu.edu'>cs!</a>
	</p>
    </body>
</html>
"""
# object that we get back represents an html document
# 2nd argument is the parser you want to use
# html parser is built in
dom = BeautifulSoup(s, "html.parser")

# dom <-- this is an object that represents document
# we can ask it some questions: can you pull out all elements
# that match a criteria
print(dom.select('h1')[0].get_text())










