import requests
from bs4 import BeautifulSoup

url= "https://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup= BeautifulSoup(response.content, 'html.parser')

    autores = soup.find_all("small", class_="author")

    for autor in autores:
        print(autor.text)

else:
    print("Error al acceder a la página")