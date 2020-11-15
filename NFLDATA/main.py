from bs4 import BeautifulSoup
import pandas as pd
import requests

BASE_URL = 'https://www.pro-football-reference.com/'
YEAR = 2020


def get_fantasy_table(year=YEAR):
    URL = BASE_URL + f'years/{year}/fantasy.htm'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')

    dfs = pd.read_html(soup.prettify())
    print(dfs)


get_fantasy_table()
