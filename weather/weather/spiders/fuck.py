# -*- coding: utf-8 -*-
import scrapy


class FuckSpider(scrapy.Spider):
    name = "fuck"
    allowed_domains = ["www.baidu.com"]
    start_urls = (
        'http://www.www.baidu.com/',
    )

    def parse(self, response):
        pass
