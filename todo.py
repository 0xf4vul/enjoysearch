
import os
import requests
import time
import urllib.request, urllib.parse, urllib.error
from user_agents import random_user_agent
from urllib.parse import urljoin, quote
import hashlib
import urllib
import random
import jieba

# first is doc
def todo_work(user, content):
    # save to doc

    # read from doc

    # md to html
    pass

def todo_save_to(user, contnet):
    name = "todo/" + user
    with open(name, 'w') as file:
        print("save to file")
        file.write(contnet)


def todo_read_from(user):
    name = "todo/" + user
    with open(name) as file:
        print("read from file")
        return file.read()

def baidu_fanyi(type, q):
    appid = '20190613000307195' #你的appid
    secretKey = 'GiYXPZ27k7gHPTFFOzke' #你的密钥

    httpClient = None
    apiurl = '/api/trans/vip/translate'
    if type == "en":
        fromLang = 'en'
        toLang = 'zh'
    elif type == "zh":
        fromLang = 'zh'
        toLang = 'en'
    else:
        fromLang = 'en'
        toLang = 'zh'

    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    url = 'http://api.fanyi.baidu.com' + apiurl+'?appid='+appid+'&q='+quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    # print(url)
    # http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
    r = requests.get(url)
    js_text = r.json()
    # print(js_text)
    # print(text["day_time_2"]["text1"])
    # print(js_text["from"])
    result = ""
    for text in js_text["trans_result"]:
        result += text["dst"] + "\n"
        # result = text["dst"]
        # li.append(result)
    # result = js_text["trans_result"][0]["dst"]
    return result

def jieba_cat(type, q):
    # print("jieba_cat")
    seg_list = jieba.cut(q)
    result = ", ".join(seg_list)

    return result
