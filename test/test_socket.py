#!/usr/bin/env python3

from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from socket import *
import threading
import json
from time import sleep, ctime

async_mode = None

app = Flask(__name__)
app.debug = False
app.threaded = True
app.config['SECRET_KEY'] = '1secret!'

thread = None
thread_lock = Lock()

count = 0
tcpdict = {}

filename = 'car.json'


def read_json():
    with open(filename) as pf:
        numbers = json.load(pf)
        print(numbers)
        return numbers


socketio = SocketIO(app) #, async_mode=async_mode)


def background_thread():
    count = 0
    print("background_thread")
    while True:
        socketio.sleep(2)
        data = read_json()
        socketio.emit('server_response', data,
                      namespace='/test')


@app.route('/')
def index():
    print("_index_")
    # return "hello flask test"
    return render_template('main.html') #, async_mode=socketio.async_mode)


@socketio.on('connect', namespace='/test')
def test_connect():
    print("_connect_")
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


def main():
    socketio.run(app)


if __name__ == '__main__':
    main()
