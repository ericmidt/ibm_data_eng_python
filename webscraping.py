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

data_list = []

for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) >= 3:
        name = columns[1].find_all('a')[1].text.strip()
        market_cap = columns[2].text.strip()  # Extract the market cap
        data_list.append({"Name": name, "Market Cap (US$ Billion)": market_cap})

df = pd.DataFrame(data_list)

print(df.head())

json_file_path = 'banks_data.json'
df.to_json(json_file_path, orient='records')