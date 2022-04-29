# Crawl shein.com
### Run spider
```
scrapy crawl shein
scrapy crawl shein_items
```


### Extracting data using the Scrapy shell
```
scrapy shell "https://jp.shein.com/Women-Blouses-c-1733.html"
```
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
# 爬取shein数据
找到对应的script
```
shein_script = response.css("script")[12].get()
```
进行分割，然后load为json
```
json.loads(shein_script.split("productIntroData:")[
                                1].split(",\n        abt: ")[0])
```

# find items
items
https://jp.shein.com/Women-Blouses-c-1733.html
## wrapper class
S-product-item__wrapper
```
response.css("div.S-product-item__wrapper")
```
## get all links in wrapper class
```
response.css("div.S-product-item__wrapper a::attr(href)").getall()
```
## next page 
https://jp.shein.com/Women-Blouses-c-1733.html?page=2

## collected items for page 1-19
https://jp.shein.com/Women-Blouses-c-1733.html?page=

## update item
To update the first document in the sample_mflix.movies collection where title equals "Tag":

db.urls.updateOne( { url: '/Cat-Print-High-Low-Hem-Button-Through-Blouse-p-6006482-cat-1733.html' },
{
   $currentDate: { lastUpdated: true } 
})

## find one not crawled
```
cursor = db.urls.find()
while cursor.hasNext():
    cursor.next()
```