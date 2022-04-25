import scrapy
import json
# from shutil import which
# from scrapy_selenium import SeleniumRequest

# SELENIUM_DRIVER_NAME = 'edge'
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('msedgedriver')
# SELENIUM_DRIVER_ARGUMENTS = ['--headless']


class SheinSpider(scrapy.Spider):
    name = "shein"

    def start_requests(self):
        urls = [
            # "https://jp.shein.com/Honeyspot-Solid-Drop-Shoulder-Oversized-Blouse-p-10209809-cat-1733.html"
            # "https://jp.shein.com/DAZY-Bishop-Sleeve-Sheer-Blouse-p-9973864-cat-1733.html"
            # "https://uiuret.hatenablog.com/entry/2022/04/23/125305"
            "https://jp.shein.com/Rhinestone-Rib-knit-Sports-Brief-p-10283098-cat-3056.html"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            # yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        try:
            shein_script = response.css("script")[12].get()
            ssdata = json.loads(shein_script.split("productIntroData:")[
                                1].split(",\n        abt: ")[0])
            goods_name = ssdata["detail"]["goods_name"]
            skc = ssdata["getSeriesAndBrand"]["skc"]
            print(goods_name, skc)
        except Exception:
            print("Can not load goods")
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
