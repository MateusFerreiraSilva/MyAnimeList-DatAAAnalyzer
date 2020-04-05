from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import json
import time

#1 - Obtem o hmtl

url = 'https://myanimelist.net/topanime.php'

option = Options()
option.headless = True # faz com que a janela do navegador nao apareca
driver = webdriver.Firefox(options=option)
driver.get(url);

for i in range(2, 3):
	element = driver.find_element_by_xpath(
		f'//*[@id="content"]/div[4]/table/tbody/tr[{i}]/td[2]/div/div[2]') 
	element.click()
	
	# Faco essa sopa para descobri o numeros de "spans" no caso seriam o generos
	element = driver.find_element_by_xpath(
		'//*[@id="content"]/table/tbody/tr/td[1]/div/div[19]')
	html_content = element.get_attribute('outerHTML')
	soup = BeautifulSoup(html_content, 'html.parser')
	spans = soup.find_all('span')

	for i in range(2, len(spans)):
		element =  driver.find_element_by_xpath(
			f'//*[@id="content"]/table/tbody/tr/td[1]/div/div[19]/span[{i}]')
		html_content = element.get_attribute('outerHTML')
		soup = BeautifulSoup(html_content, 'html.parser')
		print(soup.get_text())
	print('***************************')

	driver.back()

driver.quit()
