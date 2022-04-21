import scrapy


class SheinSpider(scrapy.Spider):
    name = "shein"

    def start_requests(self):
        urls = [
            "https://jp.shein.com/Honeyspot-Solid-Drop-Shoulder-Oversized-Blouse-p-10209809-cat-1733.html"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'shein-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        # for title in response.css("h2 a"):
        #     yield {
        #         "title": title.css("a::text").get(),
        #         "url": title.css("a::attr(href)").get(),
        #     }

        # self.log(f'Saved file {filename}')
