# selenium - biblioteka do automatyzacji zadan, np.: klikanie na stronach www

from selenium import webdriver
from bs4 import BeautifulSoup

# url = 'https://it.pracuj.pl/praca/python;kw'
url2 = "https://it.pracuj.pl/praca/programista%20python;kw"
driver = webdriver.Chrome()
driver.get(url2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

data = soup.find('script', {'id': '__NEXT_DATA__'}).text
print(data)

offers_count = int(data.split('offersCount":')[1].split(",")[0])
print(offers_count)  # 942, 220
