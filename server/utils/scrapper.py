import pandas
import requests
from bs4 import BeautifulSoup
from utils.date import DATE_REGEX


def get_game_logs(_id, year):
    url = f"https://www.espn.com/nba/player/gamelog/_/id/{_id}/type/nba/year/{year}"
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, "html.parser")
    tables = soup.find_all("table")
    dfs = pandas.read_html(str(tables), match=DATE_REGEX)
    for i in range(len(dfs)):
        dfs[i] = dfs[i][dfs[i].Date.str.contains(DATE_REGEX)]
    stats = pandas.concat(dfs)
    return stats
