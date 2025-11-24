import sqlite3
con = sqlite3.connect('BANK.db')
cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS ACCOUNTING('
               'ADHAAR_NUMBER CHAR(12) NOT NULL,'
               'NAME VARCHAR(256) NOT NULL,'
               'AGE INT NOT NULL,'
               'GENDER CHAR(1) NOT NULL,'
               'PHONE_NUMBER CHAR(10) NOT NULL,'
               'BALANCE INT DEFAULT 0)')

con.commit()

def account_Creation():
    name=input("Enter the name of account holder: ")
    age=int(input('Enter the age: '))
    gender=input("Enter the sex: ")
    phone_number=int(input("Enter the phone number: "))
    ten=str(phone_number)
    if len(ten)==10:
        adhaar_number=input('Enter your adhaar number: ')
        cursor.execute("SELECT * FROM ACCOUNTING WHERE ADHAAR_NUMBER=?", (adhaar_number,))
        if cursor.fetchone():
            print("Account already exists with this adhaar!")
        else:
            sql='INSERT INTO ACCOUNTING VALUES(?,?,?,?,?,?)'
            values=(adhaar_number,name,age,gender,ten,0)
            cursor.execute(sql,values)
            con.commit()
            print('Account created.....')
    else:
        print("Phone number must be 10 digits!")

def deposit():
    adhaar=input("Enter adhaar number: ")
    cursor.execute("SELECT NAME,BALANCE FROM ACCOUNTING WHERE ADHAAR_NUMBER=?", (adhaar,))
    data=cursor.fetchone()
    if data:
        name,bal=data
        amt=int(input("Enter amount to deposit: "))
        newbal=bal+amt
        cursor.execute("UPDATE ACCOUNTING SET BALANCE=? WHERE ADHAAR_NUMBER=?", (newbal,adhaar))
        con.commit()
        print("Amount deposited successfully!")
        print("New balance:",newbal)
    else:
        print("Account not found!")

def withdraw():
    adhaar=input("Enter adhaar number: ")
    cursor.execute("SELECT NAME,BALANCE FROM ACCOUNTING WHERE ADHAAR_NUMBER=?", (adhaar,))
    data=cursor.fetchone()
    if data:
        name,bal=data
        amt=int(input("Enter amount to withdraw: "))
        if amt<=bal:
            newbal=bal-amt
            cursor.execute("UPDATE ACCOUNTING SET BALANCE=? WHERE ADHAAR_NUMBER=?", (newbal,adhaar))
            con.commit()
            print("Amount withdrawn successfully!")
            print("Remaining balance:",newbal)
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    adhaar=input("Enter adhaar number: ")
    cursor.execute("SELECT NAME,BALANCE FROM ACCOUNTING WHERE ADHAAR_NUMBER=?", (adhaar,))
    data=cursor.fetchone()
    if data:
        name,bal=data
        print("Account holder:",name)
        print("Current balance:",bal)
    else:
        print("Account not found!")

user='Abhi'
pswd='1234'

username=input('enter the username: ')
password=input('enter the password: ')

if username==user:
    if password==pswd:
        print("Welcome to banking system")
        while True:
            print("What u want to do? \n 1. Open a bank account \n2. deposite money \n 3. withdraw money \n 4. check balance \n 5. exit")
            choice=int(input('enter your choice: '))
            if choice==1:
                account_Creation()
            elif choice==2:
                deposit()
            elif choice==3:
                withdraw()
            elif choice==4:
                check_balance()
            elif choice==5:
                print('Exiting...')
                break
            else:
                print("Wrong choice")
    else:
        print("Wrong password")
else:
    print("Wrong username")

con.close()