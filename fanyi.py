
import os
import requests
import time
import urllib.request, urllib.parse, urllib.error
from user_agents import random_user_agent
from urllib.parse import urljoin, quote
from user_agents import random_user_agent
import hashlib
import urllib
import random
import jieba
import execjs
from langdetect import detect

def gg_fanyi(type, q, dst):
    print("gg_fanyi")

    ctx = execjs.compile("""
    function TL(a) {
    var k = "";
    var b = 406644;
    var b1 = 3293161072;

    var jd = ".";
    var $b = "+-a^+6";
    var Zb = "+-3^+b+-f";

    for (var e = [], f = 0, g = 0; g < a.length; g++) {
        var m = a.charCodeAt(g);
        128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
        e[f++] = m >> 18 | 240,
        e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
        e[f++] = m >> 6 & 63 | 128),
        e[f++] = m & 63 | 128)
    }
    a = b;
    for (f = 0; f < e.length; f++) a += e[f],
    a = RL(a, $b);
    a = RL(a, Zb);
    a ^= b1 || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1E6;
    return a.toString() + jd + (a ^ b)
};

function RL(a, b) {
    var t = "a";
    var Yb = "+";
    for (var c = 0; c < b.length - 2; c += 3) {
        var d = b.charAt(c + 2),
        d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
        d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
        a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
    }
    return a
}
""")
    # t1 = time.time()
    tk = ctx.call("TL", q)
    # t2 = time.time()
    # print('took tk ' + str(t2-t1) + ' second')
    # print(tk)
    # print(q)
    headers = {'User-Agent':random_user_agent()}
    # print(q)
    type = detect(q[:30]) #"en | zh_cn"
    print("detect(q) = " + type)
    # if type == 'ko':
    #     type = "zh-cn"

    if type == "en":
        # print("gg dedect type en")
        if dst == "cn":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=zh-cn&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "en":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "fra":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=fr&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        else:
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=zh-cn&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        # url = "http://translate.google.cn/translate_a/single?client=t" \
        #       "&sl=en&tl=zh-cn&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
        #       "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
        #       "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
    elif type == 'zh-cn':
        # print("google dedect type zh-cn")
        if dst == "cn":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-cn&tl=zh-cn&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "en":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-cn&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "fra":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-cn&tl=fr&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        else:
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-cn&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
    elif type == 'zh-tw':
        # print("google dedect type zh-cn")
        if dst == "cn":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-tw&tl=zh-cn&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "en":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-tw&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "fra":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-tw&tl=fr&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        else:
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=zh-tw&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
    else:
        # print("google dedect type else")
        if dst == "cn":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=zh-cn&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "en":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        elif dst == "fra":
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=fr&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)
        else:
            url = "http://translate.google.cn/translate_a/single?client=t" \
                  "&sl=en&tl=zh-cn&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                  "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                  "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, q)

    t1 = time.time()
    r = requests.get(url, headers=headers)
    t2 = time.time()
    print('took get ' + str(t2-t1) + ' second')
    # print(r.encoding)
    # r.encoding = 'UTF-8'
    # print(r.text)

    data = r.json()
    # print(data)
    # data = "122"

    result = ''
    for dt in data[0]:
        if dt[0]:
            result += dt[0]

    return result

def youdao_fanyi(type, q, dst):
    print("youdao_fanyi")
    # q = "你好"
    # q = "hello"
    headers = {'User-Agent':random_user_agent()}
    # type = detect(q[:30]) #"en | zh_cn"
    # print("detect(q) = " + type)
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link'
    # if dst == "cn":
    #     print("youdao cn")
    #     # if type in ['zh'] 'zh-CHS'
    #     data = {'from': type, 'to': 'zh-cn', 'smartresult': 'dict', 'client': 'fanyideskweb', 'salt': '1500092479607',
    #             'sign': 'c98235a85b213d482b8e65f6b1065e26', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
    #             'action': 'FY_BY_CL1CKBUTTON', 'typoResult': 'true', 'i': q}
    # elif dst == "en":
    #     print("youdao en")
    #     data = {'from': type, 'to': 'en', 'smartresult': 'dict', 'client': 'fanyideskweb', 'salt': '1500092479607',
    #             'sign': 'c98235a85b213d482b8e65f6b1065e26', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
    #             'action': 'FY_BY_CL1CKBUTTON', 'typoResult': 'true', 'i': q}
    # elif dst == "fra":
    #     print("youdao fra")
    #     data = {'from': 'zh-tw', 'to': 'zh-CHS', 'smartresult': 'dict', 'client': 'fanyideskweb', 'salt': '1500092479607',
    #             'sign': 'c98235a85b213d482b8e65f6b1065e26', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
    #             'action': 'FY_BY_CL1CKBUTTON', 'typoResult': 'true', 'i': q}
    # else:
    #     print("youdao else")
    data = {'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb', 'salt': '1500092479607',
            'sign': 'c98235a85b213d482b8e65f6b1065e26', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CL1CKBUTTON', 'typoResult': 'true', 'i': q}

    # print(q)
    r = requests.get(url, params=data, headers=headers)
    ta = r.json()
    result = ""
    for ii in ta['translateResult']:
        for i in ii:
            result += i['tgt']
        result += "\n"

    return result

def xunfei_fanyi(type, q):
    pass


def bd_fanyi(type, q, dst):
    print("bd_fanyi")
    appid = '20190613000307195' #你的appid
    secretKey = 'GiYXPZ27k7gHPTFFOzke' #你的密钥

    # httpClient = None
    apiurl = '/api/trans/vip/translate'
    # if type == "en":
    #     fromLang = 'en'
    #     toLang = 'zh'
    # elif type == "zh":
    #     fromLang = 'zh'
    #     toLang = 'en'
    # else:
    #     fromLang = 'en'
    #     toLang = 'zh'

    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding='utf-8'))
    sign = m1.hexdigest()
    # print(dst)
    type = detect(q[:30]) #"en | zh_cn"
    print("detect(q) = " + type)
    if dst == "cn":
        # print("dst cn")
        if type == "zh-tw":
            url = 'http://api.fanyi.baidu.com' + apiurl+'?appid='+appid+'&q='+quote(q)+'&from='+'cht'+'&to='+'zh'+'&salt='+str(salt)+'&sign='+sign
        else:
            url = 'http://api.fanyi.baidu.com' + apiurl+'?appid='+appid+'&q='+quote(q)+'&from='+'auto'+'&to='+'zh'+'&salt='+str(salt)+'&sign='+sign
    elif dst == "en":
        # print("dst en")
        url = 'http://api.fanyi.baidu.com' + apiurl+'?appid='+appid+'&q='+quote(q)+'&from='+'auto'+'&to='+'en'+'&salt='+str(salt)+'&sign='+sign
    elif dst == "fra":
        # print("dst fr")
        url = 'http://api.fanyi.baidu.com' + apiurl+'?appid='+appid+'&q='+quote(q)+'&from='+'auto'+'&to='+'fra'+'&salt='+str(salt)+'&sign='+sign
    else:
        # print("......")
        url = 'http://api.fanyi.baidu.com' + apiurl+'?appid='+appid+'&q='+quote(q)+'&from='+'auto'+'&to='+'auto'+'&salt='+str(salt)+'&sign='+sign
    # print(url)
    # http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
    r = requests.get(url)
    js_text = r.json()
    result = ""
    for item in js_text["trans_result"]:
        result += "\n" + item["dst"]

    return result

def jieba_cat(type, q):
    # print("jieba_cat")
    seg_list = jieba.cut(q)
    result = " ".join(seg_list)

    return result
