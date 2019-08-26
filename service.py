# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template, flash, session, get_flashed_messages
from converter import html_to_md, get_urls
from searcher import baidu_search, bing_search, duckduckgo_search, google_search, sm1234_search
import logging

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
