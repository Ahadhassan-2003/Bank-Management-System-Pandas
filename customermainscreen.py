from tkinter import *
from tkinter import messagebox
from pandas import *
from numpy import *
from random import *
from customer_login import customerindex
        
def goback():
    main.destroy()
    import customer_login

def withdrawl():
    def withdrawl_click():
        indice = customerindex()
        input = int(amount.get())
        df = read_csv("clientaccounts.csv")
        AC_balance = df.loc[indice,'Balance'].values #checking sender balance
        if (input < 0): #Flag for checking that inputed amount is not neagtive
            Label(window,text="INVALID AMOUNT",font=("Arial",13),fg="RED",bg="#181D31",padx=12,pady=5).place(x=130,y=120)
        elif (AC_balance < input): #Checking if enough funds are present for transfer
            Label(window,text="INSUFFICIENT AMOUNT",font=("Arial",13),fg="RED",bg="#181D31",padx=12,pady=5).place(x=100,y=120)
        elif (df.loc[indice,'Status'].values=='BLOCKED'):
            Label(window,text="YOUR ACCOUNT IS BLOCKED",font=("Arial",13),fg="red",bg="#181D31",padx=12,pady=5).place(x=70,y=120)



        else:
            df.loc[indice,'Balance'] -= input
            df.to_csv("clientaccounts.csv",index=False)
            Label(window,text="WITHDRAWL SUCCESSFUL",font=("Arial",13),fg="GREEN",bg="#181D31",padx=12,pady=5).place(x=90,y=120)
    window=Tk()
    window.title("WITHDRAWL")
    window.geometry('400x200')
    window.configure(bg="#181D31")
    withdraw=Label(window,text="ENTER AMOUNT TO WITHDRAW:",font=("Tw Cen MT",12,"bold"),fg="#F0E9D2",bg="#181D31").place(x=100,y=20)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=87,y=40)
    amount=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Tw Cen MT",12,"bold"))
    amount.place(x=177,y=80)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=87,y=100)
    but_withdraw=Button(window,text="WITHDRAW",bg="lightgrey",command=withdrawl_click).place(x=168,y=150)
    window.mainloop()
def current():
    df = read_csv("clientaccounts.csv")
    indice = customerindex()
    balance = df.loc[indice,'Balance'].values
    window=Tk()
    window.title("CURRENT BALANCE")
    window.geometry('400x200')
    window.configure(bg="#181D31")
    l1=Label(window,text="YOUR CURRENT BALANCE IS:",font=("Tw Cen MT",16,"bold"),bg="#181D31",fg="#F0E9D2").place(x=10,y=10)
    Frame(window,width=300,height=2,bg="#F0E9D2").place(x=10,y=35)
    l2 = Label(window,text=(str(int(balance)),'PKR'),font="20",bg="#181D31",fg="#F0E9D2").place(x=150,y=90)
    Frame(window,width=150,height=2,bg="#F0E9D2").place(x=130,y=120)
    b1=Button(window,text="      CLOSE    ",bg="lightgrey",activebackground="green",activeforeground="white",command=window.destroy).place(x=168,y=150)
    window.mainloop()
def fund():
    def fund_click():
        df = read_csv("clientaccounts.csv")
        ACno = int(account.get())
        amount = int(money.get())
        from_indice = customerindex()
        to_indice = df[df['Account No.'] == ACno].index.values
        balance = df.loc[from_indice,'Balance'].values
        if (ACno in df['Account No.'].values):
            if (amount < 0):
                Label(window,text="INVALID AMOUNT",font=("Arial",13),fg="red",bg="#181D31",padx=12,pady=5).place(x=70,y=150)
            elif (balance < amount):
                Label(window,text="INSUFFICIENT BALANCE",font=("Arial",13),fg="red",bg="#181D31",padx=12,pady=5).place(x=70,y=150)
            elif (df.loc[indice,'Status'].values=='BLOCKED'):
                Label(window,text="YOUR ACCOUNT IS BLOCKED",font=("Arial",13),fg="red",bg="#181D31",padx=12,pady=5).place(x=70,y=150)
            else:
                df.loc[from_indice,'Balance'] -= amount
                df.loc[to_indice,'Balance'] += amount
                df.to_csv("clientaccounts.csv",index=False)     
                Label(window,text="TRANSFER SUCCESSFUL",font=("Arial",13),fg="green",bg="#181D31",padx=12,pady=5).place(x=80,y=150)
        else:
            Label(window,text="INVALID ACC NO.",font=("Arial",13),fg="red",bg="#181D31",padx=12,pady=5).place(x=120,y=150)
    window = Tk()
    window.configure(bg="#181D31")
    window.title("FUND TRANSFER")
    window.geometry('400x200')
    account=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Arial",12))
    account.place(x=165,y=20)
    accountno=Label(window,text="Acc no:",fg="#F0E9D2",bg="#181D31",font=("Arial",12)).place(x=100,y=20)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=40)
    moneytext=Label(window,text="Amount:",fg="#F0E9D2",bg="#181D31",font=("Arial",12)).place(x=100,y=60)
    money=Entry(window,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Arial",12))
    money.place(x=165,y=60)
    Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=80)
    but_transfer=Button(window,text="SEND MONEY",bg="#F0E9D2",activebackground="green",activeforeground="white",command=fund_click).place(x=150,y=120)
    window.mainloop()


df = read_csv("clientaccounts.csv")
indice = customerindex()
name = df.loc[indice,'Name'].values
acno=df.loc[indice,'Account No.'].values
main=Toplevel() 
main.title("CLIENT ACCOUNT")
main.maxsize(500,720)
main.minsize(500,720)
background_img=PhotoImage(file="bg4.png")
background=Label(main,image=background_img).place(x=0,y=0)
main.configure(bg="white")
main.resizable(False,False)
img=PhotoImage(file="customer.png")
label = Label(main,image=img,bg="#181D31").place(x=20,y=20)
Label(main,text=(''.join(name)),font=("Tw Cen MT",35,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=120,y=30)
Label(main,text=('Account no: '+str(acno[0])),font=("Tw Cen MT",15,"bold"),fg="#E6DDC4",bg="#181D31",padx=12,pady=5).place(x=120,y=80)
fundt=PhotoImage(file="transfer.png")
fundpic=Label(main,image=fundt,bg="#F0E9D2").place(x=120,y=409)
trans=PhotoImage(file="transaction.png")
transpic=Label(main,image=trans,bg="#F0E9D2").place(x=120,y=347)
currbal=PhotoImage(file="currentbalance.png")
curbalpic=Label(main,image=currbal,bg="#F0E9D2").place(x=120,y=278)
button_currentbalance=Button(main,text=" CURRENT BALANCE",bg="#181D31",fg="#F0E9D2",font=("Tw Cen MT",15,"bold"),activebackground="green",activeforeground="white",command=current).place(x=180,y=300)
button_fundtransfer=Button(main,text="  FUNDS TRANSFER ",bg="#181D31",fg="#F0E9D2",font=("Tw Cen MT",15,"bold"),activebackground="green",activeforeground="white",command=fund).place(x=180,y=430)
button_transaction=Button(main,text=   "       WITHDRAWL      ",bg="#181D31",fg="#F0E9D2",font=("Tw Cen MT",15,"bold"),activebackground="green",activeforeground="white",command=withdrawl).place(x=180,y=365)

backarrow=PhotoImage(file="backdark.png")
back_button=Button(main,image=backarrow,bg="#F0E9D2",command=goback).place(x=10,y=630)
main.mainloop()