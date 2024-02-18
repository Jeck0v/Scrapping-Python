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
#images = soup.find('section').find_all('img')
#for images in images:
        #print(images.get('src'))        #possible aussi avec images['src'] mais risque d'erreur si y a pas d'attribut src


#for category in categories.children:   #1
        #print(category.text.strip())


#find = soup.find_all('article', class_="product_pod")
#print(find)
#aside = soup.find('aside')
#side_categories = aside.find('div', class_='side_categories')
#print(side_categories)



#for child in aside.children:
    #print(child.name)





#print(soup.prettify())
#parser 1 = lxml-xml (fichier de config / échange de donnée)
#parser 2 = html.parser (  /!\ moins tolérant aux erreurs mais plus rapide)
#parser 3 = html5lib (plus lent mais plus tolérant)





#with open ('index.html', 'w') as f:        #créer un fichier html avec les infos récolté, dans ce cas là le code html de google.com
    #f.write(response.text)

#print (response.status_code)

# .raise_for_status() pour relever les erreur
# .status_code pour voir le code erreur

