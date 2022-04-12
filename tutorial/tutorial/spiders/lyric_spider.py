
import scrapy


class KanasokuSpider(scrapy.Spider):
    name = "lyric"

    def start_requests(self):
        urls = [
            'http://kanasoku.info/?page=1',
            'http://kanasoku.info/?page=2',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-1][-1]
        # filename = f'kanasoku-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for title in response.css("h2 a"):
            yield {
                "title": title.css("a::text").get(),
                "url": title.css("a::attr(href)").get(),
            }

        # self.log(f'Saved file {filename}')
