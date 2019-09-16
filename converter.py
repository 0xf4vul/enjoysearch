# -*- coding: utf-8 -*-

import os

#from mercury_parser import ParserAPI
#from html2text import html2text
import html2text
import requests
# from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time
import urllib.request, urllib.parse, urllib.error
from user_agents import random_user_agent
from urllib.parse import urljoin


def get_urls(baseurl):
    headers = {'User-Agent':random_user_agent()}
    session = HTMLSession()
    r = session.get(baseurl, headers=headers)

    all_urls = set()
    for link in r.html.absolute_links:
        all_urls.add(link)

    return "\n".join(all_urls)

def html_to_md(url, param):
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap["phantomjs.page.settings.userAgent"] = (random_user_agent())
    # driver = webdriver.PhantomJS(desired_capabilities=dcap)
    # driver = webdriver.PhantomJS(executable_path=executable_path)
    # obj = webdriver.PhantomJS(executable_path='C:\Python27\Scripts\phantomjs.exe',desired_capabilities=dcap)

    # driver.get(url)
    # driver.implicitly_wait(5)
    # html = driver.page_source
    # driver.close()
    # driver.quit()

    headers = {'User-Agent':random_user_agent()}
    session = HTMLSession()

    r = session.get(url, headers=headers)
    # print(r.encoding)
    # print(r.apparent_encoding)
    # r.encoding = 'utf-8'
    r.encoding = r.apparent_encoding
    html = r.text
    md = html2text.html2text(html)

    return md

    # print(param)
    # if param:
    #     li = param.split(" ")
    #     soup = BeautifulSoup(html, 'lxml')
    #     if len(li) > 1:
    #         name = li[0]
    #         lili = li[1].split("=")
    #         if len(lili) > 1:
    #             attrs1 = lili[0]
    #             attrs2 = lili[1].strip("\"")
    #             select_html = soup.find(name, attrs={attrs1, attrs2})
    #             md = html2text.html2text(str(select_html))
    #             return md
    #     else:
    #         name = param
    #         select_html = soup.find(name)
    #         md = html2text.html2text(str(select_html))
    #         return md
    #
    # md = html2text.html2text(html)
    # return md



if __name__ == '__main__':
    print(html_to_md('https://www.readmorejoy.com/'))
