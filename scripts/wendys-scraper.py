import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://locations.wendys.com/united-states'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_="Directory-listLink")

path = 'C:\\Users\\mcse\\Documents\\GitHub\\US-fast-food\\datasets\\'
with open((path + 'wendys-data.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["State", "Wendy's stores"])
    for result in results:
        writer.writerow([result.text, result.next_sibling.text[1:-1]])
