from tkinter import *

def manager():
   
    import manager
    

def customer():

    import customer_login

def accountant():
    
    import accountant_login
root=Tk()

root.maxsize(500,720)
root.minsize(500,720)

bgimage=PhotoImage(file="bg.png")
Label(root,image=bgimage).place(x=0,y=0)


b1=Button(root,text="Manager",font=("Tw Cen MT",25,"bold"),padx=17,fg="#181D31",bg="#F0E9D2",activebackground="#678983",activeforeground="#F0E9D2",relief=GROOVE,command=manager)
b1.place(x=150,y=310)

b2=Button(root,text="Accountant",font=("Tw Cen MT",25,"bold"),fg="#181D31",bg="#F0E9D2",activebackground="#678983",activeforeground="#F0E9D2",relief=GROOVE,command=accountant)
b2.place(x=150,y=420)

b3=Button(root,text="Customer",font=("Tw Cen MT",25,"bold"),padx=15,fg="#181D31",bg="#F0E9D2",activebackground="#678983",activeforeground="#F0E9D2",relief=GROOVE,command=customer)
b3.place(x=150,y=530)
root.mainloop()