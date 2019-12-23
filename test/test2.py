#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/23 1:57 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : test2.py
import re

url = 'https://www.hongshu.com/content/67825/108963-11126498.html'
bid, jid, cid = re.findall('\/content\/(.*)\/(.*)-(.*).html', url)[0]

# r = url.split('/')
print(bid)
print(jid)
print(cid)
