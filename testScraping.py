import string

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.pycca.com/tecnologia/audio-y-video"

#Decorador para medir tiempo de ejecución
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"El tiempo de ejecucion de {func.__name__} : es de {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def obtener_datos_productos(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    items = soup.select(".productVitrine")

    for item in items:
        name_element = item.select_one("a")
        price_element = item.select_one(".price")

        if name_element and price_element:
            name = name_element["title"]
            price = price_element.get_text(strip=True)
            data.append({"title": name, "price": price})

        if not name_element or not price_element:
            continue
    return data

@medir_tiempo
def guardar_datos_df(productos):
    df = pd.DataFrame(productos)
    df.to_csv("scraper_products.csv")

@medir_tiempo
def procesar_productos(productos):
    datos_procesados = []
    for title, price in productos:
        price.replace('$','')
        price = float(price)
        datos_procesados.append(f"Producto: {title}, Precio: {price}")
    return datos_procesados

@medir_tiempo
def escribir_datos_archivo(datos, archivo):
    with open(archivo, "w", encoding="utf-8") as archivo:
        for linea in datos:
            archivo.write(linea + "\n")

@medir_tiempo
def crear_archivo_local(products):
    df = pd.DataFrame(products)
    df.to_csv("scraper_products.csv", index=False)

@medir_tiempo
def procesar_scraping(url):
    products = obtener_datos_productos(url)
    guardar_datos_df(products)
    # escribir_datos_archivo(datos_procesados, "scraper_products.csv")

@medir_tiempo
def calcular_estadisticas(archivo):
    df = pd.read_csv(archivo)
    df["price"] = df["price"].replace("[$,]", "", regex=True)
    df['price'] = df['price'].astype(float)
    print(f"Precio promedio: {df['price'].mean():.2f}")
    print(f"Precio minimo: {df['price'].min():.2f}")
    print(f"Precio maximo: {df['price'].max():.2f}")

##Proceso de Scraping de una URL especifica
#procesar_scraping(url)
##Preparacion de columna de precio antes de verificar las estadisticas de la columna precio
calcular_estadisticas("scraper_products.csv")

