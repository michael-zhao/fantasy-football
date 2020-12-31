"""Scrapes all the data for a single player given a season.
"""
import pandas as pd

player = input("Player name: ")
year = input("Year: ")

url = f'https://www.pro-football-reference.com/search/search.fcgi?search={player}'
