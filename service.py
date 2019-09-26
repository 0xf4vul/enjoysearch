# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template, flash, session, get_flashed_messages
from src.converter import html_to_md, html_to_md_light, get_urls
from src.searcher import bd_search, bing_search, ddk_search, gg_search, sm1234_search
from src.fanyi import bd_fanyi, jieba_cat, gg_fanyi, youdao_fanyi
from src.dreams import dodreams, get_best_dreams
from src.todo import todo_save_to, todo_read_from
from src.news import save_to_html
import time
# import logging
# import asyncio

app = Flask(__name__)
app.threaded = True
app.secret_key = "readmorejoy.com"

@app.route('/markdown')
def markdown():
    url = request.args.get('url')
    param = request.args.get('param')
    type = request.args.get('type')
    # print(url)
    # print(type)
    if url:
        if type == "url":
            content = get_urls(url)
            # asyncio.get_event_loop().run_until_complete(get_urls(url)）
        elif type == "light":
            content = html_to_md_light(url, param)
        else:
            content = html_to_md(url, param)

        if content:
            return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
        else:
            print("markdown 404 Not Found")
            return '404 Not Found', 404
    else:
        return render_template('markdown.html')

# with open("static/tellyou.txt") as fp:
#     tellyoutext = fp.read()

@app.route('/')
@app.route('/search')
def keysearch():
    global start, current_who
    # print(request.args)
    who = request.args.get('who')
    key = request.args.get('key')
    ip = request.remote_addr
    start = request.args.get('start')

    # print(who, key, start)

    content = None
    page = {}
    if key:
        if who == "bd":
            content = bd_search(key, start)
        elif who == "gg":
            content = gg_search(ip, key, start)
        elif who == "bing":
            content = bing_search(key, start)
        elif who == "ddk":
            content = ddk_search(key, start)
        elif who == "sm1234":
            content = sm1234_search(key, start)
        else:
            print("who is what?")

        if content:
            # return content, 200, {'Content-Type': 'text/html; charset=UTF-8'}
            # print("return " + "who:" + who + " key:" + key)
            # url = "https://www.google.com/search"
            # return render_template('search.html', content=content, who=who, key=key, start=start, url=url)
            return render_template('search.html', content=content, who=who, key=key, start=start)
        else:
            # print("EnjoySearch meet 404, Not Found, Please try again...")
            return 'EnjoySearch meet 404, Not Found, Please try again...', 404
    else:
        key = ""
        who = ""
        start = 0
        # print("here is default search ")
        return render_template('search.html', who=who, key=key, start=start)

@app.route('/fanyi', methods=['GET', 'POST'])
def better_fanyi():
    # print("in fanyi")
    # print(request.method)
    q = request.values.get('input')
    orgtext = request.values.get('text')
    which = request.values.get('which')
    dst = request.values.get('dst')
    # print(dst)
    if q:
        if which == "gg":
            # t1 = time.time()
            result = gg_fanyi(type, q, dst)
            # t2 = time.time()
            # print('took google ' + str(t2-t1) + 'second')
        elif which == "bd":
            # t1 = time.time()
            result = bd_fanyi(type, q, dst)
            # t2 = time.time()
            # print('took baidu ' + str(t2-t1) + 'second')
        elif which == "youdao":
            # t1 = time.time()
            result = youdao_fanyi(type, q, dst)
            # t2 = time.time()
            # print('took youdao ' + str(t2-t1) + 'second')
        elif which == "cat":
            result = jieba_cat(type, q)

        # if type != 'cat':
        #     result = bd_fanyi(type, q)
        # else:
        #     result = jieba_cat(type, q)
        return render_template('fanyi.html', input=q, output=result, text=orgtext, which=which, dst=dst)
    else:
        # print("default page")
        return render_template('fanyi.html')

@app.route('/dream', methods=['GET', 'POST'])
def youdreams():
    d_user = request.values.get('user')
    d_title = request.values.get('title')
    d_input = request.values.get('input')
    # print(request.remote_addr)
    result = None
    result = dodreams(title=d_title,user=d_user,content=d_input)
    # result = get_best_dreams()
    best_result = get_best_dreams()

    return render_template('dream.html', content=result, best=best_result)

@app.route('/todo', methods=['GET', 'POST'])
def dotodo():
    user = request.values.get('fuser')
    what = request.values.get('fwhat')
    password = request.values.get('fpassword')
    # 需要密码

    print(user, what, password)
    print("-----------")
    if user in ["jiangzx", "luckrill", "蒋志祥"]:
        if input:
            todo_save_to(user, input)

        result = todo_read_from(user)
        return render_template('todo.html', user=user, input=result)

    result = ""
    return render_template('todo.html', user=user, input=result)

@app.route('/news')
def news():
    # flash("bling bling")
    # return app.send_static_file('news_out_all.html')
    return render_template('news_out_all.html')



@app.route('/test')
def yessir():
    # flash("bling bling")
    return render_template('yessir.html')


@app.route('/postdata', methods=['POST'])
def post_javascript_data():
    jsdata = request.form['data']
    # unique_id = create_csv(jsdata)
    # params = { 'uuid' : unique_id }
    print("post_javascript_data()")
    print(jsdata)
    # logger.info(jsdata)
    # logger.debug(jsdata)
    # print(jsdata)
    return (jsdata)


@app.route("/addflash")
def addFlash():
    # flash("bling bling")
    return "added a flash"


@app.route("/getflash/")
def getFlash():
    msgs = get_flashed_messages()
    msgStr = ""
    for msg in msgs:
        msgStr += msg + ","
    return msgStr


@app.route('/main.html')
def hello():
    print("main.html url right")
    return render_template('main.html')


if __name__ == '__main__':

    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
