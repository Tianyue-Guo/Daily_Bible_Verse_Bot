import requests
from bs4 import BeautifulSoup
def bible_response():
	response = requests.get("https://www.verseoftheday.com/")
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'html.parser')
		div_element = soup.find("div", {"class": "bilingual-left"})
		if div_element:
			print(div_element.text)


bible_response()