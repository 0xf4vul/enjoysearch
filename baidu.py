#!/usr/bin/env python3

from MagicBaidu import MagicBaidu
import requests
import pprint


keyword = "readmorejoy"

# Get {'title','url','text'}
def mb_test():
	mb = MagicBaidu()
	for i in mb.search(query='readmorejoy', start=10):
		try:
			pprint.pprint(i)
		except:
			pass

def baidu_test():
	kv = {'wd':keyword, 'pn':1}
	r = requests.get("http://www.baidu.com/s", params=kv)
	#print(r.request.url)
	#pprint.pprint(r.text, )
	print(r.text)



baidu_test()
