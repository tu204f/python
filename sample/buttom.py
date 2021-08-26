from tkinter import *

def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")

lbl = Label(window,text="Привет",font=("Arial Bold",50))
lbl.grid(column=0,row=0)

txt = Entry(window,width=10)
txt.grid(column=1,row=0)

btn = Button(window, text="Не нажимать!", bg="black", fg="red", command=clicked)
btn.grid(column=2,row=0)

window.geometry('400x250')
window.mainloop()