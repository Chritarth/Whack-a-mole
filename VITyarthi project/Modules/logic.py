from tkinter import messagebox
import random
from Modules import Config
#Game Timer
def countdown(g1):
    if Config.cl==50:
        return
    Config.time=int(Config.time)
    if Config.time>=0:
        mins,secs=divmod(Config.time,60)
        var2.set(f'{mins:02d}:{secs:02d}')
        Config.time=Config.time-1
        Config.countdown_id=root.after(1000, countdown,Config.time)
    else:
        autoclose()
#Timer to determine time to whack the mole
def timer():
    if Config.cl==50:
        return
    else:
        Config.time_id=root.after(max(200, 1000 - (Config.diff * 100)),pos)
#Position randomizer(moves every object to create a mole)
def pos():
    x2,y2=random.choice(Config.Hole_pos)
    canvas.moveto(Config.mole,x2,y2)
    canvas.moveto(Config.mole_eye1,x2+30,y2)
    canvas.moveto(Config.mole_eye2,x2+50,y2)
    canvas.moveto(Config.mole_snout,x2+10,y2+30)
    timer()
    return x2,y2
#Score Calculation
def score(event):
    root.after_cancel(Config.time_id)
    Config.score1+=1
    if Config.score1%5==0:
        Config.diff+=1
    var.set(f"Score = {Config.score1}")
    pos()
#on pressing Start button
def start():
    PlaceHoles()
    timer()
    Start.destroy()
    countdown(Config.time)
#On closing the window while the game is running
def close():
    Config.cl=50
    if messagebox.askokcancel("Quit", "Are you sure you want to exit while the game is running"):
        root.destroy()
    else:
        Config.cl=0
        countdown(Config.time)
#Places Holes after start is pressed
def PlaceHoles():
    canvas.create_oval(2,140,150,180, fill="black",outline="white",width=2)
    canvas.create_oval(172,140,320,180, fill="black",outline="white",width=2)
    canvas.create_oval(342,140,490,180, fill="black",outline="white",width=2)
    canvas.create_oval(2,240,150,280, fill="black",outline="white",width=2)
    canvas.create_oval(172,240,320,280, fill="black",outline="white",width=2)
    canvas.create_oval(342,240,490,280, fill="black",outline="white",width=2)
    canvas.create_oval(2,340,150,380, fill="black",outline="white",width=2)
    canvas.create_oval(172,340,320,380, fill="black",outline="white",width=2)
    canvas.create_oval(342,340,490,380, fill="black",outline="white",width=2)
    canvas.create_oval(2,440,150,480, fill="black",outline="white",width=2)
    canvas.create_oval(172,440,320,480, fill="black",outline="white",width=2)
    canvas.create_oval(342,440,490,480, fill="black",outline="white",width=2)
    Config.mole=canvas.create_arc(202,350,300,480,extent=180, fill="brown",outline="black",width=2)
    Config.mole_snout=canvas.create_oval(202,202,240,220,fill='pink',outline='black',width=2)
    Config.mole_eye1=canvas.create_line(0,0,0,22,fill='black',width=4)
    Config.mole_eye2=canvas.create_line(0,0,0,22,fill='black',width=4)
    canvas.moveto(Config.mole,197,390)
    canvas.moveto(Config.mole_snout,207,420)
    canvas.moveto(Config.mole_eye1,227,390)
    canvas.moveto(Config.mole_eye2,247,390)
    canvas.tag_bind(Config.mole,"<Button-1>",score)
    canvas.tag_bind(Config.mole_snout,"<Button-1>",score)
    canvas.tag_bind(Config.mole_eye1,"<Button-1>",score)
    canvas.tag_bind(Config.mole_eye2,"<Button-1>",score)
#to close the game when timer ends
def autoclose():
    root.after_cancel(Config.time_id)
    root.after_cancel(Config.countdown_id)
    if messagebox.showinfo("Time's up",f"Thanks for playing, Your score: {Config.score1}"):
        root.destroy()
