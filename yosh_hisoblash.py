
"""
Sana: 01-01-2023
Mavzu: Yoshni hisoblash DASTURI
Kanal: @sunnatjonpy

"""
from datetime import datetime 
from tkinter import *
oyna =Tk()
oyna.title("YOSHNI HISOBLAGICH")
oyna.geometry("400x400")

titlee = Label(text="Yosh  Hisoblagich",font="Stencil 12")
titlee.pack()


yil_text = Label(text="Tug'ilgan yil:👇🏻")
yil_text.place(x=145,y=35,width="110",height="30")


yil = Entry()
yil.place(x=160,y=70,width="80",height="30")

def hisobla():
    bugun = datetime.today()
    natija.config(text=f"Siz {bugun.year-int(yil.get())} yoshdasiz! ")
    
hisob = Button(text="Hisoblash",command=hisobla,bg="beige")
hisob.place(x=140,y=120,width="120",height="50")


natija = Label(text="Natija", bg="white")
natija.place(x=140,y=180,width="120",height="40")





oyna.mainloop()