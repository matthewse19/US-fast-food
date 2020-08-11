import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://restaurants.subway.com/united-states'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_="Directory-listLink")

path = 'C:\\Users\\mcse\\Documents\\GitHub\\US-fast-food\\datasets\\'
with open((path + 'subway-data.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["State", "Subway stores"])
    for result in results:
        writer.writerow([result.span.text, result.attrs['data-count'][1:-1]])
