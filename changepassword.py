from tkinter import *
from tkinter import messagebox
from pandas import *
from numpy import *
from random import *
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class a:
    code=str(r.randint(100000,999999))
def checkemail():
    acno=int(Acno.get())
    enteredemail=email.get()
    df=read_csv('clientaccounts.csv')
    indice_mail = df[df['Email'] == enteredemail].index.values
    indice_acno = df[df['Account No.'] == acno].index.values
    if (indice_acno == indice_mail):
        Label(window,text="                  CODE SENT                       ",fg="green",bg="#181D31",font=("Arial",12)).place(x=80,y=230)
        sendmail()
    else:
        Label(window,text="WRONG EMAIL OR ACCOUNT NO",fg="red",bg="#181D31",font=("Arial",12)).place(x=80,y=230)
def sendmail():
            remail=email.get()
            smtp_user = 'amaanashraf222999@gmail.com'
            smtp_password = 'bmkebaddondkkgop'
            server = 'smtp.gmail.com'
            port = 587
            msg = MIMEMultipart("alternative")
            msg["Subject"] = 'DAULAT PAY'
            msg["From"] = smtp_user
            msg["To"] = remail
            msg.attach(MIMEText("Your OTP for Changing password is "+a.code+"\nPlease don't share this otp with anyone"))
            s = smtplib.SMTP(server, port)
            s.ehlo()
            s.starttls()
            s.login(smtp_user, smtp_password)
            s.sendmail(smtp_user, remail, msg.as_string())
            s.quit()
def changepassword():
    acno=int(Acno.get())
    enteredemail=email.get()
    sentcode = de.get()
    passw = password.get()
    df=read_csv('clientaccounts.csv')
    indice_acno = df[df['Account No.'] == acno].index.values
    indice_mail = df[df['Email'] == enteredemail].index.values
    if (sentcode != a.code):
        Label(window,text="             INVALID CODE               ",fg="red",bg="#181D31",font=("Arial",12)).place(x=90,y=230)
    else:
        df.loc[indice_acno,'Password'] = passw
        df.to_csv("clientaccounts.csv",index=False)
        Label(window,text="       CHANGE SUCCESSFUL          ",fg="green",bg="#181D31",font=("Arial",12)).place(x=80,y=230)

window=Tk()
window.configure(bg="#181D31")
window.geometry('400x300')
window.title("CHANGE ACCOUNT PASSWORD")
Acno=Entry(window,width=25,bg="#181D31",border=0,fg="#F0E9D2",font=("Ariel",12))
Acno.place(x=100,y=10)
Acno.bind("<Button-1>",lambda e: Acno.delete(0,END))
Acno.insert(0,"Account No")
email=Entry(window,width=25,bg="#181D31",border=0,fg="#F0E9D2",font=("Ariel",12))
email.bind("<Button-1>",lambda e: email.delete(0,END))
email.place(x=100,y=60)
email.insert(0,"Enter Your Email")
Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=80)
Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=30)
de=Entry(window,width=25,bg="#181D31",border=0,fg="#F0E9D2",font=("Ariel",12))
de.bind("<Button-1>",lambda e: de.delete(0,END))
Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=130)
de.insert(0,"Enter Code(sent to mail)")
but_change=Button(window,text="Change Pasword",fg="#181D31",bg="#F0E9D2",command=changepassword).place(x=150,y=200)
de.place(x=100,y=110)
password=Entry(window,width=25,bg="#181D31",border=0,fg="#F0E9D2",font=("Ariel",12))
password.bind("<Button-1>",lambda e: password.delete(0,END))
password.place(x=100,y=160)
password.insert(0,"Enter New Password")
Frame(window,width=250,height=2,bg="#F0E9D2").place(x=100,y=180)
sendcode=Button(window,text="send code",fg="#181D31",bg="#F0E9D2",command=checkemail).place(x=290,y=107)
window.mainloop()