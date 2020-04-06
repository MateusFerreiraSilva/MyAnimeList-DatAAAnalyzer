from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import json
import time
from collections import Counter

#1 - Obtem o hmtl

url = 'https://myanimelist.net/topanime.php'

option = Options()
option.headless = True # faz com que a janela do navegador nao apareca
driver = webdriver.Firefox(options=option)
driver.get(url);

c = Counter()

for i in range(2, 52):
	try:
		element = driver.find_element_by_xpath(
			f'//*[@id="content"]/div[4]/table/tbody/tr[{i}]/td[2]/div/div[2]')
	except:
		continue 

	element.click()
	
	try:
		element = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr/td[1]/div')
	except:
		continue

	hmtl_content = element.get_attribute('outerHTML')
	soup = BeautifulSoup(hmtl_content, 'html.parser')

	dark_texts = soup.find_all('span', 'dark_text')
	
	for i in dark_texts:
		if i.get_text() == 'Genres:':
			genres = i.find_next_siblings('span')
			list_genres = [g.get_text() for g in genres]
			c.update(list_genres)
	
	driver.back()

driver.quit()

with open('AnimeGenres.json', 'w', encoding='utf-8') as file:
	js = json.dumps(c, indent=4) 
	file.write(js)