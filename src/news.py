import jinja2
import requests
from bs4 import BeautifulSoup
from user_agents import random_user_agent
from flask import Flask, request, redirect, url_for, render_template, flash, session, get_flashed_messages
import os

path = os.path.dirname(os.path.realpath(__file__))

def sohu_news():
    print("sohu news")
    url = 'http://www.sohu.com'

    headers = {'User-Agent': random_user_agent()}
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(r.text, 'lxml')
    '''
        <div class="news" data-spm="top-news1">
    '''
    # top-news1 top-news2 top-news3 top-news4 top-news5
    result = {}
    divs = soup.select('[data-spm="top-news1"] p a')
    print(len(divs))
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sohu"
        yield result

    divs = soup.select('[data-spm="top-news2"] li a')
    print(len(divs))
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sohu"
        # print(a.text.strip())
        # print(a['href'])
        yield result

    divs = soup.select('[data-spm="top-news3"] li a')
    print(len(divs))
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sohu"
        # print(a.text.strip())
        # print(a['href'])
        yield result

    divs = soup.select('[data-spm="top-news4"] li a')
    print(len(divs))
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sohu"
        # print(a.text.strip())
        # print(a['href'])
        yield result


def sina_news():
    print("sina news")
    url = 'https://news.sina.com.cn/'
    # <ul class="list_14" data-sudaclick="blk_news_3">
    headers = {'User-Agent': random_user_agent()}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    divs = soup.select('.ct_t_01 p a')
    print(len(divs))
    result = {}
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sina"
        yield result

    # <ul class="list_14" data-sudaclick="blk_news_1">
    divs = soup.select('[data-sudaclick="blk_news_1"] li a')
    print(len(divs))
    result = {}
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sina"
        yield result

    divs = soup.select('[data-sudaclick="blk_news_2"] li a')
    print(len(divs))
    result = {}
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sina"
        yield result

    divs = soup.select('[data-sudaclick="blk_news_3"] li a')
    print(len(divs))
    result = {}
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sina"
        yield result

    divs = soup.select('[data-sudaclick="blk_news_4"] li a')
    print(len(divs))
    result = {}
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sina"
        yield result

def sina_news_s():
    url = 'https://news.sina.com.cn/'
    # <ul class="list_14" data-sudaclick="blk_news_3">
    headers = {'User-Agent': random_user_agent()}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    divs = soup.select('[data-sudaclick="blk_news_1"] li a')
    # print(len(divs))
    result = {}
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sina"
        yield result

def sohu_news_s():
    url = 'https://news.sina.com.cn/'
    # <ul class="list_14" data-sudaclick="blk_news_3">
    headers = {'User-Agent': random_user_agent()}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    divs = soup.select('[data-spm="top-news2"] li a')
    # print(len(divs))
    for a in divs:
        result['title'] = a.text.strip()
        result['url'] = a['href']
        result['name'] = "sohu"
        # print(a.text.strip())
        # print(a['href'])
        yield result


def render_without_request(template_name, **context):
    # path1 = path + "/../templates"

    file_loader = jinja2.FileSystemLoader(path + "/../templates")
    env = jinja2.Environment(
        loader=file_loader,
        autoescape=jinja2.select_autoescape(['html', 'xml'])
    )

    template = env.get_template(template_name)
    return template.render(**context)

def merge_data():
    for item in sina_news():
        yield item
    for item in sohu_news():
        yield item

def save_to_html():
    content = merge_data()
    html = render_without_request('news.html', content=content)
    # print(html)
    with open(path + "/../templates/news_out_all.html", 'w') as file:
        file.write(html)

    # content = sina_news_s()
    # html = render_without_request('news_s.html', content=content)
    # # print(html)
    # with open(path + "/../templates/news_out_s.html", 'w') as file:
    #     file.write(html)

if __name__ == '__main__':
    save_to_html()
