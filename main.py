import requests
import re
from bs4 import BeautifulSoup

def price_range_to_integers(price_range):
    return [int(salary.replace(" ","")) for salary in price_range]

url = 'https://rocketjobs.pl/widelki_tak'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')

job_offers = []

offers = soup.find_all(class_='MuiBox-root css-6vg4fr')
for offer in offers:
    job_name = offer.find('h2', class_='css-g9dzcj').get_text()
    price_range = re.findall(r'\d+\s\d+', offer.find(class_='css-lz8wxo').get_text())
    job_offers.append({'jobName': job_name, 'salary':price_range_to_integers(price_range)})


print(job_offers)