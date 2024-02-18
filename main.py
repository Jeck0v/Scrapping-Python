#=================================================================================================================
# IMPORT
#=================================================================================================================

from pprint import pprint
import requests
from bs4 import BeautifulSoup
#=================================================================================================================
url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#===========================================================================================
# Recherche d'info sur l'aside
#===========================================================================================

#aside = soup.find('div', class_='side_categories')
#categories_div = aside.find('ul').find('li').find('ul')     #on descend dans l'arborescance pour pointer vers ce que l'on cherche
#categories = [child.text.strip() for child in categories_div.children if child.name] #1 Simplifié avec un pprint(categories) aussi

#===========================================================================================
#Si on veux récup tout les titres complets des livres:
#pprint permet d'affiché les données de façon davantage lisible, et davantage ordonnée
#titles_tags = soup.find_all('a', title = True)
#titles = [a['title'] for a in titles_tags]
#pprint(titles)

#version simplifié de l'exo
titles = [a['title'] for a in soup.find_all('a', title = True)]
pprint(titles)

#============================================================================================
