import urllib
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_247549.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")


# Retrive 
tags = soup('span')

spans = [int(tag.contents[0]) for tag in tags]
summation = sum(spans)
print (summation)
