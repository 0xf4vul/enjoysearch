#!/usr/bin/env python3

import os

#from mercury_parser import ParserAPI
#from html2text import html2text
import html2text
import requests
from bs4 import BeautifulSoup
import pprint
import urllib.request, urllib.parse, urllib.error
from magic_google import MagicGoogle

def abc():
    print("abc")


def google_search(key, pn):
    print("google_search start...")
    kv = {'q':key, 'start':pn}

    # mg = MagicGoogle(PROXIES)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    }
    r = requests.get("https://www.google.com/search", params=kv, headers=headers)
    print(r.url)
    soup = BeautifulSoup(r.text, 'lxml')

    pq_content = self.pq_html(content)
    li = []
    for item in pq_content('div.g').items():
        result = {}
        result['title'] = item('h3.r>a').eq(0).text()
        href = item('h3.r>a').eq(0).attr('href')
        if href:
            url = self.filter_link(href)
            result['url'] = url
        text = item('span.st').text()
        result['text'] = text
        yield result
        li.append(result)


if __name__ == '__main__':
    google_search("软件测试", 1)
