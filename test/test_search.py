import os

import html2text
import requests
from bs4 import BeautifulSoup
import time
import pprint
import urllib.request, urllib.parse, urllib.error
from requests_html import HTMLSession

session = HTMLSession()

dirver = None

def do_search(key, pn):
    global driver
    print("sm1234_search start...")
    kv = {'q':"软件测试", 'first':36}

    print(kv)

    # url = "https://cn.bing.com/search?q=软件测试"
    # #url = "https://cn.bing.com/search?q=inurl%3aphp%3fid%3d&qs=HS&sc=8-0&cvid=2EEF822D8FE54B6CAAA1CE0169CA5BC5&sp=1&first=53&FORM=PERE3"
    # #url = "https://cn.bing.com/search?q=debian+10&PC=U316&FORM=CHROMN"
    # #url = "https://cn.bing.com/search?q=debian+10&PC=U316&FORM=BESBTB&ensearch=1"

    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    # }
    # r = requests.get("https://www.bing.com/search", params=kv, headers=headers)
    # print(r.url)

    url = 'http://sm.sm1234.net/?q=python3&p=2'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    r = requests.get(url, headers=headers)
    html = r.text
    # url1 = "https://cn.bing.com/search?q=dev&qs=n&form=QBRE&sp=-1&pq=dev&sc=8-3&sk=&cvid=83A65B35BD374BA6A9E7909A9E1CCF05"
    # url3 = "https://cn.bing.com/search?q=dev&qs=n&sp=-1&pq=dev&sc=8-3&sk=&cvid=83A65B35BD374BA6A9E7909A9E1CCF05&first=31&FORM=PERE2"
    # r = session.get(url3)
    # r.html.render()
    # print(r.url)

    soup = BeautifulSoup(html, 'lxml')

    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    # }
    # #baseurl = "https://cn.bing.com/search?q=软件测试&first=1"
    # #r = requests.get(baseurl, headers=headers)
    # cookies = dict(cookies_are='working')
    # r = requests.get("https://www.bing.com/search", params=kv, headers=headers, cookies=cookies)
    # #print(r.text)
    #
    # print(r.url)
    # print(r.status_code)
    # soup = BeautifulSoup(r.text, 'lxml')
    # select_html = soup.find("div", attrs={'id':'content_left'})
    #li = []
    for item in soup.find_all("div", attrs={"class":"g"}):
        print("sm1234 search b_alog")
        result = {}
        result['title'] = item.h2.get_text()
        result['url'] = item.h2.a['href']
        result['text'] = (item.find("div", attrs={"class":"std"})).get_text()
        print(result['title'])
        print(result['text'])
        #li.append(result)

        #yield result

    #return li
do_search("dev", 16)
