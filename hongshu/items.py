# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HongshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    msg = scrapy.Field()
    other = scrapy.Field()
    chptitle = scrapy.Field()
    content = scrapy.Field()
    subclassname = scrapy.Field()
    nextjuanid = scrapy.Field()
    nextcid = scrapy.Field()
    prevjuanid = scrapy.Field()
    prevcid = scrapy.Field()
    needbuy = scrapy.Field()
    needlogin = scrapy.Field()
    chpprice = scrapy.Field()
    bookprice = scrapy.Field()
    charnum = scrapy.Field()
    publishtime = scrapy.Field()
    viplevel = scrapy.Field()
    money = scrapy.Field()
    egold = scrapy.Field()
    consumefail = scrapy.Field()
    curpos = scrapy.Field()
    sexflag = scrapy.Field()
    catename = scrapy.Field()
    bid = scrapy.Field()
    classname = scrapy.Field()
    author = scrapy.Field()
    authorid = scrapy.Field()
    viplevelname = scrapy.Field()
    username = scrapy.Field()
    vipchpcount = scrapy.Field()
    freechpcount = scrapy.Field()
    barcode = scrapy.Field()
    shouquaninfo = scrapy.Field()
    lzinfo = scrapy.Field()
    author_memo = scrapy.Field()
    isxiajia = scrapy.Field()
