"""Scrapes all the data for a single player given a season.
"""
import pandas as pd
import requests

def find_id(player_name):
    url = f'https://www.pro-football-reference.com/search/search.fcgi?search={player}'
    redirect_url = requests.get(url).url
    player_id = redirect_url.split('/')[5].partition('.')[0]
    return player_id    

player = input("Player name: ")
year = input("Year: ")

print(find_id(player))

