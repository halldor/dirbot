import scrapy

from ..items import Website


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name url description
        @returns items 1
        """
        selector = "//div[contains(@class, 'site-item')]/div[contains(@class, 'title-and-desc')]"
        for site in response.xpath(selector):
            item = Website()
            item['url'] = site.xpath("a/@href").extract_first()
            item['name'] = site.xpath("a/div[contains(@class, 'site-title')]/text()").extract_first()
            item['description'] = site.xpath("div[contains(@class, 'site-descr')]/text()").re_first('\s*([^\n]*)\\r')
            yield item
