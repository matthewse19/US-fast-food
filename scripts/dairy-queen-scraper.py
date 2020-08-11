import requests
from bs4 import BeautifulSoup
import csv
import us_state_abbrev as usa

def convert(abbrev):
    return usa.abbrev_us_state[abbrev] if abbrev in usa.abbrev_us_state else abbrev

URL = 'https://www.dairyqueen.com/us-en/Sitemap/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_="center-960")

path = 'C:\\Users\\mcse\\Documents\\GitHub\\US-fast-food\\datasets\\'
with open((path + 'dairy-queen-data.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["State/Province", "DQ stores"])
    state = ''
    count = 0
    for result in results:
        if result.name == 'h2':
            if state != '':
                #append previous data
                writer.writerow([convert(state), count])
            state = result.string
            count = 0
        elif result.name == 'ul':
            count = len(list(result.find_all('li')))
    #append the last one
    writer.writerow([convert(state), count])
