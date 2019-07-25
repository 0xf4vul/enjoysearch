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
from requests_html import HTMLSession

session = HTMLSession()

dirver = None

def bing_search(key, pn):
    global driver
    print("bing_search start...")
    kv = {'q':"软件测试", 'first':36}

    print(kv)
    # if (pn == 1):
    #     driver = webdriver.PhantomJS()
    #     url = "https://cn.bing.com"
    #     driver.get(url)
    #     driver.implicitly_wait(5)
    #     driver.find_element_by_id("sb_form_q").clear()
    #     driver.find_element_by_id("sb_form_q").send_keys(key)
    #     driver.find_element_by_id("sb_form_go").submit()
    #     #time.sleep(3)
    #     #print(driver.page_source)
    #     print(driver.find_element_by_class_name("b_msg").text)
    #     print(driver.find_element_by_class_name("b_widePag sb_bp").text)
    #     #driver.find_element_by_class_name('sw_next').click()
    # else:
    #     print("bing sw_next")
    #     #print(driver.page_source)
    #     print(driver.find_element_by_class_name("b_msg").text)
    #     print(driver.find_element_by_class_name("sw_next").text)
    #     print(driver.find_element_by_class_name("sb_pagN sb_pagN_bp b_widePag sb_bp").text)
    #     #driver.find_element_by_class_name('sw_next').click()
    #
    # driver.implicitly_wait(8)
    # print(driver.find_element_by_class_name("b_msg").text)
    # print(driver.find_element_by_class_name("sw_next").text)

    # url = "https://cn.bing.com/search?q=软件测试"
    # #url = "https://cn.bing.com/search?q=inurl%3aphp%3fid%3d&qs=HS&sc=8-0&cvid=2EEF822D8FE54B6CAAA1CE0169CA5BC5&sp=1&first=53&FORM=PERE3"
    # #url = "https://cn.bing.com/search?q=debian+10&PC=U316&FORM=CHROMN"
    # #url = "https://cn.bing.com/search?q=debian+10&PC=U316&FORM=BESBTB&ensearch=1"
    # #driver = webdriver.PhantomJS()
    # driver = webdriver.Chrome()
    # #driver.maximize_window()
    # driver.get(url)
    # driver.implicitly_wait(5)
    # html = driver.page_source
    # print(html)
    # time.sleep(5)
    # driver.close()
    #driver.quit()
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
    # }
    # r = requests.get("https://www.bing.com/search", params=kv, headers=headers)
    # print(r.url)

    # url = 'https://cn.bing.com/search?q='+word+'&qs=bs&ajf=60&first=31&Accept-Language=en-us'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    #r = requests.get(url, headers=headers)
    url1 = "https://cn.bing.com/search?q=dev&qs=n&form=QBRE&sp=-1&pq=dev&sc=8-3&sk=&cvid=83A65B35BD374BA6A9E7909A9E1CCF05"
    url3 = "https://cn.bing.com/search?q=dev&qs=n&sp=-1&pq=dev&sc=8-3&sk=&cvid=83A65B35BD374BA6A9E7909A9E1CCF05&first=31&FORM=PERE2"
    r = session.get(url3)
    r.html.render()
    print(r.url)
    html = r.text
    #driver.close()



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
    for item in soup.find_all("li", attrs={"class":"b_algo"}):
        print("bing search b_alog")
        result = {}
        result['title'] = item.h2.get_text()
        result['url'] = item.h2.a['href']
        result['text'] = (item.find("div", attrs={"class":"b_caption"})).get_text()
        print(result['title'])
        #li.append(result)

        #yield result

    #return li
#bing_search("dev", 16)

def do_script():
    url = "https://segmentfault.com/a/1190000015641160"
    r = session.get(url)
    #print(r.html.text)
    #print(r.html.text.markdown)
    #r.html.render()
    md = html2text.html2text(r.html.html)
    print(md)


do_script()

#bing_search("dev", 6)
