from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Тестовое приложение")
root.geometry("500x500")

s = ttk.Style()

print(s.theme_names(), s.theme_use()) #вывести какие темы есть(по имени), узнать какая сейчас тема стоит(пустые скобки), либо в кавычках вписать нужную тему

s.configure('one.TButton', foreground="red", padding=20) #s.configure(название стиля, опции), '.' - меняет все виджеты ttk, 'TButton' - меняет кнопку, 'one.TButton' - только к 1 кнопке, ей назначаем style="one.TButton", padding=20(если нужна высота)


ttk.Button(root, text="Один", width=20, style="one.TButton").pack()
ttk.Button(root, text="Два", width=20).pack()  #нельзя менять высоту, только ширину и padx и pady не работают

Entry(root).pack()
ttk.Entry(root).pack()



root.mainloop()
