import requests
import re
from bs4 import BeautifulSoup

url = 'https://rocketjobs.pl/widelki_tak'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')

job_offers = []

offers = soup.find_all(class_='MuiBox-root css-6vg4fr')
for offer in offers:
    job_name = offer.find('h2', class_='css-g9dzcj').get_text()
    salary = re.search(r'\d+\s\d+', offer.find(class_='css-lz8wxo').get_text()).group()
    job_offers.append({'jobName': job_name, 'salary': salary})


print(job_offers)
