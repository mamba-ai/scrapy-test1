import scrapy
import json
import pymongo
# from shutil import which
# from scrapy_selenium import SeleniumRequest

# SELENIUM_DRIVER_NAME = 'edge'
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('msedgedriver')
# SELENIUM_DRIVER_ARGUMENTS = ['--headless']


class SheinSpider(scrapy.Spider):
    name = "shein"

    def load_db(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mongotest"]
        self.items_col = db["items"]
        self.urls_col = db["urls"]
        self.url_cursor = self.urls_col.find()

    def start_requests(self):
        self.load_db()
        # urls = [
        #     # "https://jp.shein.com/Honeyspot-Solid-Drop-Shoulder-Oversized-Blouse-p-10209809-cat-1733.html"
        #     # "https://jp.shein.com/DAZY-Bishop-Sleeve-Sheer-Blouse-p-9973864-cat-1733.html"
        #     # "https://uiuret.hatenablog.com/entry/2022/04/23/125305"
        #     "https://jp.shein.com/Rhinestone-Rib-knit-Sports-Brief-p-10283098-cat-3056.html"
        # ]
        base_url = "https://jp.shein.com"

        for url_entry in self.url_cursor:
            self.current_url = url_entry["url"]
            url = base_url + url_entry["url"]
            self.current_url_id = url_entry["_id"]
            yield scrapy.Request(url=url, callback=self.parse)
            # yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        try:
            shein_script = response.css("script")[12].get()
            ssdata = json.loads(shein_script.split("productIntroData:")[
                                1].split(",\n        abt: ")[0])
            goods_name = ssdata["detail"]["goods_name"]
            print("goods_name", goods_name)
            data_entry = {
                "url_id": self.current_url_id,
                "url": self.current_url,
                "data": ssdata
            }
            res = self.items_col.insert_one(data_entry)
            print(goods_name, " inserted, id=", res.inserted_id)
            # self.log(f'Saved item {goods_name}')
        except Exception:
            print("Can not load goods")
        try:
            print("currentid", self.current_url_id)
            url_filter = {"_id": self.current_url_id}
            self.urls_col.update_one(
                url_filter, {"$currentDate": {"lastUpdated": True}})
        except Exception:
            print("Can not update url")

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
