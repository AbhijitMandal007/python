import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="product_pod")

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product name", "price", "availability"])

    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").get_text(strip=True)
        availability = product.find(
            "p", class_="instock availability"
        ).get_text(strip=True)

        writer.writerow([name, price, availability])

print("Products information saved to products.csv")