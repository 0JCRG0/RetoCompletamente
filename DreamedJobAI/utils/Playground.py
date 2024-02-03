import requests
import together
from dotenv import load_dotenv
import os
import logging
import json
from bs4 import BeautifulSoup
from googlesearch import search
from dotenv import load_dotenv

load_dotenv(".env")

SERP_API = os.environ.get("SERP_API")

lugares_recomendados = [
    "parque local",
    "estudio de yoga",
    "gimnasio cercano",
    "centro de meditación",
    "jardín botánico"]

location = "en Puebla"

from serpapi import GoogleSearch

def get_results(query, num_results=2, location="Puebla"):
	params = {
		"q": query,
		"location": location,
		"api_key": f"{SERP_API}"
		}

	search = GoogleSearch(params)
	results = search.get_dict()
	#new_results = results.get("results", [])

	#urls = [result['link'] for result in results]
	return results

x = get_results("Cafe")

y = len(x)

print(x, y)

exit()

#for result in search(query, num_results=2, sleep_interval=2, timeout=5):
#		print(result)

import yagooglesearch

query = "site:github.com"



for place in lugares_recomendados:
	query = place + location
	client = yagooglesearch.SearchClient(
    query,
    tbs="li:1",
    max_search_result_urls_to_return=1,
    http_429_cool_off_time_in_minutes=45,
    http_429_cool_off_factor=1.5,
    # proxy="socks5h://127.0.0.1:9050",
    verbosity=5,
    verbose_output=False,  # False (only URLs) or True (rank, title, description, and URL)
	)
	client.assign_random_user_agent()

	urls = client.search()

	len(urls)

	for url in urls:
		print(url)

exit()

load_dotenv(".env")

TOGETHER_API_KEY = os.environ.get("TOGETHER_AI_API_KEY")