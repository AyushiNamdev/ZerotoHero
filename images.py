#GOAL= get the title of every book with a two star rating

import requests
import bs4
print('http://books.toscrape.com/catalogue/page-2.html')
print('http://books.toscrape.com/catalogue/page-3.html')
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page_num = 12
print(base_url.format(page_num))

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
products = soup.select(".product_pod")
example = products[0]
example.select(".star-rating.Three")
print(example.select('a')[1]['title'])

#we can check if something is 2 stars(string call in, example.select(rating))

two_star_titles = []
for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)



