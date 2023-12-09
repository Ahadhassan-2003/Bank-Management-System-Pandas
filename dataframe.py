from pandas import *
from numpy import *
from tkinter import *
from random import *
from numpy import *

#------------------------------------------ All Functions ---------------------------------------------------------

class a:
    accounttype = str

def accountselection(): #Function for account selection
    a.accounttype = input("Which type of account do you want to open:\n1: BASIC\n2: CURRENT\n3: SAVINGS\n4: FOREIGN CURRENCY\n5: FIXED DEPOSITS\n?")
    match (a.accounttype):
        case '1': a.accounttype = 'BASIC'
        case '2': a.accounttype = 'CURRENT'
        case '3': a.accounttype = 'SAVINGS'
        case '4': a.accounttype = 'FOREIGN CURRENCY'
        case '5': a.accounttype = 'FIXED DEPOSITS'
        case _: print("INVALID INPUT! TRY AGAIN!"),accountselection()

def newaccount(): #Function for creating a new account
    ACno = randint(100000,999999) #Random account number generation
    accountselection()
    dict1 = { #Creation of a dictionary for producing new rows/accounts
    'Account No.':[ACno],
    'Name':[input("Please enter your name: ")],
    'Password':[input("Please enter a strong password: ")],
    'Accounttype':[a.accounttype],
    'Balance': [0],
    'CNIC':[input("Please enter your CNIC: ")],
    'Mobile#':[input("Please enter your phone number: ")]
    }
    df = DataFrame.from_dict(dict1).set_index('Account No.')#Creation of DataFrame with dictionary
    df.to_csv("clientaccounts.csv",mode='a',header=False) #Storing the DataFrame in csv while ignoring headers i.e 'Name','Password' of the dictionary
    print("\n\t\t\tCONGRATULATIONS!!\n\t\t YOUR ACCOUNT HAS BEEN CREATED\n")
    print(f"\t\t  YOUR ACCOUNT NO. IS: {ACno} \n")
    print("PLEASE SAVE/REMEBER THIS AS YOU WILL BE NEEDING THIS FOR YOUR TRANSACTIONS\n")

def deposit(): #Function for depositing cash in an account
    ACno = int(input("Please enter the Account Number for deposit: ")) #Input of account number
    amount = int(input("Enter the amount you want to deposit: ")) #Input of amount being deposited
    df = read_csv("clientaccounts.csv") #importing csv file into a dataframe
    indice = df[df['Account No.'] == ACno].index.values #Code in outer [] returns a Series of True/false/bool, checking all columns for the value while the full line returns the index value of the account number
    df.loc[indice,'Balance'] += amount #Addding amount
    df.to_csv("clientaccounts.csv",index=False) #Writing changed values in the same csv file
    print("\n\t\tDEPOSIT SUCCESSFUL!!\n")

def funds_transfer():
    fromAC_no = int(input("Enter your account number (SENDER): ")) #Input of sender account number
    fromAC_pass = input("Enter your account password: ") #Input of sender password

    df = read_csv("clientaccounts.csv") #Import csv file to a variable

    indice_fromAC_no = df[df['Account No.'] == fromAC_no].index.values #Code in outer [] returns a Series of True/false/bool, checking all columns for the value while the full line returns the index value of the account number
    indice_fromAC_pass = df[df['Password'] == fromAC_pass].index.values #Code in outer [] returns a Series of True/false/bool, checking all columns for the value while the full line returns the index value of the password
    
    if (indice_fromAC_no == indice_fromAC_pass): #Condition for checking if password is correct or not
        print("\n\t\tPASSWORD VALID!\n")
        toAC_no = int(input("Enter the Account No. to which you want to tansfer your amount (RECEIVER): ")) #Input reciever account number 
        indice_toAC_no = df[df['Account No.'] == toAC_no].index.values #Code in outer [] returns a Series of True/false/bool, checking all columns for the value while the full line returns the index value of the account number
        amount = int(input("Enter the amount that you want to transfer: ")) #Input  amount
        AC_balance = df.loc[indice_fromAC_no,'Balance'].values #checking sender balance
        if (amount < 0): #Flag for checking that inputed amount is not neagtive
            print("\n\t\tINVALID AMOUNT!\n")
        elif (AC_balance < amount): #Checking if enough funds are present for transfer
            print("\t\tINSUFFICIENT FUNDS IN YOUR ACCOUNT!\n")
        else:
            df.loc[indice_fromAC_no,'Balance'] -= amount
            df.loc[indice_toAC_no,'Balance'] += amount
            df.to_csv("clientaccounts.csv",index=False)
            print("\n\t\tTRANSFER SUCCESSFUL!!\n")
    else:
        print("\n\t\tINVALID ACCOUNT NO. OR PASSWORD\n")

def withdrawl():
    ACno = int(input("Please enter the Account Number for withdrawl: ")) #Input of account number
    amount = int(input("Enter the amount you want to withdrawl: ")) #Input of amount being deposited
    df = read_csv("clientaccounts.csv") #importing csv file into a dataframe
    indice = df[df['Account No.'] == ACno].index.values #Code in outer [] returns a Series of True/false/bool, checking all columns for the value while the full line returns the index value of the account number
    AC_balance = df.loc[indice,'Balance'].values #checking sender balance
    if (amount < 0): #Flag for checking that inputed amount is not neagtive
        print("\n\t\tINVALID AMOUNT!\n")
    elif (AC_balance < amount): #Checking if enough funds are present for transfer
        print("\t\tINSUFFICIENT FUNDS IN YOUR ACCOUNT!\n")
    else:
        df.loc[indice,'Balance'] -= amount
        df.to_csv("clientaccounts.csv",index=False)
        print("\n\t\tWITHDRAWL SUCCESSFUL!!\n")

def mainmenu():
    print("\t\t\tWELCOME TO 'TRIPLE A' BANK MANAGEMENT SYSTEM")
    print("------------------------------------------------------------------------------------------------------\n")
    select = input(("1: Sign in as Admin\n2: Sign in as Accountant\n3: Sign in as Client\nInput your choice: "))
    match (select):
        case '1': manager_signin()
        case '2': accountant_signin()
        case '3': clientaccount()
        case _: print("INVALID INPUT!"),mainmenu()

def manager_signin():
    username = input("Please input your username: ")
    password = input("Please enter your password: ")

    df = read_csv('adminaccounts.csv')
    
    indice_username = df[df['Username'] == username].index.values
    indice_password = df[df['Password'] == password].index.values
    print(indice_username,indice_password)
    if (indice_username == indice_password or indice_username.size != 0 or indice_password != 0):
        print("\n\t\tPASSWORD VALID!\n")
    else:
        print("\n\t\tINVALID USERNAME OR PASSWORD\n")
        while(True):
            select = input("1: Re-enter username and password\n2: Go back to mainmenu:\nInput your choice: ")
            if (select == '1'):
                manager_signin()
                break
            elif (select == '2'):
                mainmenu()
                break
            else:
                print("\nINVALID INPUT!\n")

def accountant_signin():
    username = input("Please input your username: ")
    password = input("Please enter your password: ")

    df = read_csv('adminaccounts.csv')
    
    indice_username = df[df['Username'] == username].index.values
    indice_password = df[df['Password'] == password].index.values
    print(indice_username,indice_password)
    if (indice_username == indice_password or indice_username.size != 0 or indice_password != 0):
        print("\n\t\tPASSWORD VALID!\n")
    else:
        print("\n\t\tINVALID USERNAME OR PASSWORD\n")
        while(True):
            select = input("1: Re-enter username and password\n2: Go back to mainmenu:\nInput your choice: ")
            if (select == '1'):
                accountant_signin()
                break
            elif (select == '2'):
                mainmenu()
                break
            else:
                print("\nINVALID INPUT!\n")

def clientaccount():
    pass

deposit()