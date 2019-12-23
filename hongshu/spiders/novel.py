# -*- coding: utf-8 -*-
import json
import re

import scrapy

from hongshu.items import HongshuItem
from hongshu.settings import BOOK_URL, HEADERS
from utils.js_encryption import decrypt


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['www.hongshu.com']
    start_urls = ['https://www.hongshu.com/content/67825/108963-11126498.html']

    def start_requests(self):
        url = 'https://www.hongshu.com/content/67825/108963-11126498.html'
        bid, jid, cid = re.findall('\/content\/(.*)\/(.*)-(.*).html', url)[0]
        key_payload = f'method=getchptkey&bid={bid}&cid={cid}'
        yield scrapy.Request(url=BOOK_URL, method='POST', headers=HEADERS, body=key_payload, callback=self.get_key,
                             meta={'cid': cid, 'bid': bid, 'jid': jid})

    def get_key(self, response):
        bid = response.meta['bid']
        jid = response.meta['jid']
        cid = response.meta['cid']
        payload = f'method=getchpcontent&bid={bid}&jid={jid}&cid={cid}'
        data = json.loads(response.text)
        if data['msg'] == '获取章节内容成功':
            key = data['key']
            yield scrapy.Request(url=BOOK_URL, method='POST', headers=HEADERS, body=payload, callback=self.parse,
                                 meta={'key': key})
        else:
            self.logger.debug('Get Key Failed!!!')

    def parse(self, response):
        key = response.meta['key']
        data = json.loads(response.text)
        if data['msg'] == '获取章节内容成功':
            item = HongshuItem()
            for field in item.fields:
                try:
                    item[field] = data[field]
                except NameError():
                    self.logger.debug('Field is not Defined ' + field)
            item['content'] = decrypt(key, item['content'])  # js 解密章节内容
            yield item
        else:
            self.logger.debug('Get Chapter Failed!!!')
