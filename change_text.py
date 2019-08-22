#!/usr/bin/env python3
import toml
import random
import os, shutil

def change_text_info():
    path = os.path.dirname(os.path.realpath(__file__))
    in_name = path + "/static/textinfo.toml"
    out_name = path + "/static/tellyou.txt"
    html1 = path + "/templates/search.html"
    html2 = path + "/templates/tmp.html"

    with open(in_name, 'r', encoding='utf-8') as fd:
        text = toml.loads(fd.read())

        num = random.randint(1, text["total"])
        name = "text" + str(num)
        # print(text[name])

        # with open(out_name, 'w', encoding='utf-8') as fd:
        #     fd.write(text[name]+"\n")
        # <div id="tellyou">{{ tellyou }}</div>

        with open(html1, 'r', encoding='utf-8') as fd, open(html2, 'w', encoding='utf-8') as fd2:
            lines = fd.readlines()
            for line in lines:
                if "<div id=\"tellyou\">" in line:
                    # print(line)
                    # line = "change tellyou"
                    line = "<div id=\"tellyou\">" + text[name] + "</div>\n"
                fd2.write(line)
        # print("result check")
        shutil.copyfile(html2, html1)
            #print(lines)

if __name__ == '__main__':
    change_text_info()
