from tkinter import *
from pandas import *




def deleteaccount():
    df = read_csv("clientaccounts.csv")
    ACno = int(ac_number.get())
    indice = df[df['Account No.'] == ACno].index.values
    df.drop(indice,axis=0,inplace=True)
    df.to_csv("clientaccounts.csv",index=False)
    Label(root,text='ACCOUNT DELETED',fg="red",bg="#181D31",font=("Tw Cen MT",15,"bold")).place(x=98,y=180)
root=Tk()
root.configure(bg="#181D31")

root.maxsize(400,250)
root.minsize(400,250)

Label(root,text="Enter Account Number",font=("Tw Cen MT",18,"bold"),bg="#181D31",fg="#F0E9D2").place(x=20,y=16)
Frame(root,width=230,height=2,bg="#F0E9D2").place(x=17,y=50)

ac_number=Entry(root,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Tw Cen MT",12,"bold"))
ac_number.place(x=110,y=68)
Frame(root,width=250,height=2,bg="#F0E9D2").place(x=82,y=92)

Label(root,text="Enter Name",font=("Tw Cen MT",18,"bold"),bg="#181D31",fg="#F0E9D2").place(x=20,y=100)
Frame(root,width=130,height=2,bg="#F0E9D2").place(x=17,y=130)

ac_name=Entry(root,width=20,fg="#F0E9D2",border=0,bg="#181D31",font=("Tw Cen MT",12,"bold")).place(x=110,y=148)
Frame(root,width=250,height=2,bg="#F0E9D2").place(x=82,y=172)

block_but=Button(root,text="DELETE",bg="#F0E9D2",fg="#181D31",command=deleteaccount).place(x=168,y=200)
root.mainloop()