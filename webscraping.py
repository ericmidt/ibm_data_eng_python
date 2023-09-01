from bs4 import BeautifulSoup
import html5lib
import requests
import pandas as pd

html_data = requests.get("https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks")
print(html_data)
html_data = html_data.text

soup = BeautifulSoup(html_data, 'html5lib')

with open('webscraping.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

tag_object = soup.table.prettify()

with open('table.html', 'w', encoding='utf-8') as f:
    f.write(tag_object)