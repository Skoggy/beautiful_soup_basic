
from bs4 import BeautifulSoup
import requests

jessica_author = 'Jessica Skogstad'

# def find_articles():
html_text = requests.get('https://www.mumstrife.com/').text
soup = BeautifulSoup(html_text, 'lxml')

articles = soup.find_all('li', class_='list-post magazine-layout magazine-1')


for index, article in enumerate(articles):
    author = article.find('span', class_='author-italic author vcard').text
    if jessica_author in author:
        published_date = article.find('time', class_='entry-date published')
        header = article.find('h2', class_='entry-title grid-title').text
        teaser = article.find('div', class_='item-content entry-content').text
        with open(f'articles/{index}.txt', 'w') as f:
            f.write(f"Headline: {header.strip()} \n")
            f.write(f"Written by: {author.strip()} \n")
            f.write(f"Published on: {published_date.text} \n")
            f.write(f"Teaser: {teaser.strip()}")
        print(f'File Saved: {index}')
