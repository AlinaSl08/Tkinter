from tkinter import *
from datetime import datetime


temp = 0
after_id = ""

def tick():
    global temp, after_id
    after_id = root.after(1000, tick) #будет обновляться функция каждую секунду, тут 1000 = 1 сек
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.pack_forget() #кнопка скрывается после нажатия
    btnStop.pack()
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id) #остановка секундомера


def continue_tick():
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()


def reset_tick():
    global temp
    temp = 0
    label1.configure(text="00:00")
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()

root = Tk()
root.title("Секундомер")
root.geometry("300x200")
root.resizable(width=False, height=False)

label1 = Label(root, width=10, font=("Comic Sans MS", 30), text="00:00")
label1.pack()


btnStart = Button(root, text="Старт", font=("Comic Sans MS", 20), width=15, command=start_tick)
btnStop = Button(root, text="Стоп", font=("Comic Sans MS", 20), width=15, command=stop_tick)
btnContinue = Button(root, text="Продолжить", font=("Comic Sans MS", 20), width=15, command=continue_tick)
btnReset = Button(root, text="Сброс", font=("Comic Sans MS", 20), width=15, command=reset_tick)

btnStart.pack()


root.mainloop()
