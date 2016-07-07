# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from db_spider.items import DbSpiderItem


class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = (
        'https://www.douban.com/tag/%E6%8E%A8%E7%90%86/book?start=0',
    )
    rules = (
        Rule(LinkExtractor(allow=r'start=\d{1,3}$'),callback='parse_item',follow=True),
    )

    def parse_item(self,response):
        items = []
        book_list = response.xpath('//div[@class="mod book-list"]/dl')
        for book in book_list:
            item = DbSpiderItem()
            try:
                item['book_name'] = book.xpath('dd/a/text()').extract()[0]
                item['book_star'] = book.xpath('dd/div[2]/span[1]/@class').extract()[0][7:]
                item['book_rating'] = book.xpath('dd/div[2]/span[2]/text()').extract()[0]
                desc = book.xpath('dd/div[1]/dl[1]/dd/div[1]/text()').extract()[0].strip().split('/')
                item['book_price'] = desc.pop()
                item['book_publish_time'] = desc.pop()
                item['book_publish'] = desc.pop()
                item['book_author'] = '/'.join(desc)
            except:
                pass
            items.append(item)
        return items

