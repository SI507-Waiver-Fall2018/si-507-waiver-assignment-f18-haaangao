# Han Gao / hangao

# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

print('***** Part 3 Output *****')

base_url = "https://www.michigandaily.com"
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')

most_read_raw = soup.find(class_='view-most-read')
most_read_title_raw = most_read_raw.find_all('li')

most_read_title = []
for title in most_read_title_raw:
    most_read_title.append(title.string)

# print(most_read_title)

most_read_url = []
for link in most_read_raw.find_all('a'):
    most_read_url.append(base_url + link.attrs['href'])

most_read_author = []
for url in most_read_url:
    page_most_read = requests.get(url)
    soup_most_read = BeautifulSoup(page_most_read.content, 'html.parser')

    author = soup_most_read.find(class_='byline')
    
    if (author != None):
        a = author.next_element.next_element.next_element.string
        most_read_author.append(a)
    else:
        most_read_author.append("No Author Available")

# print(most_read_author)

for i in range(len(most_read_title)):
    print(most_read_title[i], "\n by", most_read_author[i])