# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogsItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()  # 发布作者
    author_link = scrapy.Field()  # 作者博客主页链接

    title = scrapy.Field()  # 标题
    link = scrapy.Field()  # 标题链接
    summary = scrapy.Field()  # 摘要
    post_date = scrapy.Field()  # 发布时间
    digg_num = scrapy.Field()  # 推荐数
    comment_num = scrapy.Field()  # 评论数
    view_num = scrapy.Field()  # 阅读数
    add_date = scrapy.Field()  # 抓取时间
