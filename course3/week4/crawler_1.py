import urllib.request
from bs4 import BeautifulSoup

file_handler = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_627076.html').read()
soup = BeautifulSoup(file_handler, 'html.parser')

print(sum([ int(tag.getText()) for tag in soup('span') ]))