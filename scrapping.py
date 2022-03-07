import requests
result = requests.get("https://example.com/")
print(type(result))
print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup)
print(soup.select('title'))
print(soup.select('p'))
print(soup.select('title')[0].getText())

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,"lxml")
print(type(soup.select('.toctext')[0]))