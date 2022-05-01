from tkinter import *
from turtle import color, width

from sqlalchemy import Integer

window = Tk()
window.geometry('600x400')
window.title('printing')
Label(window,text="welcome to my 1st screen",font="Arial 14 underline", background="pink", justify="left").pack()
name= IntVar()
name1= IntVar()
a=IntVar()
Entry(window,textvariable=name,width="70",background="black").pack()
Entry(window,textvariable=name1,width="70",background="black").pack()

def myfunc():
    a=( name.get() + name1.get() )
    print(a)
    
Button(window,text="Calculate",activebackground="red",activeforeground="blue",bg="pink",command=myfunc).pack()
window.mainloop()