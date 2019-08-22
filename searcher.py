# -*- coding: utf-8 -*-

import os

import html2text
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from user_agents import random_user_agent

def baidu_search(key, pn):
    print("baidu_search start...")
    kv = {'wd':key, 'pn':pn}
    print(kv)
    headers = {'User-Agent':random_user_agent()}
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    # }
    r = requests.get("http://www.baidu.com/s", params=kv, headers=headers)
    print(r.url)
    soup = BeautifulSoup(r.text, 'lxml')
    # select_html = soup.find("div", attrs={'id':'content_left'})
    li = []
    now = int(pn)
    for item in soup.find_all('div', attrs={"class":"c-container"}):
        #print("search c-container")
        now += 1
        if item.has_attr('id') and item['id'] == str(now):
            #print(type(now))
            result = {}
            result['title'] = item.h3.get_text()
            #print(item.h3)
            #print(item.h3.name) name is h3
            #print(item.h3.a.contents)
            #result['title'] = str(item.h3.a.contents).strip("[]")
            ss = ''
            for div in item.find_all('div'):
            	if div.has_attr('class') and (div['class'][0].find('abstract') != -1 or div['class'][0] == 'c-row'):
            		ss += div.get_text()
                    #ss += div.contents
            result['text'] = ss
            if item.h3.a:
                #result['url'] = item.h3.a.get('href')
                #print(item.h3.a.string)
                result['url'] = item.h3.a['href']
                li.append(result)
            else:
                print("item.h3.a is None ***")
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

    headers = {'User-Agent':random_user_agent()}
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    # }
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

def sm1234_search(key, pn):
    # print("sm1234_search start...")
    kv = {'q':key, 'p':pn}
    # print(kv)
    headers = {'User-Agent':random_user_agent()}
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    # }
    r = requests.get("http://sm.sm1234.net/", params=kv, headers=headers)
    # url = 'http://sm.sm1234.net/?q=python3&p=2'
    # print(r.url)
    soup = BeautifulSoup(r.text, 'lxml')

    li = []
    now = int(pn)
    for item in soup.find_all('div', attrs={"class":"g"}):
        # print(item)
        now += 1
        # if item.has_attr('id') and item['id'] == str(now):
        result = {}
        result['title'] = item.h2.get_text()
        result['url'] = "http://sm.sm1234.net" + item.h2.a['href']
        #http://sm.sm1234.net
        # print(result['url'])
        result['text'] = (item.find("div", attrs={"class":"std"})).get_text()

        li.append(result)

    return li

def duckduckgo_search(key, pn):
    # kv = {'wd':key, 'pn':pn}
    pn = int(pn) * 3
    # dc = pn - 1

    # kv = {'q':key, 's':pn, 'dc':pn, 'api':'/d.js'}
    if pn > 10:
        kv = {'q':key, 's':pn, 'dc':pn, 'v':'l', 'o':'json', 'api':'/d.js'}
    else:
        kv = {'q':key, 's':pn, 'dc':pn}
    # print(kv)
    # print(random_user_agent())
    headers = {'User-Agent':random_user_agent()}
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    # }
    r = requests.post("https://www.duckduckgo.com/html", params=kv, headers=headers)
    # print(r.url)
    # print(r.status_code)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')

    li = []
    # <div class="result results_links results_links_deep web-result ">
    # On server, need use follow string.
    # <div class="links_main links_deep result__body">
    for item in soup.find_all('div', attrs={"class":"links_main links_deep result__body"}):
        result = {}
        result['title'] = item.h2.get_text()
        result['url'] = item.h2.a['href']
        result['text'] = (item.find("a", attrs={"class":"result__snippet"})).get_text()

        li.append(result)

    return li

# def which_search(key, pn):
#     pass
