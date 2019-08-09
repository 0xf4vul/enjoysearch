#!/usr/bin/env python3
import toml
import random

def change_text_info():
    in_name = "static/textinfo.toml"
    out_name = "static/tellyou.txt"

    with open(in_name, 'r') as fd:
        text = toml.loads(fd.read())

        num = random.randint(1, text["total"])
        name = "text" + str(num)
        print(text[name])

        with open(out_name, 'w') as fd:
            fd.write(text[name]+"\n")

if __name__ == '__main__':
    change_text_info()
