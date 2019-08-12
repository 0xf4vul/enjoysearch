#!/usr/bin/env python3
import toml
import random
import os

def change_text_info():
    path = os.path.dirname(os.path.realpath(__file__))
    in_name = path + "/static/textinfo.toml"
    out_name = path + "/static/tellyou.txt"

    with open(in_name, 'r', encoding="utf-8") as fd:
        text = toml.loads(fd.read())

        num = random.randint(1, text["total"])
        name = "text" + str(num)
        print(text[name])

        with open(out_name, 'w') as fd:
            fd.write(text[name]+"\n")

if __name__ == '__main__':
    change_text_info()
