
import os
import requests
import time
import urllib.request, urllib.parse, urllib.error
from src.user_agents import random_user_agent
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

def todo_save_to(user, content):
    name = "todo/" + user
    with open(name, 'w') as file:
        print("save to file")
        file.write(content)


def todo_read_from(user):
    name = "todo/" + user
    with open(name) as file:
        print("read from file")
        return file.read()
