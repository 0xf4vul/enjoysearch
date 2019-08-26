
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pprint

url = "https://www.readmorejoy.com/"
site = requests.get(url)
data = site.text
soup = BeautifulSoup(data, "lxml")


# my_list = soup.find("div", {"id": "links"}).find_all("div", {'class': re.compile('.*web-result*.')})[0:15]

all = soup.find_all("a")
all_urls = set()

for a in all:
    u = (a.get('href'))
    if u.startswith("/"):
        u = urljoin(url, u)

    all_urls.add(u)
pprint.pprint(all_urls)
# str = str(all_urls, "\n")
# print(str)
