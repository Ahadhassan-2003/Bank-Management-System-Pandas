from tkinter import *
from tkinter import messagebox
from pandas import *
from numpy import *
from random import *


def goback():
    newac.destroy()

def submit_but():
    Name = name.get()
    username = user.get()
    password = passw.get()
    id = cnic.get()
    mobile = phno.get()
    dict1 = { #Creation of a dictionary for producing new rows/accounts
    'Name':[Name],
    'Username':[username],
    'Password':[password],
    'CNIC':[id],
    'Mobile#':[mobile]
    }
    df = read_csv("accountant_accounts.csv")
    if (username in df['Username'].values):
        Label(newac,text="Username Taken",padx=100,font=("Tw Cen MT",15),fg="red",bg="#F0E9D2").place(x=80,y=520)
    elif (len(id)!=13):
        Label(newac,text="       Invalid CNIC no.                   ",font=("Tw Cen MT",15),fg="red",bg="#F0E9D2").place(x=150,y=520)
    elif (len(mobile)!=10):
        Label(newac,text="      Invalid Mobile No.             ",font=("Tw Cen MT",15),fg="red",bg="#F0E9D2").place(x=150,y=520)
    else:
        df = DataFrame.from_dict(dict1).set_index('Name')#Creation of DataFrame with dictionary
        df.to_csv("accountant_accounts.csv",mode='a',header=False)
        Label(newac,text="Account Successfully Created",font=("Tw Cen MT",15),fg="green",bg="#F0E9D2").place(x=135,y=520)
newac=Toplevel()
newac.maxsize(500,720)
newac.minsize(500,720)

bgimage3=PhotoImage(file="bg3.png")
Label(newac,image=bgimage3).place(x=0,y=0)

Label(newac,text="Welcome",font=("Tw Cen MT",30,"bold"),fg="#181D31",bg="#F0E9D2").place(x=170,y=170)

name=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
name.bind("<Button-1>",lambda e: name.delete(0,END))
name.place(x=130,y=250)
name.insert(0,"Enter Name")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=270)

user=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
user.bind("<Button-1>",lambda e: user.delete(0,END))
user.place(x=130,y=300)
user.insert(0,"Enter Username")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=320)

passw=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
passw.bind("<Button-1>",lambda e: passw.delete(0,END))
passw.place(x=130,y=350)
passw.insert(0,"Create a Password")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=370)

cnic=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
cnic.bind("<Button-1>",lambda e: cnic.delete(0,END))
cnic.place(x=130,y=400)
cnic.insert(0,"Enter CNIC")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=420)

phno=Entry(newac,width=25,fg="#181D31",border=0,bg="#F0E9D2",font=("Ariel",12))
phno.bind("<Button-1>",lambda e: phno.delete(0,END))
phno.place(x=130,y=450)
phno.insert(0,"Enter Phone no")
Frame(newac,width=250,height=2,bg="#181D31").place(x=130,y=470)

backarrow=PhotoImage(file="backlight.png")
back_button=Button(newac,image=backarrow,bg="#181D31",command=goback).place(x=10,y=630)
sub_button=Button(newac,text="Submit",font=("Tw Cen MT",15,"bold"),fg="#F0E9D2",bg="#181D31",activebackground="#678983",activeforeground="#F0E9D2",relief=GROOVE,command=submit_but)
sub_button.place(x=200,y=550)

newac.mainloop()
