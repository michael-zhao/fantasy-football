from sys import argv
from requests import get
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.pro-football-reference.com/'
year = datetime.today().year-1
max_players = 300

r = get(url + '/years/' + str(year) + '/fantasy.htm')
soup = BeautifulSoup(r.content, 'html.parser')
parsed_table = soup.find_all('table')[0]

df = []

for i, row in enumerate(parsed_table.find_all('tr')[2:]):
    if i % 10 == 0:
        print(i, end=' ')
    if i >= max_players:
        print('\nComplete.')
        break

    try:
        dat = row.find('td', attrs = {'data-stat': 'player'})
        name = dat.a.get_text()
        stub = dat.a.get('href')
        stub = stub[:-4] + '/fantasy/' + str(year)
        pos = row.find('td', attrs={'data-stat': 'fantasy_pos'}).get_text()

        tdf = pd.read_html(url + stub)[0]

        tdf.columns = tdf.columns.get_level_values(-1)

        tdf = tdf.rename(columns={'Unnamed: 4_level_2': 'Away'})
        tdf['Away'] = [1 if r=='@' else 0 for r in tdf['Away']]

        tdf = tdf.iloc[:, [1,2,3,4,5,-3]]

        tdf = tdf.query('Date != "Total"')

        tdf['Name'] = name
        tdf['Position'] = pos
        tdf['Season'] = year

        df.append(tdf)
    except:
        pass

df = pd.concat(df)
df.head()

df.to_csv('fantasy2019.csv')

