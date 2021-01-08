import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from datetime import datetime
import player_scrape
# import warnings

# warnings.filterwarnings('ignore')

player = input("Player name (e.g. Russell Wilson): ")
year = input("Year (default is latest season): ") or datetime.today().year-1

# df = player_scrape.create_player_df(player, year)
# print(df)

# read from the scraped csv instead of straight from the website
df = pd.read_csv('fantasy2019.csv')

# drop the game #, date, team, away (W/L), and season (all 2019)
df.drop(['G#', 'Date', 'Tm', 'Away', 'Season'])

#separate based on position
rb_df = df[df['Position'] == 'RB']
qb_df = df[df['Position'] == 'QB']
wr_df = df[df['Position'] == 'WR']
te_df = df[df['Position'] == 'TE']
