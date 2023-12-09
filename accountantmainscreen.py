from tkinter import *
from tkinter import messagebox
from pandas import *
from numpy import *
from random import *
from accountant_login import accountantindex

def changepassword():
    import changepassword
def deposit():
    def deposit_clicked():
        df=read_csv("clientaccounts.csv")
        acno=int(ac_number.get())
        amm=int(amount.get())
        indice=df[df['Account No.']==acno].index.values
        if (df.loc[indice,'Status'].values=='BLOCKED'):
            Label(window,text="THIS ACCOUNT IS BLOCKED",font=("Arial",13),fg="red",bg="#181D31",padx=12,pady=5).place(x=70,y=180)
        elif (amm < 0): #Flag for checking that inputed amount is not neagtive
            Label(window,text="INVALID AMOUNT",font=("Arial",13),fg="RED",bg="#181D31",padx=12,pady=5).place(x=130,y=120)
        else:    
            df.loc[indice,'Balance']+=amm
            df.to_csv("clientaccounts.csv",index=False)
            Label(window,text="DEPOSIT SUCCESSFUL",fg="green",bg="#181D31",font=("Tw Cen MT",12,"bold")).place(x=98,y=180)

    window=Tk()
    window.geometry('400x250')
    window.configure(bg="#181D31")
    Label(window,text="Enter Acc no:",font=("Tw Cen MT",18,"bold"),bg="#181D31",fg="#F0E9D2").place(x=20,y=20)
    Frame(window,width=170,height=2,bg="#F0E9D2").place(x=17,y=50)

    ac_number=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Tw Cen MT",12,"bold"))
    ac_number.place(x=110,y=68)
    Frame(window,width=150,height=2,bg="#F0E9D2").place(x=82,y=92)

    Label(window,text="Enter Amount:",font=("Tw Cen MT",18,"bold"),bg="#181D31",fg="#F0E9D2").place(x=20,y=100)
    Frame(window,width=150,height=2,bg="#F0E9D2").place(x=17,y=130)

    amount=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Tw Cen MT",12,"bold"))
    amount.place(x=110,y=142)
    Frame(window,width=150,height=2,bg="#F0E9D2").place(x=82,y=162)
    deposit_but=Button(window,text="DEPOSIT",bg="#F0E9D2",fg="#181D31",command=deposit_clicked).place(x=156,y=220)

    window.mainloop()


def newaccount():
    import newaccount
def goback():
    ac_sc.destroy()

ac_sc=Toplevel()   
ac_sc.maxsize(500,720)
ac_sc.minsize(500,720)
indice=accountantindex()
df=read_csv("accountant_accounts.csv")
name=df.loc[indice,'Name'].values[0]
bgimage1=PhotoImage(file="bg4.png")
Label(ac_sc,image=bgimage1).place(x=0,y=0)

mgimage=PhotoImage(file="accountant.png")
Label(ac_sc,image=mgimage,bg="#181D31").place(x=20,y=20)

Label(ac_sc,text=name,font=("Tw Cen MT",35,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=120,y=30)
Label(ac_sc,text='ACCOUNTANT',font=("Tw Cen MT",15,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=120,y=80)

b1=Button(ac_sc,text="Cash Deposit",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",padx=30,activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE,command=deposit)
b1.place(x=130,y=230)

b2=Button(ac_sc,text=" Change Client Password",font=("Tw Cen MT",14,"bold"),fg="#F0E9D2",bg="#181D31",padx=10,activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE,command=changepassword)
b2.place(x=130,y=320)

b3=Button(ac_sc,text="Create an Account",font=("Tw Cen MT",20,"bold"),fg="#F0E9D2",bg="#181D31",activebackground="#181D31",activeforeground="#F0E9D2",relief=GROOVE,command=newaccount)
b3.place(x=130,y=410)

backarrow=PhotoImage(file="backlight.png")
back_button=Button(ac_sc,image=backarrow,bg="#181D31",command=goback).place(x=10,y=630)

ac_sc.mainloop()