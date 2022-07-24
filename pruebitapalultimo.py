from tkinter import *
from turtle import position
from weakref import WeakSet
import nba_now
from nba_now import *
from tkinter import ttk

main_window = Tk()
main_window.geometry("420x420")
main_window.title("NBA NOW")

def players_windowP():
    n = 0.030

    win = Tk()
    win.title('Player Info')
    win.geometry("820x520")
    win.resizable(False, False)

    wrapper1= LabelFrame(win)

    mycanvas = Canvas(wrapper1, width=800, height=520)
    mycanvas.pack(side=LEFT)



    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command= mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)

    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window=myframe, anchor="nw")

    wrapper1.pack(fill="both", expand="yes", padx=0, pady=0)

    stats = get_links()['leagueRosterPlayers']
    players = get(BASE_URL + stats).json()['league']['standard']


    for player in players:
        fname = player['firstName']
        lname = player['lastName']
        jersey = player['jersey']
        pos = player ['pos']
        height = player['heightFeet']
        team = player['lastAffiliation']

        data = Label(myframe, text=f"{fname} {lname} - {team}\n    Number: {jersey}\n    Height: {height} feet\n    Position: {pos}",
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

players = Button(main_window, text= "Player Info",
font=('Arial', 12, 'bold'),
justify=CENTER,
state=ACTIVE,
bd=1,
command=players_windowP)
players.place(relx=0.5, rely=0.8, anchor=S)

main_window.mainloop()