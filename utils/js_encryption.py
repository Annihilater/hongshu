#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/23 1:28 下午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : js_encryption.py
import execjs

utf_to_changes = r"""
function utf8to16(str) {
    var out, i, len, c;
    var char2, char3;
    out = "";
    len = str.length;
    i = 0;
    while (i < len) {
        c = str.charCodeAt(i++);
        switch (c >> 4) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
        case 7:
            out += str.charAt(i - 1);
            break;
        case 12:
        case 13:
            char2 = str.charCodeAt(i++);
            out += String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F));
            break;
        case 14:
            char2 = str.charCodeAt(i++);
            char3 = str.charCodeAt(i++);
            out += String.fromCharCode(((c & 0x0F) << 12) | ((char2 & 0x3F) << 6) | ((char3 & 0x3F) << 0));
            break;
        }
    }
    return out;
}
"""

hs_decrypt = r"""
function hs_decrypt(str, key) {
    if (str == "") {
        return "";
    }
    var v = str2long(str, false);
    var k = str2long(key, false);
    var n = v.length - 1;
    var z = v[n - 1]
      , y = v[0]
      , delta = 0x9E3779B9;
    var mx, e, q = Math.floor(6 + 52 / (n + 1)), sum = q * delta & 0xffffffff;
    while (sum != 0) {
        e = sum >>> 2 & 3;
        for (var p = n; p > 0; p--) {
            z = v[p - 1];
            mx = (z >>> 5 ^ y << 2) + (y >>> 3 ^ z << 4) ^ (sum ^ y) + (k[p & 3 ^ e] ^ z);
            y = v[p] = v[p] - mx & 0xffffffff;
        }
        z = v[n];
        mx = (z >>> 5 ^ y << 2) + (y >>> 3 ^ z << 4) ^ (sum ^ y) + (k[p & 3 ^ e] ^ z);
        y = v[0] = v[0] - mx & 0xffffffff;
        sum = sum - delta & 0xffffffff;
    }
    return long2str(v, true);
};

function long2str(v, w) {
    var vl = v.length;
    var sl = v[vl - 1] & 0xffffffff;
    for (var i = 0; i < vl; i++) {
        v[i] = String.fromCharCode(v[i] & 0xff, v[i] >>> 8 & 0xff, v[i] >>> 16 & 0xff, v[i] >>> 24 & 0xff);
    }
    if (w) {
        return v.join('').substring(0, sl);
    } else {
        return v.join('');
    }
}
function str2long(s, w) {
    var len = s.length;
    var v = [];
    for (var i = 0; i < len; i += 4) {
        v[i >> 2] = s.charCodeAt(i) | s.charCodeAt(i + 1) << 8 | s.charCodeAt(i + 2) << 16 | s.charCodeAt(i + 3) << 24;
    }
    if (w) {
        v[v.length] = len;
    }
    return v;
}
"""

base64decode = r"""
    function base64decode(str) {
    var c1, c2, c3, c4, base64DecodeChars = new Array(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,62,-1,-1,-1,63,52,53,54,55,56,57,58,59,60,61,-1,-1,-1,-1,-1,-1,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,-1,-1,-1,-1,-1,-1,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,-1,-1,-1,-1,-1);
    var i, len, out;
    len = str.length;
    i = 0;
    out = "";
    while (i < len) {
        do {
            c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
        } while (i < len && c1 == -1);if (c1 == -1)
            break;
        do {
            c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
        } while (i < len && c2 == -1);if (c2 == -1)
            break;
        out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));
        do {
            c3 = str.charCodeAt(i++) & 0xff;
            if (c3 == 61)
                return out;
            c3 = base64DecodeChars[c3];
        } while (i < len && c3 == -1);if (c3 == -1)
            break;
        out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));
        do {
            c4 = str.charCodeAt(i++) & 0xff;
            if (c4 == 61)
                return out;
            c4 = base64DecodeChars[c4];
        } while (i < len && c4 == -1);if (c4 == -1)
            break;
        out += String.fromCharCode(((c3 & 0x03) << 6) | c4);
    }
    return out;
}
"""


def utf_encode(data):
    js_context = execjs.compile(utf_to_changes)
    ret3 = js_context.call('utf8to16', data)
    return ret3


def content_decrypt(data, key):
    js_context = execjs.compile(hs_decrypt)
    ret2 = js_context.call('hs_decrypt', data, key)
    return ret2


def base64_decode(data):
    js_context = execjs.compile(base64decode)
    ret = js_context.call('base64decode', data)
    return ret


def decrypt(key, content):
    return utf_encode(content_decrypt(base64_decode(content), key))


if __name__ == '__main__':
    key = "47541161"
    content = r"""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"""

    print(decrypt(key, content))
