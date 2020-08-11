import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://locations.pizzahut.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_="Directory-listLink")

path = 'C:\\Users\\mcse\\Documents\\GitHub\\US-fast-food\\datasets\\'
with open((path + 'pizza-hut-data.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["State", "Pizza hut stores"])
    for result in results:
        writer.writerow([result.span.text, result.attrs['data-count'][1:-1]])
