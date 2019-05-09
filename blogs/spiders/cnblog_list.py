# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from blogs.items import BlogsItem
import time
import re
import scrapy
import logging


class CnblogListSpider(Spider):
    name = 'cnblog_list'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/']

    def parse(self, response):
        logging.info('{fix}[{url}开始执行]{fix}'.format(fix='*' * 50,
                                                    url=response.request.url))
        blogs = response.xpath('//div[@class="post_item"]')
        for sel in blogs:
            item = BlogsItem()
            item["add_date"] = time.time()
            item["author"] = sel.xpath(
                ".//div[@class='post_item_foot']/a/text()").extract_first()
            item["author_link"] = sel.xpath(
                ".//div[@class='post_item_foot']/a/@href").extract_first()
            item["post_date"] = sel.xpath(
                ".//div[@class='post_item_foot']/text()").re(r'\d+.*\d+')
            if (len(item["post_date"]) > 0):
                item["post_date"] = item["post_date"][0]
            item["comment_num"] = sel.xpath(
                ".//span[@class='article_comment']/a/text()").re(r'\d+')
            if (len(item["comment_num"]) > 0):
                item["comment_num"] = item["comment_num"][0]
            item["view_num"] = sel.xpath(
                ".//span[@class='article_view']/a/text()").re(r'\d+')[0]
            item["title"] = sel.xpath(".//h3/a/text()").extract_first()
            item["link"] = sel.xpath(".//h3/a/@href").extract_first()
            item["summary"] = re.sub(
                re.compile(r"[\r\n\s]*", re.S), "", ''.join(
                    sel.xpath(
                        ".//p[@class='post_item_summary']/text()").extract()))
            item["digg_num"] = sel.xpath(
                ".//span[@class='diggnum']/text()").re(r'\d+')[0]
            # print(item)
            yield item

        # # 抓取下一页
        next_url = response.xpath(
            ".//a[text()='Next >']/@href").extract_first()
        if next_url is not None:
            next_url = "http://www.cnblogs.com" + next_url
            yield scrapy.Request(next_url, callback=self.parse)

        logging.info('{fix}[{url}执行完成]{fix}'.format(fix='*' * 50,
                                                    url=response.request.url))
