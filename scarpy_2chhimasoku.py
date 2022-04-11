from urllib import request
from bs4 import BeautifulSoup
# !pip install scrapy
# !pip install beautifulsoup4

urls = []
for n in range(2, 11):
    response = request.urlopen('http://himasoku.com/?p=' + str(n))
    soup = BeautifulSoup(response)
    response.close()
    h2s = soup.find_all("h2", class_="article-title entry-title")
    for u in h2s:
        urls.append(u.a.get('href'))

urls

lines = []
for url in urls:
    response = request.urlopen(url)
    soup = BeautifulSoup(response)
    response.close()
    title = soup.find("h2", class_="article-title entry-title")
    lines.append(title.text)
    res = soup.find_all('div', class_="t_b")
    for r in res:
        lines.append(r.text + "\n")

with open('himasoku3.txt', 'w') as f:
    f.writelines(lines)
