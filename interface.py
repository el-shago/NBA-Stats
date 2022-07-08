from tkinter import *
from turtle import position
from weakref import WeakSet
import nba_now
from nba_now import *

main_window = Tk()
main_window.geometry("420x420")
main_window.title("NBA NOW")

def score_windowP():
    n = 0.030
    score_window=Tk()
    score_window.geometry("420x420")
    score_window.title("Scoreboards")
    
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']
    

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        
        guiones = Label(score_window, text=f"{home_team['triCode']} vs {away_team['triCode']}\n{home_team['score']} - {away_team['score']}\n{period['current']} - {clock}",
        font=('Arial', 25, 'bold'),
        relief = RAISED,
        bd=6,
        padx=20,
        pady=20,
        justify=CENTER)
        guiones.place(relx= 0.5, rely= n, anchor=N)
        n+= 0.45

#Label
Title = Label(main_window, text= "NBA NOW",
font=('Arial', 25, 'bold'),
relief = RAISED,
bd=6,
padx=20,
pady=20,
justify=CENTER)
Title.place(relx= 0.5, rely=0.030, anchor=N)

#Buttons
score = Button(main_window, text= "Scoreboards",
font=('Arial', 12, 'bold'),
justify=CENTER,
state=ACTIVE,
bd=1,
command=score_windowP)
score.place(relx=0.1, rely=0.5, anchor=W)
'''
leaders = Button(main_window, text= "Team Leaders", 
font=('Arial', 12, 'bold'),
justify=CENTER,
state=ACTIVE,
bd=1,
command=leaders_windowP)
leaders.place(relx=0.9, rely=0.5, anchor=E)

players = Button(main_window, text= "Player Info",
font=('Arial', 12, 'bold'),
justify=CENTER,
state=ACTIVE,
bd=1,
command=players_windowP)
players.place(relx=0.5, rely=0.8, anchor=S)
'''
main_window.mainloop()

#Falta decorar pero acomodado ya esta
#Scoreboard ya corre en ventanas, falta decorar, poner scroll y buscar la manera de que se actualice en tiempo real