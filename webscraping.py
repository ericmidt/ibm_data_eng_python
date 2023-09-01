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

# Get third table
table = soup.find_all('table')[2]

table_html = table.prettify()

with open("table.html", "w", encoding="utf-8") as f:
    f.write(table_html)

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in table.find_all('tr'):
    columns = row.find_all('td')
    for column in columns:
        print(column.string)
    # name = col[1].string
    # market_cap = col[3].string
    # data = data.append({"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True)

print(data.head())