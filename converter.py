# -*- coding: utf-8 -*-

import os
#from mercury_parser import ParserAPI
#from html2text import html2text
import html2text
import requests
from bs4 import BeautifulSoup
# from requests_html import HTMLSession
import time
import urllib.request, urllib.parse, urllib.error
from user_agents import random_user_agent
from urllib.parse import urljoin
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import asyncio
# from pyppeteer import launch

# async def ppet(url):
#     browser = await launch({
#     # 'executablePath':'/Applications/Chromium.app/Contents/MacOS/Chromium',
#     'handleSIGINT':False,
#     'handleSIGTERM':False,
#     'handleSIGHUP':False,
#     })
#     # browser = await launch()
#     page = await browser.newPage()
#     await page.goto(url)
#     # await page.screenshot({'path': 'example.png'})
#     html = await page.content()
#     await browser.close()
#     return html
#
# def get_urls(baseurl):
#     new_loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(new_loop)
#     html = asyncio.get_event_loop().run_until_complete(ppet(baseurl))
#     return html

def get_urls(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text

    soup = BeautifulSoup(html, 'lxml')
    all_text = soup.find_all("a")
    all_urls = set()

    for item in all_text:
        a = (item.get('href'))
        if a.startswith("/"):
            a = urljoin(url, a)

        all_urls.add(a)

    str = "\n".join(all_urls)
    # print(str)
    return str

    # headers = {'User-Agent':random_user_agent()}
    # session = HTMLSession()
    # r = session.get(baseurl, headers=headers)
    #
    # all_urls = set()
    # for link in r.html.absolute_links:
    #     all_urls.add(link)
    #
    # return "\n".join(all_urls)

def html_to_md_light(url, param):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text

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

def html_to_md(url, param):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (random_user_agent())
    driver = webdriver.PhantomJS(desired_capabilities=dcap)

    driver.get(url)
    driver.implicitly_wait(5)
    html = driver.page_source
    # driver.close()
    driver.quit()

    # headers = {'User-Agent':random_user_agent()}
    # session = HTMLSession()

    # r = session.get(url, headers=headers)
    # print(r.encoding)
    # print(r.apparent_encoding)
    # r.encoding = 'utf-8'
    # r.encoding = r.apparent_encoding
    # r.html.render()
    # html = r.html
    # html = r.html
    # val = html.render()
    # r = session.get('http://www.readmorejoy.com/')
    # r.html.render()
    # md = html2text.html2text(r.text)
    #
    # return md

    # print(param)
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
