from requests import get
from bs4 import BeautifulSoup
import sys
import json


isbn = sys.argv[1]
url = 'https://www.goodreads.com/book/show/'+str(isbn)
print url


response = get(url)


html_soup = BeautifulSoup(response.text, 'html.parser')

reviews = html_soup.find_all('div', class_= 'reviewText stacked')
authors = html_soup.find_all('div', class_='reviewHeader uitext stacked')


list_reviews = [10]
list_authors = [10]
jsonList = []

for rev in reviews:
    if rev.span.find('span',style='display:none') is not None:
        review = rev.span.find('span',style='display:none').text
        list_reviews.append(review)
for auth in authors:
        if auth.span.a is not None:
            author = auth.span.a.text
            list_authors.append(author)
            #print author

for i in range(0,len(list_reviews)):
    jsonList.append({"author" : list_authors[i], "review" : list_reviews[i]})

print(json.dumps(jsonList, indent = 1))
