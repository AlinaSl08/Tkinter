from tkinter import *

root = Tk()
root.title("Тестовое приложение")
root.geometry("1280x720")
root.resizable(width=False, height=False)

root["bg"] = "black"


def add():
    e.insert(END, "Hello")

def dele():
    e.delete(0, END)

def get():
    label1["text"] = e.get()

#виджет ввода
e = Entry(root, show="*")
e.pack()


btn1 = Button(root, font="Arial 15", text="Insert", command=add)
btn1.pack()

btn2 = Button(root, font="Arial 15", text="Delete", command=dele)
btn2.pack()

btn3 = Button(root, font="Arial 15", text="Get", command=get)
btn3.pack()

label1 = Label(root, bg="black", fg="white")
label1.pack()


root.mainloop()
