from tkinter import *
from turtle import position, right
from weakref import WeakSet
from tkinter import ttk
from pyparsing import originalTextFor
from setuptools import Command
import nba_now
from nba_now import *

main_window = Tk()
main_window.geometry("420x420")
main_window.title("NBA NOW")




def score_windowP():
    score_window = Tk()
    score_window.resizable(False, False)
    score_window.geometry("420x420")
    score_window.title("Scoreboard")
    frame_container=Frame(score_window)

    canvas_container=Canvas(frame_container, height=420)
    frame2=Frame(canvas_container)
    myscrollbar=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview) # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0,0),window=frame2,anchor='nw')

    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']
        

    for game in games:
        n = 0.030
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        data = Label(frame2, text=f"{home_team['triCode']} vs {away_team['triCode']}\n{home_team['score']} - {away_team['score']}\n{period['current']} - {clock}",
        font=('Arial', 25, 'bold'),
        relief = RIDGE,
        bd=6,
        padx=20,
        pady=20,
        borderwidth= 5,
        justify=CENTER)
        data.place(relx= 0.5, rely= n, anchor=N)
    
        n+= 0.45
        data.pack() # your labels, entries, whatever you whant inside your frame

    frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
    canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                                #in this case "x=0 y=0 width=0 height=frame2height"
                                                                                                                #width 0 because we only scroll verticaly so don't mind about the width.

    canvas_container.pack(side=LEFT)
    myscrollbar.pack(side=RIGHT, fill = Y)

    frame_container.pack()       


def leaders_windowP():
    leaders_window=Tk()
    #leaders_window.resizable(False, False)
    leaders_window.geometry("620x420")
    leaders_window.title("Team Leaders")
    frame_container=Frame(leaders_window)
    

    canvas_container=Canvas(frame_container, height=420)
    frame2=Frame(canvas_container)
    myscrollbar=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview) # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0,0),window=frame2,anchor='nw')

    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: (x['ppg'],['rank'])) 

    for i, team in enumerate(teams):
        n = 0.030
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        apg = team['apg']['avg']
        

        data = Label(frame2, text=f"{i+1}. {name} - {nickname}\n    PPG: {ppg}\n    APG: {apg}",
        font=('Arial', 25, 'bold'),
        relief = RIDGE,
        bd=6,
        padx=0,
        pady=30,
        borderwidth= 5,
        justify=LEFT)
        data.place(relx= 0, rely= n, anchor=N)
        
        n+= 0.45
        data.pack()

    frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
    canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                                #in this case "x=0 y=0 width=0 height=frame2height"
                                                                                                                #width 0 because we only scroll verticaly so don't mind about the width.

    canvas_container.pack(side=LEFT)
    myscrollbar.pack(side=RIGHT, fill = Y)

    frame_container.pack()

'''
def players_windowP():
    players_window=Tk()
    players_window.geometry("520x520")
    players_window.title("Players Info")

    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: (x['ppg'],['rank'])) #Quite el int, ya no marca error y si corre pero idk xd

    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        apg = team['apg']['avg']
        

    data = Label(players_window, text=f"{i+1}. {name} - {nickname}\n PPG: {ppg}\n APG: {apg}",
    font=('Arial', 25, 'bold'),
    relief = RIDGE,
    bd=6,
    padx=20,
    pady=20,
    borderwidth= 5,
    justify=CENTER)
    data.place(relx= 0.5, rely= n, anchor=N)
    
    n+= 0.45
    data.pack()
'''
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

leaders = Button(main_window, text= "Team Leaders", 
font=('Arial', 12, 'bold'),
justify=CENTER,
state=ACTIVE,
bd=1,
command=leaders_windowP)
leaders.place(relx=0.9, rely=0.5, anchor=E)
'''
players = Button(main_window, text= "Player Info",
font=('Arial', 12, 'bold'),
justify=CENTER,
state=ACTIVE,
bd=1,
command=players_windowP)
players.place(relx=0.5, rely=0.8, anchor=S)
'''

main_window.mainloop()