from tkinter import *
from tkinter import messagebox
from pandas import *
from numpy import *
from random import *
def unblockclicked():
    df = read_csv("clientaccounts.csv")
    ACno = int(ac_number.get())
    if (ACno in df['Account No.'].values):
        indice = df[df['Account No.'] == ACno].index.values
        df.loc[indice,'Status'] = 'UNBLOCKED'
        df.to_csv("clientaccounts.csv",index=False)
        Label(root,text='ACCOUNT UNBLOCKED   ',fg="green",bg="#181D31",font=("Tw Cen MT",15)).place(x=98,y=180)
    else:
        Label(root,text='ACCOUNT NOT FOUND',fg="red",bg="#181D31",font=("Tw Cen MT",15)).place(x=98,y=180)
def button_input():
    df = read_csv("clientaccounts.csv")
    ACno = int(ac_number.get())
    if (ACno in df['Account No.'].values):
        indice = df[df['Account No.'] == ACno].index.values
        df.loc[indice,'Status'] = 'BLOCKED'
        df.to_csv("clientaccounts.csv",index=False)
        Label(root,text='     ACCOUNT BLOCKED   ',fg="green",bg="#181D31",font=("Tw Cen MT",15)).place(x=98,y=180)
    else:
        Label(root,text='ACCOUNT NOT FOUND',fg="red",bg="#181D31",font=("Tw Cen MT",15)).place(x=98,y=180)
       
root=Tk()
root.configure(bg="#181D31")

root.maxsize(400,250)
root.minsize(400,250)

Label(root,text="Enter Account Number",font=("Tw Cen MT",18,"bold"),bg="#181D31",fg="#F0E9D2").place(x=20,y=16)
Frame(root,width=230,height=2,bg="#F0E9D2").place(x=17,y=50)

ac_number=Entry(root,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Tw Cen MT",12,"bold"))
ac_number.place(x=150,y=100)
Frame(root,width=250,height=2,bg="#F0E9D2").place(x=82,y=120)
block_but=Button(root,text="BLOCK",bg="#F0E9D2",fg="#181D31",command=button_input).place(x=128,y=150)
unblock_but=Button(root,text="UNBLOCK",bg="#F0E9D2",fg="#181D31",command=unblockclicked).place(x=208,y=150)
root.mainloop()