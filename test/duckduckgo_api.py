from requests_html import HTMLSession
import urllib
import requests
import pprint
import json

def DockduckgoSearch(search):
# def query(query, useragent='python-duckduckgo '+str(__version__), safesearch=True, html=False, meanings=True, **kwargs):
    safesearch=True
    html=False
    meanings=True
    useragent='python-duckduckgo '
    safesearch = '1' if safesearch else '-1'
    html = '0' if html else '1'
    meanings = '0' if meanings else '1'
    params = {
        'q': search,
        'o': 'json',
        'kp': safesearch,
        'no_redirect': '1',
        'no_html': html,
        'd': meanings,
        }
    #params.update(kwargs)
    encparams = urllib.parse.urlencode(params)
    url = 'http://api.duckduckgo.com/?' + encparams

    #request = urllib2.Request(url, headers={'User-Agent': useragent})
    response = requests.get(url, headers={'User-Agent': useragent})
    #response = urllib2.urlopen(request)
    jsondata = json.loads(response.text)

    print(jsondata)
    for i in jsondata.get('RelatedTopics',[]):
        print(i.get("Result"))
        print(i.get('FirstURL'))
        print(i.get("Text"))
        print("---------------")
    #print(jsondata)



DockduckgoSearch("python")
