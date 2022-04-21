# scrapy-test1
scrapy-test1

## installation
create virtual env python 3.8.9
```python
python3 -m venv venv
source venv/bin/activate
```
install scrapy
```python
pip3 install Scrapy
```

## Tutorial 
https://docs.scrapy.org/en/latest/intro/tutorial.html

### Creating a project
```
scrapy startproject tutorial
```

### Create kanasoku spider
tutorial/tutorial/spiders/kanasoku_spider.py
### Run spider
```
scrapy crawl kanasoku
```

### Extracting data using the Scrapy shell
```
scrapy shell 'http://kanasoku.info/?page=1'
```
### Get the titles
```
response.css("h2 a").get()
>>> '<a href="http://kanasoku.info/articles/155280.html">【画像】警視庁さん、ついに萌えイラストを使って防犯アピールｗｗｗｗｗｗ</a>'
```
### Get the links
```
response.css("h2 a::attr(href)").get()
>>> 'http://kanasoku.info/articles/155280.html'
```
### Get the text
```
response.css("h2 a::text)").get()
>>> '【画像】警視庁さん、ついに萌えイラストを使って防犯アピールｗｗｗｗｗｗ'
```
### Get the all text
```
response.css("h2 a::text)").getall()
```

### Crawl and store the results in json
```
scrapy crawl kanasoku -o kanasoku.json
```

# Test Selenium
## Selenium Installation
```
pip3 install selenium
```
# Crawl shein.com
## crawl women-clothing-recommended to collect the items 
https://jp.shein.com/Clothing-c-2030.html?ici=jpen_tab01navbar03&scici=navbar_WomenHomePage~~tab01navbar03~~3~~webLink~~~~0&src_module=topcat&src_tab_page_id=page_select_class1650511045249&src_identifier=fc%3DWomen%60sc%3DCLOTHING%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar03%60jc%3Durl_https%253A%252F%252Fjp.shein.com%252FClothing-c-2030.html&srctype=category&userpath=category%3ECLOTHING

## item
https://jp.shein.com/Honeyspot-Solid-Drop-Shoulder-Cuffed-Blouse-p-9829408-cat-1733.html?src_identifier=fc%3DWomen%60sc%3DCLOTHING%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar03%60jc%3Durl_https%253A%252F%252Fjp.shein.com%252FClothing-c-2030.html&src_module=topcat&src_tab_page_id=page_select_class1650511045249&scici=navbar_WomenHomePage~~tab01navbar03~~3~~webLink~~~~0

Name: Honeyspot Solid Drop Shoulder Cuffed Blouse
SKU: sw2202142339254883
Price: ¥1,441
Color: 
Description: 
Size & Fit:
About brand: 
Pictures:
Reviews:
Category: Home  Women Clothing Women Tops, Blouses & Tee Women Blouses  Honeyspot Solid Drop Shoulder Oversized Blouse
