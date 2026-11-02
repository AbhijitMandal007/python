import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/" 
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

headlines = soup.find_all("span",class_ = "titleline")

for headline in headlines:
    link = headline.find("a")

    if link:
        print("Headline:",link.text)
        print("link",link.get("herf"))
        print()