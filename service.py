# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, render_template, flash, session, get_flashed_messages
from converter import html_to_md
from searcher import baidu_search, bing_search, google_search
import logging
import subprocess
#from spider import Spider
#from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = "readmorejoy"
#socketio = SocketIO(app)

# @socketio.on('my event')
# def test_message(message):
#     emit('my response', {'data': 'got it!'})
#
# @socketio.on('my event', namespace='/test')
# def test_message(message):
#     emit('my response', {'data': message['data']})
#
# @socketio.on('my broadcast event', namespace='/test')
# def test_message(message):
#     emit('my response', {'data': message['data']}, broadcast=True)
#
# @socketio.on('connect', namespace='/test')
# def test_connect():
#     emit('my response', {'data': 'Connected'})
#
# @socketio.on('disconnect', namespace='/test')
# def test_disconnect():
#     print('Client disconnected')

@app.route('/markdown')
def markdown():
    url = request.args.get('url')
    param = request.args.get('param')
    print(url)
    if url:
        content = html_to_md(url, param)
        if content:
            return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
        else:
            print("markdown 404 Not Found")
            return '404 Not Found', 404
    else:
        return render_template('markdown.html')


@app.route('/crawler')
def crawler():
    url = request.args.get('url')
    print(url)
    content =""
    if url:
        proc = subprocess.Popen(['./crawler.py', url])
        #out, err = proc.communicate()
        # while proc.poll() is None:
        #     print("working...")

        # for li in spider.crawl(url):
        #     content = spider.get_interLink()
        #     print("aaa")
        #     print(content)

        return render_template('crawler.html', content=content)
        # spider = Spider(url)
        # content = spider.crawl(url)
        # if content:
        #     return content, 200, {'Content-Type': 'text/x-markdown; charset=UTF-8'}
        # else:
        #     print("markdown 404 Not Found")
        #     return '404 Not Found', 404
    else:
        return render_template('crawler.html', content=content)



with open("static/tellyou.txt") as fp:
    tellyoutext = fp.read()


@app.route('/')
@app.route('/search')
def keysearch():
    global start, current_engine
    # print(request.args)
    engine = request.args.get('engine')
    key = request.args.get('key')
    ip = request.remote_addr
    start = request.args.get('start')
    # start = int(start)
    # print("request get:", engine, key, start)

    # if not engine:
    #     engine = "google"

    # if current_engine == engine:
    #     if engine == "baidu":
    #         #start += 10
    #     elif engine == "google":
    #         #start += 10
    #     elif engine == "bing":
    #         #start += 10
    # else:   # new engine type
    #     current_engine = engine
    #     start = 1
    print(engine, key, start)

    content = None
    page = {}
    if key:
        if engine == "baidu":
            content = baidu_search(key, start)
        elif engine == "google":
            content = google_search(key, start)
        elif engine == "bing":
            content = bing_search(key, start)
        else:
            print("engine is what?")

        if content:
            # return content, 200, {'Content-Type': 'text/html; charset=UTF-8'}
            # print("return " + "engine:" + engine + " key:" + key)
            return render_template('search.html', content=content, engine=engine, key=key, start=start, tellyou=tellyoutext)
        else:
            print("search 404 Not Found")
            return '404 Not Found', 404
    else:
        key = ""
        engine = ""
        start = 0
        print("default search ")

        return render_template('search.html', engine=engine, key=key, start=start, tellyou=tellyoutext)


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
    #socketio.run(app, host="0.0.0.0", port=5000)
