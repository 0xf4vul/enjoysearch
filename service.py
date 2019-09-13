# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template, flash, session, get_flashed_messages
from converter import html_to_md, get_urls
from searcher import baidu_search, bing_search, duckduckgo_search, google_search, sm1234_search
from fanyi import baidu_fanyi, jieba_cat, google_fanyi, youdao_fanyi
from dreams import dodreams, get_best_dreams
from todo import todo_save_to, todo_read_from
# import logging

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
    global start, current_engine
    # print(request.args)
    engine = request.args.get('engine')
    key = request.args.get('key')
    ip = request.remote_addr
    start = request.args.get('start')

    # print(engine, key, start)

    content = None
    page = {}
    if key:
        if engine == "baidu":
            content = baidu_search(key, start)
        elif engine == "google":
            content = google_search(key, start)
        elif engine == "bing":
            content = bing_search(key, start)
        elif engine == "duckduckgo":
            content = duckduckgo_search(key, start)
        elif engine == "sm1234":
            content = sm1234_search(key, start)
        else:
            print("engine is what?")

        if content:
            # return content, 200, {'Content-Type': 'text/html; charset=UTF-8'}
            # print("return " + "engine:" + engine + " key:" + key)
            return render_template('search.html', content=content, engine=engine, key=key, start=start)
        else:
            # print("EnjoySearch meet 404, Not Found, Please try again...")
            return 'EnjoySearch meet 404, Not Found, Please try again...', 404
    else:
        key = ""
        engine = ""
        start = 0
        # print("here is default search ")
        return render_template('search.html', engine=engine, key=key, start=start)

@app.route('/fanyi', methods=['GET', 'POST'])
def better_fanyi():
    # print("in fanyi")
    # print(request.method)
    q = request.values.get('input')
    orgtext = request.values.get('text')
    # type = request.values.get('type')
    which = request.values.get('which')
    # print(q)
    # print(which)
    if q:
        if which == "google":
            result = google_fanyi(type, q)
        elif which == "baidu":
            result = baidu_fanyi(type, q)
        elif which == "youdao":
            result = youdao_fanyi(type, q)
        elif which == "cat":
            result = jieba_cat(type, q)

        # if type != 'cat':
        #     result = baidu_fanyi(type, q)
        # else:
        #     result = jieba_cat(type, q)
        return render_template('fanyi.html', input=q, output=result, text=orgtext)
    else:
        # print("default page")
        return render_template('fanyi.html')

@app.route('/dream', methods=['GET', 'POST'])
def youdreams():
    d_user = request.values.get('user')
    d_title = request.values.get('title')
    d_input = request.values.get('input')
    result = None
    result = dodreams(title=d_title,user=d_user,content=d_input)
    # result = get_best_dreams()
    best_result = get_best_dreams()

    return render_template('dream.html', content=result, best=best_result)

@app.route('/todo', methods=['GET', 'POST'])
def dotodo():
    user = request.values.get('fuser')
    input = request.values.get('input')
    # 需要密码
    # print(user)
    # print(input)
    if user in ["jiangzx", "luckrill", "蒋志祥"]:
        if input:
            todo_save_to(user, input)

        result = todo_read_from(user)
        return render_template('todo.html', user=user, input=result)

    result = ""
    return render_template('todo.html', user=user, input=result)

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
