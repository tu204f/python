from tkinter import *

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
lbl = Label(window,text="Привет",font=("Arial Bold",50))
lbl.grid(column=0,row=0)
window.geometry('400x250')
window.mainloop()