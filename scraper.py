from sys import argv
from requests import get
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

year = datetime.today().year-1 or int(input("Enter your desired year (default is previous season): "))
week = None or int(input(f"What week of the {year} season? (default is whole season) "))

