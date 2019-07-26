
from bs4 import BeautifulSoup
import requests

query = "py ajax"
site = requests.get("https://duckduckgo.com/html/?q="+query)
data = site.text
soup = BeautifulSoup(data, "html.parser")

my_list = soup.find("div", {"id": "links"}).find_all("div", {'class': re.compile('.*web-result*.')})[0:15]


(result__snippet, result_url) = ([] for i in range(2))

for i in my_list:
      try:
            result__snippet.append(i.find("a", {"class": "result__snippet"}).get_text().strip("\n").strip())
      except:
            result__snippet.append(None)
      try:
            result_url.append(i.find("a", {"class": "result__url"}).get_text().strip("\n").strip())
      except:
            result_url.append(None)
