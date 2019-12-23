#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/23 12:02 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : novel_spider.py


from scrapy import cmdline

cmdline.execute('scrapy crawl novel'.split())
