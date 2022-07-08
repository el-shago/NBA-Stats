from tkinter import *
from tkinter import ttk
import nba_now
from nba_now import * 

n = 0.030
scoreboard = get_links()['currentScoreboard']
games = get(BASE_URL + scoreboard).json()['games']

root = Tk()
root.title('Learn To Code at Codemy.com')

alto=420
ancho=420
anchoalto="420x420"
root.geometry(anchoalto)
# Create A Main Frame
main_frame = Frame(root,width=ancho,height=alto)
main_frame.place(x=0,y=0)
# Create A Canvas
my_canvas = Canvas(main_frame, width=ancho, height=alto)
my_canvas.place(x=0,y=0)
# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.place(x=605,y=0,height=alto)
# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas,width=ancho,height=alto)
second_frame.place(x=0,y=0)
# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

posY=0
altura = 0

for thing in range(100):
    posY = posY + 30
    altura = altura + 30
    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']
        
        guiones = Label(second_frame, text=f"{home_team['triCode']} vs {away_team['triCode']}\n{home_team['score']} - {away_team['score']}\n{period['current']} - {clock}",
        font=('Arial', 25, 'bold'),
        relief = RAISED,
        bd=6,
        padx=20,
        pady=20,
        justify=CENTER)
        guiones.place(relx= 0.5, rely= n, anchor=N)
        n+= 0.45
        guiones.place(x=50,y=posY)
    second_frame.configure(height=altura) #Changing the height of the second_frame each time a button is added

root.mainloop()