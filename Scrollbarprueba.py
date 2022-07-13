
from tkinter import *
from tkinter import ttk
from turtle import left

from debugpy import configure
from setuptools import Command
import nba_now
from nba_now import * 

n = 0.030
scoreboard = get_links()['currentScoreboard']
games = get(BASE_URL + scoreboard).json()['games']

win = Tk()
win.title('MyScroller')
win.geometry("620x520")
win.resizable(False, False)

wrapper1= LabelFrame(win)

mycanvas = Canvas(wrapper1, width=520, height=520)
mycanvas.pack(side=LEFT)



yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command= mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=0, pady=0)

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
        

    data = Label(myframe, text=f"{i+1}. {name} - {nickname}\n    PPG: {ppg}\n    APG: {apg}",
    font=('Arial', 25, 'bold'),
    relief = RIDGE,
    bd=6,
    padx=0,
    pady=30,
    borderwidth= 5,
    justify= LEFT)
    data.place(relx= 0, rely= n, anchor=N)
        
    n+= 0.45
    data.pack()


win.mainloop()