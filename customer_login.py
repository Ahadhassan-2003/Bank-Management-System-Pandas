from tkinter import *
from tkinter import messagebox
from pandas import *
from numpy import *
from random import *
def goback():
    mg.destroy()
def customerindex():
    username = user.get()
    password = passw.get()
    df = read_csv("clientaccounts.csv")
    index = df[df['Username'] == username].index.values
    return index

def login():
    username = user.get()
    password = passw.get()
    df = read_csv("clientaccounts.csv")
    username_indice = df[df['Username'] == username].index.values
    password_indice = df[df['Password'] == password].index.values
    if (username_indice == password_indice):
        import customermainscreen
    else:
        l1 = Label(mg,text="INVALID LOGIN",font=("Tw Cen MT",15),fg="RED",bg="#181D31",padx=12,pady=5).place(x=160,y=540)
mg=Toplevel()
mg.maxsize(500,700)
mg.minsize(500,700)
mg.title("SIGN IN AS CUSTOMER")
bgimage1=PhotoImage(file="bg 2.png")
Label(mg,image=bgimage1).place(x=0,y=0)

mgimage=PhotoImage(file="customer.png")
Label(mg,image=mgimage,bg="#181D31").place(x=200,y=180)

Label(mg,text="Log in as Customer",font=("Tw Cen MT",25,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=110,y=270)

user=Entry(mg,width=25,fg="#F0E9D2",border=0,bg="#181D31",font=("Ariel",12))
user.bind("<Button-1>",lambda e: user.delete(0,END))
user.place(x=130,y=350)
user.insert(0,"Username")
userimg=PhotoImage(file="username.png")
Label(mg,image=userimg,bg="#181D31").place(x=80,y=340)
Frame(mg,width=250,height=2,bg="#F0E9D2").place(x=130,y=370)

passw=Entry(mg,width=25,fg="#F0E9D2",border=0,bg="#181D31",font=("Ariel",12))
passw.bind("<Button-1>",lambda e: passw.delete(0,END))
passw.place(x=130,y=420)
passw.insert(0,"Password")
passimg=PhotoImage(file="password.png")
Label(mg,image=passimg,bg="#181D31").place(x=80,y=410)
Frame(mg,width=250,height=2,bg="#F0E9D2").place(x=130,y=440)
backarrow=PhotoImage(file="backlight.png")
back_button=Button(mg,image=backarrow,bg="#181D31",command=goback).place(x=10,y=630)
sub_button=Button(mg,text="Submit",font=("Tw Cen MT",15,"bold"),fg="#F0E9D2",bg="#678983",activebackground="#678983",activeforeground="#F0E9D2",relief=GROOVE,command=login)
sub_button.place(x=200,y=480)

Frame(mg,width=300,height=50,bg="#678983").place(x=220,y=640)
mg.mainloop()
