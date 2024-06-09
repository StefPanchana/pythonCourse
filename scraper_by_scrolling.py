import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://www.pycca.com/tecnologia/audio-y-video"
base_products_by_scroll = 10


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
def scan_all_items_of_page(soup):
    #Obtener el número total de productos de la página especifica
    total_productos = float(soup.select_one(".value").get_text(strip=True))
    print(f"La cantidad de productos en esta pagina es de: {total_productos}")

    #Calcular el promedio de scrolling a realizar
    scroll_count = int(total_productos / base_products_by_scroll)

    return total_productos


@medir_tiempo
def scrolling_execute(scroll_count, driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    elements = []
    while scroll_count > len(elements):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        # elements = driver.find_elements(By.CLASS_NAME, 'productVitrine')
        initial_html = driver.page_source
        initial_soup = BeautifulSoup(initial_html, "html.parser")
        items = initial_soup.select(".productVitrine")
        elements = process_data(items)

    # Close the WebDriver
    driver.quit()
    # Return elements
    return elements

@medir_tiempo
def process_data(items):
    data = []
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
def scrolling_page(scroll_count, driver):
    #Ciclo de obtencion de datos de la pagina para obtener datos completos de la pagina de productos
    for scroll in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"Ejecutando scroll {scroll}")
        #Tiempo de espera para que el scrolling haya finalizado y poder obtener todos los productos
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "productVitrine")))

    initial_html = driver.page_source
    initial_soup = BeautifulSoup(initial_html, "html.parser")
    # Close the WebDriver
    driver.quit()
    return initial_soup

@medir_tiempo
def obtener_datos_productos(soup, scroll_count):
    data = []
    items = soup.select(".productVitrine")

    if len(items) == scroll_count:
        print("Se ha completado el scroll de productos de la pagina")
    else:
        print(f"Productos scaneados despues de ejecutar scrolling {len(items)}")

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
def process_scrapping(base_url, driver):
    driver.get(base_url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "productVitrine")))
    initial_html = driver.page_source
    initial_soup = BeautifulSoup(initial_html, "html.parser")
    return initial_soup


@medir_tiempo
def guardar_datos_df(productos):
    df = pd.DataFrame(productos)
    df.to_csv("scraper_products.csv")

# Procesar scrapping de pagina
driver = webdriver.Chrome()  # Make sure you have chromedriver installed and in your PATH
soup = process_scrapping(base_url, driver)
# Scan all items de la pagina a procesar
scroll_count = scan_all_items_of_page(soup)
# Ejecutar Scrolling
# initial_soup = scrolling_page(scroll_count, driver)
products = scrolling_execute(scroll_count, driver)
# Obtener datos de los productos de la pagina
#products = obtener_datos_productos(initial_soup, scroll_count)
# Guardar productos en un archivo .csv
guardar_datos_df(products)
