from matplotlib import pyplot as plt
import pandas as pd
import json

with open('AnimeGenres.json') as f:
	array = json.load(f)

data = {k: v for k, v in sorted(array.items(), key=lambda item: item[1], reverse=True)}

sizes = [int(x) for x in data.values()]
labels = list(data.keys())

sizes = sizes[0:10]
labels = labels[0:10]

plt.style.use('fivethirtyeight')
plt.title('The top 10 genres of the most popular animes')


plt.pie(sizes, labels=labels, autopct='%.1f%%',
	 shadow=False, wedgeprops={'edgecolor' : 'black'})

plt.savefig('MostPopularAnimeGenres.png')