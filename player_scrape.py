"""Scrapes all the data for a single player given a season.
"""
import pandas as pd
import requests
from datetime import date, datetime
import webbrowser

def find_id(player_name):
    url = f'https://www.pro-football-reference.com/search/search.fcgi?search={player}'
    redirect_url = requests.get(url).url
    player_id = redirect_url.split('/')[5].partition('.')[0]
    return player_id

player = input("Player name (e.g. Russell Wilson): ")
year = input("Year (default is latest season): ") or datetime.today().year-1
player_id = find_id(player)
fantasy_url = f'https://www.pro-football-reference.com/players/{player_id[0]}/{player_id}/fantasy/{year}'

# for testing:
# webbrowser.open(fantasy_url)

# needed to run `pip3 install lxml`
# reads in the table of weeks/fpts
df = pd.read_html(fantasy_url)[0]
# print(df)


