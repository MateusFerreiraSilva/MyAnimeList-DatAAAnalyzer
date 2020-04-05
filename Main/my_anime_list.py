import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd
from matplotlib import pyplot as plt

#1 - Obtem o hmtl

url = 'https://myanimelist.net/topanime.php'

option = Options()
option.headless = True # faz com que a janela do navegador nao apareca
driver = webdriver.Chrome(options=option)
driver.get(url);

element = driver.find_element_by_xpath(f'//*[@id="content"]/div[4]/table')
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find_all('table')[0] # pega a tabela

#1.5 - Pegar o cabecalho da tabela
columns_name = ['Rank', 'Title', 'Score', 'Format', 'Episodes', 'Date', 'Members']

#2 - Pega o conteudo da tabela
pos = []
anime_name = []
score = []
anime_format = []
anime_episodes = []
anime_date = []
anime_members = []

for row in table.find_all('tr')[1:]: # pega todos os elementos do 1 pra frente
	columns = row.find_all('td')
	cont = 0
	for column in columns[0:3]:
		if cont == 0:
			pos.append(int(column.get_text()))

		elif cont == 1:
			aux = column.find_all('div')

			name = aux[3].find_all('a')[0].get_text()
			anime_name.append(name)

			infos = aux[4].get_text().strip().split('\n')
			infos = [i.strip() for i in infos]

			form = infos[0].split()[0]
			eps = int(infos[0].split()[1].strip('(').strip(')'))
			date = infos[1]
			members = int(infos[2].split()[0].replace(',',''))

			anime_format.append(form)
			anime_episodes.append(eps)
			anime_date.append(date)
			anime_members.append(members)

		else:
			anime_score = float(column.get_text())
			score.append(anime_score)

		cont += 1

table_content = [pos, anime_name, score, anime_format, anime_episodes, anime_date, anime_members]

driver.quit() # Fecho o chrome

#3 - Estruturar com pandas
# Criando dicionario para facilitar a conversão para um DataFrame
dic = {}
for i in range(0, len(columns_name)):
	dic[columns_name[i]] = table_content[i]

df = pd.DataFrame(dic)

#4 - Gera o grafico com matplotlib
x_axis = df['Title'][0:11]
y_axis = df['Members'][0:11]


#fig 1
plt.style.use('seaborn-bright')
plt.bar(x_axis, y_axis)
plt.xlabel('Animes')
plt.ylabel('Members')
plt.title('Most popular anime (MAL)')

plt.grid(True)
plt.xticks(rotation=90)

plt.tight_layout()
plt.savefig('MostPopularAnime.png')
plt.show()

#fig 2

y2_axis = df['Score'][0:11]

plt.style.use('bmh')
plt.scatter(x_axis, y2_axis)
plt.xlabel('Animes')
plt.ylabel('Score')
plt.title('Best Scores of MAL')

plt.grid(True)
plt.xticks(rotation=90)

plt.tight_layout()
plt.savefig('BestScoresMAL.png')
plt.show()