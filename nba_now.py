from requests import get
from pprint import PrettyPrinter 

BASE_URL = "https://data.nba.net" #URL del que vamos a pedir informacion
ALL_JSON = "/prod/v1/today.json"

printer =  PrettyPrinter()
home_team = 0
away_team = 0

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    #printer.pprint(data)
    links = data['links']
    return links
    
#Dara el link del que vamos a sacar la informacion 

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("-------------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{period['current']} - {clock}")
#Funcion para mostrar el Scoreboard de los juegos que se estan jugando actualmente


def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(
        BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: (x['ppg'],['rank'])) #Quite el int, ya no marca error y si corre pero idk xd

    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        apg = team['apg']['avg']
        print("-----------------------------------")
        print(f"{i+1}. {name} - {nickname}")
        print(f"    PPG: {ppg}")
        print(f"    APG: {apg}")

    #printer.pprint(teams[0].keys())


def get_players():
    stats = get_links()['leagueRosterPlayers']
    players = get(BASE_URL + stats).json()['league']['standard']

    #printer.pprint(players1[0].keys())

    for player in players:
        fname = player['firstName']
        lname = player['lastName']
        jersey = player['jersey']
        pos = player ['pos']
        height = player['heightFeet']
        team = player['lastAffiliation']
        print("---------------------------")
        print(f"{fname} {lname} - {team}")
        print(f"Number: {jersey}") 
        print(f"Height: {height} feet")
        print(f"Position: {pos}")

#Muestra a los equipos lideres en la tabla segun su rank


#Desarrollar mas el programa, agregar un menu que permita al usuario elegir cualquiera de los 3 metodos, agregar mas metodos como mostrar a los jugadores lideres en puntos, etc.

get_scoreboard()
'''
get_players()
get_scoreboard()
get_stats()
'''