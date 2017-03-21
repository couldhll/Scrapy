# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from kaola.items import KaolaItem


class ProductSpider(CrawlSpider):
    name = "product"
    allowed_domains = ["kaola.com"]
    start_urls = ['http://kaola.com/']
    rules = (
        Rule(LinkExtractor(allow=(r'/category/'), unique=True), follow=True),
        Rule(LinkExtractor(allow=(r'/brand/'), unique=True), follow=True),
        Rule(LinkExtractor(allow=(r'/activity/'), unique=True), follow=True),
        Rule(LinkExtractor(allow=(r'/product/\w+.html'), unique=True), callback='parse_product'),
    )

    def parse_product(self, response):
        item = KaolaItem()
        item['name'] = response.xpath('//dt[@class="product-title"]/text()')[0].extract()
        item['price'] = response.xpath('//span[@class="PInfo_r currentPrice"]/span/text()')[0].extract()
        item['url'] = response.url
        return item
