from tkinter import *
from tkinter import messagebox
from random import *
from turtledemo.chaos import coosys

clicks = 0

def randomize():
    global clicks
    btnClick.place(x=randint(70, 1000), y = randint(70, 650))
    clicks += 1
    labelClick["text"] = str(clicks)
    labelClick.pack()



root = Tk()
root.title("Кликер")
root.geometry("1280x720")
root.resizable(width=False,height=False)

root["bg"] = "black"

labelClick = Label(root, text="0", font="Arial 30", bg='black', fg="white")
labelClick.pack()


btnClick = Button(root,
                  text="Click",
                  bg = "lime",
                  fg = "black",
                  padx=20,
                  pady = 8,
                  font ="Arial 13",
                  command=randomize)

btnClick.place(x=randint(70, 1000), y = randint(70, 650))


root.mainloop()
