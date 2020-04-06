import datetime
from matplotlib import pyplot as plt
import pandas as pd

def to_datetime(dates):
	begin = []
	end = []
	for x in dates:
		aux = x.split(' - ')
		begin.append(datetime.datetime.strptime(aux[0], '%b %Y'))
		end.append(datetime.datetime.strptime(aux[1], '%b %Y'))
	return [begin, end]

df = pd.read_json('TopAnimeTable.json')
df['DateBegin'], df['DateEnd'] = to_datetime(df['Date'])
df['Date'].drop
print(df)

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