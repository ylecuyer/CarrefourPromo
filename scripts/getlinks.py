import requests
import urllib
from bs4 import BeautifulSoup

url = "http://www.carrefour.fr/carte-carrefour/5-d-economies-tous-les-jours"
r = requests.get(url)
soup = BeautifulSoup(r.text)

results = soup.find_all(class_="content")[10].find_all("a")

print(results[0]['href'])
print("\tout=input_express.pdf")
print(results[1]['href'])
print("\tout=input_contact.pdf")
print(results[2]['href'])
print("\tout=input_city.pdf")
print(results[3]['href'])
print("\tout=input_montagne.pdf")
