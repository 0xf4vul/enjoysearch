
# import os
# import requests
# import time
# import urllib.request, urllib.parse, urllib.error
# from user_agents import random_user_agent
# from urllib.parse import urljoin, quote
# import hashlib
# import urllib
# import random
# import jieba
import sqlite3
import time


# 数据库 if_you_dream
# ID，Star, Title, Text, User, Creat_time, Update_time, Remarks

# c.execute('''CREATE TABLE Dreams
#        (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
#        Title          TEXT     NOT NULL,
#        Content        TEXT     NOT NULL,
#        User           TEXT     NOT NULL,
#        Star           INT,
#        Creat_time     TEXT,
#        Update_time    TEXT,
#        Remarks        TEXT);''')


# conn.commit()
# conn.close()
def creat_db_table():
    conn = sqlite3.connect('readmorejoy.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE Dreams
           (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
           Title          TEXT     NOT NULL,
           Content        TEXT     NOT NULL,
           User           TEXT     NOT NULL,
           Star           INT,
           Creat_time     TEXT,
           Update_time    TEXT,
           Remarks        TEXT);''')
    # conn.commit()
    conn.close()

# creat_db_table()


# 格式化成2016-03-20 11:45:39形式


def dodreams(title, user, content):
    conn = sqlite3.connect('readmorejoy.db')
    c = conn.cursor()

    if title and content:
        print("title and content")
        title = "如果 " + title
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(now)
        if not user:
            user = "匿名"
        # c.execute("INSERT INTO Dreams (Title,Content,User,Star,Creat_time) \
        c.execute("INSERT INTO Dreams (Title,Content,User,Creat_time) \
              VALUES ('%s', '%s', '%s', '%s')" % (title, content, user, now));
        conn.commit()


    cursor = c.execute("SELECT ID, Title, Content, User from Dreams ORDER BY ID DESC LIMIT 20 ")
    for row in cursor:
        result = {}
        result['title'] = row[1]
        result['text'] = row[2]
        result['user'] = row[3]
        yield result
