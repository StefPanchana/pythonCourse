import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url= "https://www.pycca.com/tecnologia/audio-y-video"

#Decorador para medir tiempo de ejecución
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin= time.time()
        print(f"El tiempo de ejecucion de {__name__} : es de {fin-inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def obtener_datos_productos(url):
    response = requests.get(url)
    
    soup= BeautifulSoup(response.text, 'html.parser')
    data = []

    items = soup.select(".productVitrine")

    for item in items:
        name_element = item.select_one("a")
        price_element = item.select_one(".price")

        if name_element and price_element:
            name = name_element["title"]
            price = price_element.get_text(strip=True)

            data.append({
                "title": name,
                "price": price
                })
            
        if not name_element or not price_element:
            continue
    return data

@medir_tiempo
def procesar_datos(products):
    df = pd.DataFrame(products)
    df