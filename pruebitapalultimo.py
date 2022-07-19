from tkinter import *
from turtle import position
from weakref import WeakSet
import nba_now
from nba_now import *
from tkinter import ttk

main_window = Tk()
main_window.geometry("420x420")
main_window.title("NBA NOW")

def score_windowP():
    n = 0.030
    score_window = Tk()
    score_window.resizable(False, False)
    score_window.geometry("420x420")
    score_window.title("Scoreboard")
    frame_container=Frame(score_window)

    canvas_container=Canvas(frame_container, height=420)
    frame2=Frame(canvas_container)
    myscrollbar=Scrollbar(frame_container,orient="vertical",command=canvas_container.yview) # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0,0),window=frame2,anchor='nw')

    stats = get_links()['leagueRosterPlayers']
    players = get(BASE_URL + stats).json()['league']['standard']

    for player in players:
        fname = player['firstName']
        lname = player['lastName']
        jersey = player['jersey']
        pos = player ['pos']
        height = player['heightFeet']
        team = player['lastAffiliation']

        data = Label(frame2, text=f"{fname} {lname} - {team}\n    Number: {jersey}\n    Height: {height} feet\n    Position: {pos}",
        font=('Arial', 25, 'bold'),
        relief = RIDGE,
        bd=6,
        padx=0,
        pady=30,
        borderwidth= 5,
        justify= LEFT)
        data.place(relx= 0, rely= n, anchor=N)
                
        n+= 0.45
        data.pack() # your labels, entries, whatever you whant inside your frame

    frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
    canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                                    #in this case "x=0 y=0 width=0 height=frame2height"
                                                                                                                    #width 0 because we only scroll verticaly so don't mind about the width.

    canvas_container.pack(side=LEFT)
    myscrollbar.pack(side=RIGHT, fill = Y)

    frame_container.pack()

players = Button(main_window, text= "Player Info",
font=('Arial', 12, 'bold'),
justify=CENTER,
state=ACTIVE,
bd=1,
command=score_windowP)
players.place(relx=0.5, rely=0.8, anchor=S)

main_window.mainloop()