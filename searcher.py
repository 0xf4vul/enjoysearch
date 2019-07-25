# -*- coding: utf-8 -*-

import os

#from mercury_parser import ParserAPI
#from html2text import html2text
import html2text
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pprint
import urllib.request, urllib.parse, urllib.error


def baidu_search(key, pn):
    print("baidu_search start...")
    kv = {'wd':key, 'pn':pn}
    print(kv)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    }
    r = requests.get("http://www.baidu.com/s", params=kv, headers=headers)
    print(r.url)
    soup = BeautifulSoup(r.text, 'lxml')
    # select_html = soup.find("div", attrs={'id':'content_left'})
    li = []
    now = int(pn)
    for item in soup.find_all('div', attrs={"class":"c-container"}):
        #print("search c-container")
        if item.has_attr('id') and item['id'] == str(now):
            #print(type(now))
            now += 1
            result = {}
            result['title'] = item.h3.get_text()
            ss = ''
            for div in item.find_all('div'):
            	if div.has_attr('class') and (div['class'][0].find('abstract') != -1 or div['class'][0] == 'c-row'):
            		ss += div.get_text()
            result['text'] = ss
            if item.h3.a:
                #result['url'] = item.h3.a.get('href')
                result['url'] = item.h3.a['href']
                li.append(result)
            else:
                print("item.h3.a is None *******")
                print(item.h3)
            #print(result)
            #yield result

    return li

def bing_search(key, pn):
    print("bing_search start...")
    kv = {'q':key, 'first':pn}

    subscription_key = "35b243b7106244a5b4ade56b8fb4c093"
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    params = {"q": key, "textDecorations": True, "textFormat": "HTML",  "offset":pn}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    li = []
    for v in search_results["webPages"]["value"]:
        # print(v["name"])
        # print(v["url"])
        # print(v["snippet"])
        result = {}
        result['title'] = v["name"]
        result['url'] = v["url"]
        result['text'] = v["snippet"]
        #print(result['title'])
        li.append(result)

    return li

def google_search(key, pn):
    print("google_search start...")
    kv = {'q':key, 'start':pn}

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    }
    r = requests.get("https://www.google.com/search", params=kv, headers=headers)
    #print(r.url)
    soup = BeautifulSoup(r.text, 'lxml')

    li = []
    for item in soup.find_all('div', attrs={"class":"g"}):
        #print("bing search div g")
        a = item.find('a')
        result = {}
        result['title'] = a.text.strip()
        result['url'] = a["href"]
        stext = item.find("span", attrs={"class":"st"})
        if stext:
            result['text'] = stext.text

        li.append(result)

    return li

def duckduckgo_search(key, pn):
    pass

def save_md(md):

    timestr = time.strftime('%Y%m%d-%M', time.localtime(time.time()))  #转化为时间格式2018-12-11 12：20：20
    filename = ("md/text" + str(count).zfill(3)) + ".md"
    pass

if __name__ == '__main__':
    print(html_to_md('https://www.readmorejoy.com/'))
