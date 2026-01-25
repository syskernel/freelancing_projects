import requests
from bs4 import BeautifulSoup

url = "https://www.petsmart.com/search/f/category/dry%20food?q=dog%2520food"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "lxml")

print(soup)