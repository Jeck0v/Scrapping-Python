import requests
from bs4 import BeautifulSoup

url = "https://www.docstring.fr/api/books_to_scrape/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#find = soup.find_all('article', class_="product_pod")
#print(find)
aside = soup.find('aside')
for child in aside.children:
    print(child.name)





#print(soup.prettify())
#parser 1 = lxml-xml (fichier de config / échange de donnée)
#parser 2 = html.parser (  /!\ moins tolérant aux erreurs mais plus rapide)
#parser 3 = html5lib (plus lent mais plus tolérant)





#with open ('index.html', 'w') as f:        #créer un fichier html avec les infos récolté, dans ce cas là le code html de google.com
    #f.write(response.text)

#print (response.status_code)

# .raise_for_status() pour relever les erreur
# .status_code pour voir le code erreur

