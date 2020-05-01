import User_database as user
from Employee_Database import *
import Employee_Functions as Efun

print("To gain access to the employee function, please log in and enter your username and password below\n")


verification=False
while True:

    if verification==False:
      login = input("Enter login: ")
      password = int(input("Enter password: "))


    if employee_verification(login,password):
     verification=True
     print("Here are all the features available to the employee {}\n".format(login))
     print("1)Register a new user\t\t\t\t\t\t\t2)Transfer money from one account to another\n3)Making a loan for a client who has a bank account\t4)Making a loan for a new client (To do this, you will need to open an account for him)\n5)Client Card Lock\t\t\t\t\t\t\t\t\t\t6)Pledge loan processing\n7)All customers\n")

     select1 = int(input("Enter function to execute: "))

     if select1 == 1:
         print("1)Register a new user\t\t\t1.1)Open an account for a client (Two account types $, AZN are available)\t\t\t1.2)Open card for customer\n")

         select2 = input("Enter function to execute: ")

         if select2=="1":
           uname=input("Enter customer name: ")
           uSurname=input("Enter customer name: ")
           uYearofbirth=input("Enter customer's year of birth: ")
           uphonenumber=int(input("Enter customer mobile number: "))
           uresidence=input("Enter customer location: ")
           ulogin=input("Enter customer login: ")
           upassword=int(input("Enter customer password: "))
           user.add_user(uname,uSurname,uYearofbirth,uphonenumber,uresidence,ulogin,upassword)

         elif select2=="1.1":
            unamecheck=input("Enter customer name: ")
            unamebill=input("Choose account currency: ")
            Efun.open_an_bill_with_a_client(unamecheck,unamebill)


         elif select2=="1.2":
             unamecheckcard=input("Enter customer name: ")
             Efun.new_card_user(unamecheckcard)

     elif select1 == 2:
         unametransfer=input("Enter customer name: ")
         unamebill1=int(input("Choose from which account to withdraw money (1 or 2): "))
         unamebill2=int(input("Choose which account to send money to (1 or 2): "))
         unamesummtransfer=int(input("Choose transfer amount: "))
         Efun.transfer(unametransfer,unamebill1,unamebill2,unamesummtransfer)


     elif select1 == 3:
         unamekredit=input("The name of the client for whom the loan is issued: ")
         usumkredit=int(input("Enter loan amount: "))
         timekredit=int(input("Enter the time in months: "))
         Efun.loan_processing_on_bill(unamekredit,usumkredit,timekredit)
         #докончить

     elif select1 ==4:
         unamebillnewname=input("Enter customer name: ")
         unamebillnew=input("Choose account currency: ")
         unamebillnewcredit=int(input("Enter loan amount: "))
         unamebillnewtime=int(input("Enter loan soon: "))
         Efun.new_kredit_new_bill(unamebillnewname,unamebillnew,unamebillnewcredit,unamebillnewtime)




     elif select1 == 5:
         card_id=int(input("Enter the id card you want to block: "))
         Efun.bloc_card(card_id)

     elif select1 == 7:
         user.Print()

     elif select1==6:
         unamecreditzaloq=input("Enter customer name: ")
         zaloq=input("Enter what you want to pledge: ")
         Efun.zaloq_credit(unamecreditzaloq, zaloq)

     elif select1==7:
         user.Print()

    else:
         print("Password is incorrect repeat password.\n")

