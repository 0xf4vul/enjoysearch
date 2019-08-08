import json

def get_info_json():
    textinfo = None
    with open("textinfo.json", 'r') as fd:
        textinfo = json.load(fd)
        print(textinfo)
        print(textinfo.keys())
        # print(textinfo["x2"])
        # print(textinfo["book"][0]["id"])
        # print(textinfo["book"][1]["id"])

        # result = [(item.get('language', 'NA'), item.get('edition', 'NA')) for item in textinfo['book']]
        # print(result)

        for x in textinfo:
            print(textinfo[x])
            if x == "book":
                for y in textinfo[x]:
                    print(y)
                    for xy in y:
                        print(y[xy])

get_info_json()
