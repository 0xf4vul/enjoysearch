
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

import argparse

dbname = "readmorejoy.db"
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
def creat_todo_db_table():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE Todo
           (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
           Content        TEXT     NOT NULL,
           User           TEXT     NOT NULL,
           Password       TEXT     NOT NULL,
           Ver            INT,
           Creat_time     TEXT,
           Update_time    TEXT,
           Remarks        TEXT);''')

    conn.commit()
    conn.close()


def creat_db_table():
    conn = sqlite3.connect(dbname)
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

    title = "如果 我是蒋志祥"
    content = "努力探索给人类真正做点好事\r\n\r\n积极向大家学习\r\n\r\n积极和大家交流，感谢理解"
    user = "蒋志祥"
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    c.execute("INSERT INTO Dreams (Title,Content,User,Star,Creat_time) \
          VALUES ('%s', '%s', '%s', '%s', '%s')" % (title, content, user, '0', now));
    conn.commit()
    conn.close()


# display max 50; Delete nums; Update nums;
def select_all_50():
    print("select_all_50")
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    cursor = c.execute('SELECT * FROM Dreams ORDER BY ID DESC LIMIT 50')
    for row in cursor:
        print(row)
    conn.close()

def db_update_nums(li):
    print("db_update_nums")
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    for l in li:
        print(l)
        c.execute('UPDATE Dreams SET Star=1 WHERE ID = %s' % (l))

    conn.commit()
    conn.close()

def db_delete_nums(li):
    print("db_delete_nums")
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    for l in li:
        print(l)
        c.execute('DELETE FROM Dreams WHERE ID = %s' % (l))
    conn.commit()
    conn.close()

def select_all():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    cursor = c.execute('SELECT * FROM Dreams')
    for row in cursor:
        print(row)
    cursor = c.execute('SELECT * FROM Dreams WHERE Star=?', '0')
    # cursor = c.execute('SELECT * FROM Dreams')
    for row in cursor:
        print(row)




def dodreams(title, user, content):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    if title and content:
        print("title and content")
        title = "如果 " + title
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(now)
        if not user:
            user = "匿名"
        # c.execute("INSERT INTO Dreams (Title,Content,User,Star,Creat_time) \
        c.execute("INSERT INTO Dreams (Title,Content,User,Star,Creat_time) \
              VALUES ('%s', '%s', '%s', '%s', '%s')" % (title, content, user, '0', now));
        conn.commit()

    cursor = c.execute("SELECT ID, Title, Content, User from Dreams ORDER BY ID DESC LIMIT 30 ")
    for row in cursor:
        result = {}
        result['title'] = row[1]
        result['text'] = row[2]
        result['user'] = row[3]
        yield result

def get_best_dreams():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    cursor = c.execute("SELECT ID, Title, Content, User from Dreams  WHERE Star>0 ORDER BY ID DESC LIMIT 30 ")
    for row in cursor:
        result = {}
        result['title'] = row[1]
        result['text'] = row[2]
        result['user'] = row[3]
        yield result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-type')
    parser.add_argument('integers', metavar='N', type=int, nargs='*', help='id, id, id')
    args = parser.parse_args()

    if args.type in ('del', 'd', 'delete'):
        db_delete_nums(args.integers)
    elif args.type in ('up', 'update', 'u'):
        db_update_nums(args.integers)
    elif args.type in ('show', 'list', 'select', 'all'):
        select_all_50()
    else:
        select_all_50()

# creat_db_table()
# select()
