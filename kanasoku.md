# test kanasoku spider
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
