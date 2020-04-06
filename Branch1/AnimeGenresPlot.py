from matplotlib import pyplot as plt
import pandas as pd
import json

with open('AnimeGenres.json') as f:
	array = json.load(f)

data = {k: v for k, v in sorted(array.items(), key=lambda item: item[1], reverse=True)}

x_axis = [int(x) for x in data.values()]
y_axis = data.keys()

plt.style.use('fivethirtyeight')
plt.ylabel('Amount in top 50 anime')
plt.xlabel('Genre of anime')
plt.title('The genres of the most popular animes')
plt.grid(True)
plt.xticks(rotation=90)
plt.bar(y_axis, x_axis)

plt.show()
plt.savefig('MostPopularAnimeGenres.png')