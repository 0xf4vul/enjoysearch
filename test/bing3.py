import requests

subscription_key = "35b243b7106244a5b4ade56b8fb4c093"
assert subscription_key


search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

search_term = "google search site"

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
#"count":5,
params = {"q": search_term, "textDecorations": True, "textFormat": "HTML",  "offset":5}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

for v in search_results["webPages"]["value"]:
    print(v["name"])
    print(v["url"])

    # print(len(v))

#print(search_results)
