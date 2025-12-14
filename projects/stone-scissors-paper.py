from tkinter import *
from random import *

root = Tk()

root.title("Камень, ножницы, бумага")
root.geometry("600x400")
root.resizable(width=False, height=False)

root["bg"] = "black"


def Whyknb():
    knb = ['Камень', 'Ножницы', 'Бумага']
    value = choice(knb)
    labelText.configure(text=value)


labelText = Label(root, text="", fg = "white", font = ("Comic Sans MS", 20),  bg="black")
labelText.place(y = 150, x = 240) #вывод

stone = Button(root, text="Камень", font=("Comic Sans MS", 20), bg = "white", command=Whyknb)
stone.place(x=50, y=300)

scissors = Button(root, text="Ножницы", font=("Comic Sans MS", 20), bg = "white", command=Whyknb)
scissors.place(x=220, y=300)

paper = Button(root, text="Бумага", font=("Comic Sans MS", 20), bg = "white", command=Whyknb)
paper.place(x=420, y=300)

root.mainloop()
