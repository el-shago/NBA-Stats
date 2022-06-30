from requests import get
from pprint import PrettyPrinter 

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer =  PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("-------------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}, {clock}, {period} ")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{period['current']} - {clock}")

def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    data = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']



get_scoreboard()