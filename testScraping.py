import requests
from bs4 import BeautifulSoup
import pandas as pd

url= "https://www.pycca.com/tecnologia/audio-y-video"

response = requests.get(url)

if response.status_code == 200:
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

    print(data)
    df = pd.DataFrame(data)
    df.to_csv("scraper_products.csv", index=False)


else:
    print("Error al acceder a la página")