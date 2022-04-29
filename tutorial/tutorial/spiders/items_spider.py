import scrapy
import json
import pymongo
# from shutil import which
# from scrapy_selenium import SeleniumRequest

# SELENIUM_DRIVER_NAME = 'edge'
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('msedgedriver')
# SELENIUM_DRIVER_ARGUMENTS = ['--headless']


class SheinSpider(scrapy.Spider):
    name = "shein_items"

    def load_db(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mongotest"]
        self.col = db["urls"]

    def start_requests(self):
        self.load_db()
        # urls = [
        #     "https://jp.shein.com/Women-Blouses-c-1733.html"
        # ]
        base_url = "https://jp.shein.com/Women-Blouses-c-1733.html?page="
        for pageno in range(2, 20):
            url = base_url + str(pageno)
            yield scrapy.Request(url=url, callback=self.parse)
            # yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        try:
            item_urls = response.css(
                "div.S-product-item__wrapper a::attr(href)").getall()
            print(item_urls)
        except Exception:
            print("Can not load goods")
        try:
            item_urls_json = [{"url": iu} for iu in item_urls]
            res = self.col.insert_many(item_urls_json)
            print("inserted: ", res.inserted_ids)
        except Exception:
            print("bulk write error")

            # title = response.css("h1.product-intro__head-name::text").get()
            # print(title)
            # print(response.selector.xpath('//title/@text'))
            # page = response.url.split("/")[-1]
            # filename = f'shein-{page}.html'
            # with open(filename, 'wb') as f:
            #     f.write(response.body)
            # for title in response.css("h2 a"):
            #     yield {
            #         "title": title.css("a::text").get(),
            #         "url": title.css("a::attr(href)").get(),
            #     }
            # self.log(f'Saved file {filename}')
