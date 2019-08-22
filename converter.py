# -*- coding: utf-8 -*-

import os

#from mercury_parser import ParserAPI
#from html2text import html2text
import html2text
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
# from phantomjs_bin import executable_path
import time
import pprint
import urllib.request, urllib.parse, urllib.error
from user_agents import random_user_agent
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

def html_to_md(url, param):
    driver = webdriver.PhantomJS()
    # driver = webdriver.PhantomJS(executable_path=executable_path)

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
