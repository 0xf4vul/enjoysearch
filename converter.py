# -*- coding: utf-8 -*-

import os

#from mercury_parser import ParserAPI
#from html2text import html2text
import html2text
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from phantomjs_bin import executable_path
import time
import urllib.request, urllib.parse, urllib.error
from user_agents import random_user_agent
from urllib.parse import urljoin

#from MagicGoogle import MagicGoogle

#mercury = ParserAPI(api_key=os.environ['MERCURY_API_KEY'])

# def convert(html, title=None):
#     if title:
#         title = '# {}'.format(title)
#         html = '\n\n'.join([title, html])
#
#     return html2text(html)
#
# def meh(url):
#     try:
#         d = mercury.parse(url)
#         return convert(d.content, title=d.title)
#     except KeyError:
#         return None
def get_urls(baseurl):
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap["phantomjs.page.settings.userAgent"] = (random_user_agent())
    # driver = webdriver.PhantomJS(desired_capabilities=dcap)
    #
    # driver.get(baseurl)
    # driver.implicitly_wait(5)
    # html = driver.page_source
    # # driver.close()
    # driver.quit()
    #
    # soup = BeautifulSoup(html, 'lxml')

    headers = {'User-Agent':random_user_agent()}
    r = requests.get(baseurl, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    all_text = soup.find_all("a")
    all_urls = set()

    for item in all_text:
        a = (item.get('href'))
        if a.startswith("/"):
            a = urljoin(baseurl, a)

        all_urls.add(a)

    str = "\n".join(all_urls)
    # print(str)
    return str

def html_to_md(url, param):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (random_user_agent())
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    # driver = webdriver.PhantomJS(executable_path=executable_path)
    # obj = webdriver.PhantomJS(executable_path='C:\Python27\Scripts\phantomjs.exe',desired_capabilities=dcap)

    driver.get(url)
    driver.implicitly_wait(5)
    html = driver.page_source
    # driver.close()
    driver.quit()

    print(param)
    if param:
        li = param.split(" ")
        soup = BeautifulSoup(html, 'lxml')
        if len(li) > 1:
            name = li[0]
            lili = li[1].split("=")
            if len(lili) > 1:
                attrs1 = lili[0]
                attrs2 = lili[1].strip("\"")
                select_html = soup.find(name, attrs={attrs1, attrs2})
                md = html2text.html2text(str(select_html))
                return md
        else:
            name = param
            select_html = soup.find(name)
            md = html2text.html2text(str(select_html))
            return md

    md = html2text.html2text(html)
    return md



if __name__ == '__main__':
    print(html_to_md('https://www.readmorejoy.com/'))
