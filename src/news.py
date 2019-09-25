from requests_html import HTMLSession
import html2text
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80  Safari/537.36 QIHU 360SE'
}

def test_rander():
    session = HTMLSession()
    # r = session.get('http://www.readmorejoy.com/')

    r = session.get('https://www.toutiao.com/a6739019577469960717/')
    r.html.render()
    sleep(3)
    # print(r.text)
    md = html2text.html2text(r.text)

    print(md)

def sohu_news():
    url = 'http://www.sohu.com'

    # session = HTMLSession()
    # r = session.get(url, headers=headers)
    r = requests.get(url, headers=headers)
    html = r.text
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    '''
        <div class="news" data-spm="top-news1">
    '''
    # top-news1 top-news2 top-news3 top-news4 top-news5
    divs = soup.select('[data-spm="top-news3"] li a')

    for a in divs:
        print(a.text.strip())
        print(a['href'])
    # for news in divs:
    #     # print(news)
    #     p = news.select('li a' )
    #     # t = p.select('a')
    #     for tt in p:
    #         # print(tt)
    #         print(tt.text)
    #         print(tt['href'])
            # print(t)
            # print(t.text)
            # print(t[href])
        # print(p)
        # t = p.select('a')
        # print(t.text)
        # print(t[href])
        # if len(news.select('p'))>0:
        #     p = news.select('p')
        #     for p1 in p:
        #         print(p1)
        #     a = news.select('a')
        #     for a1 in a:
        #         print(a1['href'])

        # print(n)

def sina_news():
    url = 'https://news.sina.com.cn/'
    r = requests.get(url, headers=headers)
    r.encoding='utf-8'
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    divs = soup.select('.ct_t_01 p a')
    print(divs)
    for a in divs:
        print(a.text.strip())
        print(a['href'])

sina_news()
sohu_news()
