from tkinter import *

root = Tk()
root.title("Тестовое приложение")
root.geometry("500x500")
root.resizable(width=False, height=False)


def open_win():
    win = Toplevel() #попап
    win.geometry("200x200+300+300") #+300+300 это от 300 пикселей вправо от угла(левого) и на 300 пикселей вниз(от верхнего)
    win.grab_set() #нельзя закрыть основное окно, пока не закроем дочернее
    l = Label(win, text="Toplevel", font="Arial 15 bold", fg="brown").pack()
    win.overrideredirect(1) #убирает title и возможность закрыть окно через крестик
    win.after(3000, lambda:win.destroy()) #закрывается спустя кол-во секунд

btn = Button(root, text="Открыть", padx=40, pady=5, command=open_win).place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
