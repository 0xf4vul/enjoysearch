#!/usr/bin/env python3
import toml
import random
import os, shutil
from datetime import datetime

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
def new_change_text_info():
    # define day time
    day_time = [
    {"start":"00:00", "end":"05:00", "name":"day_text1"},
    {"start":"05:01", "end":"06:00", "name":"day_text2"},
    {"start":"06:01", "end":"08:30", "name":"day_text3"},
    {"start":"08:31", "end":"09:30", "name":"day_text4"},
    {"start":"09:10", "end":"11:30", "name":"day_text5"},
    {"start":"11:31", "end":"13:00", "name":"day_text6"},
    {"start":"13:01", "end":"14:00", "name":"day_text7"},
    {"start":"14:01", "end":"17:50", "name":"day_text8"},
    {"start":"17:51", "end":"20:00", "name":"day_text9"},
    {"start":"20:01", "end":"22:00", "name":"day_text10"},
    {"start":"22:01", "end":"23:00", "name":"day_text11"},
    {"start":"23:01", "end":"24:00", "name":"day_text12"},
    ]

    a = "08:42"
    b = "21:02"
    for d in day_time:
        if (a > d["start"]) and (a < d["end"]):
            print(d)
        if (b > d["start"]) and (b < d["end"]):
            print(d)
        pass

    path = os.path.dirname(os.path.realpath(__file__))
    in_name = path + "/static/textinfo.toml"
    with open(in_name, 'r', encoding='utf-8') as fd:
        text = toml.loads(fd.read())

        print(text["day_time_2"])
        print(text["day_time_2"]["total"])
        print(text["day_time_2"]["text1"])

        now = datetime.now()
        print(now.strftime('%a, %b %d %H:%M'))
        time_h = now.strftime('%H')
        time_m = now.strftime('%M')
        print(time_h, time_m)
        # num = random.randint(1, text["total"])
        # name = "text" + str(num)
    pass

if __name__ == '__main__':
    new_change_text_info()
