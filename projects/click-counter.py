from tkinter import *

root = Tk()
root.title("Счетчик кликов")
root.geometry("200x200")
root.resizable(width=False, height=False)

count = 0


def clicked():
    global count
    count +=1
    click.configure(text=count)



click = Label(root, text="0", font="Arial 35")
click.pack()

bt = Button(root, text="Кликнуть", padx="20", pady="20", command=clicked)
bt.pack()


root.mainloop()