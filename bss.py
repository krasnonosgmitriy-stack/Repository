from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")
for book in books:
    if book.find("p", class_="star-rating Five") or book.find("p", class_="star-rating Four"):
        title = book.find("h3").text
        price = book.find("p", class_="price_color").text
        print(f"{title} - {price}")