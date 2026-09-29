from tkinter import *
from Modules import logic 
from Modules import Config

# Buttons, Widgets etc
root = Tk()  
root.geometry("500x500")
root.resizable(False, False)
root.title("Whack-a-Mole")
canvas=Canvas(root, width=500, height=500, bg="lightgreen")
canvas.grid()
l=Label(root, text="Whack A Mole", bg="green", fg='lightgreen')
var=StringVar()
l2=Label(root, bg="lightgreen", textvariable=var, padx=50)
var2=StringVar()
Timer=Label(root, bg='lightgreen', textvariable=var2, font=('Courier', 18, 'bold'))
Timer.place(x=400, y=50)
l.config(font=("Courier", 16))
l.place(x=170, y=5)
l2.place(x=150, y=30)
l2.config(font=("Courier", 12))
Start=Button(root, text='Start', fg='black', bg='white', font='Courier', command=logic.start, height=3, width=7)
Start.place(x=215, y=220)
#--------------
logic.root = root
logic.canvas = canvas
logic.var = var
logic.var2 = var2
logic.Start = Start
# For the Close button
root.protocol("WM_DELETE_WINDOW", logic.close)
root.mainloop()