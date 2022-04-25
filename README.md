# Scrapy test

## installation
create virtual env python 3.8.9
```python
python3 -m venv venv
source venv/bin/activate
```
install scrapy
```python
pip3 install Scrapy
/Users/zhaoliang/Documents/Git/scrapy-test/venv/bin/python3 -m pip install scrapy
```

## Tutorial 
https://docs.scrapy.org/en/latest/intro/tutorial.html

### Creating a project
```
scrapy startproject tutorial
```
### Test kanasoku spider
[test kanasoku](kanasoku.md)
### Extracting data in our spider
使用yield传递收集的数据到item pipeline
### Storing the scraped data
用json储存
## 测试中间件 (middleware)
编辑process_request(self, request, spider)函数，使用selenium来发送请求。
https://testerhome.com/articles/30486

### clemfromspace/ scrapy-selenium
https://github.com/clemfromspace/scrapy-selenium
### Install the scrapy selenium package
```
pip install scrapy-selenium
>>>Successfully installed scrapy-selenium-0.0.7
```
# Test Selenium
[test selenium](selenium.md)
# Crawl shein.com
[Crawl shein.com](shein.md)

# 其他
+ Available tool commands¶
  https://docs.scrapy.org/en/latest/topics/commands.html
+ Configuration settings
  https://docs.scrapy.org/en/latest/topics/commands.html#configuration-settings
+ Pipeline与数据库
  https://docs.scrapy.org/en/latest/topics/item-pipeline.html#item-pipeline
+ Deploying Spiders 
  https://docs.scrapy.org/en/latest/topics/deploy.html#topics-deploy
+ 避免反爬
  https://docs.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned
+ 动态渲染网页爬取
 https://docs.scrapy.org/en/latest/topics/dynamic-content.html