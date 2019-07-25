#!/usr/bin/env python3

from MagicGoogle import MagicGoogle
import pprint

mg = MagicGoogle()

#  Crawling the whole page
# results = mg.search_page(query='readmorejoy')
# for result in results:
#     print(result)

#pprint.pprint(result)

morejoys = mg.search(query='readmorejoy')
for result in morejoys:
    print(result)

# Crawling url
# for url in mg.search_url(query='python'):
#     pprint.pprint(url)
