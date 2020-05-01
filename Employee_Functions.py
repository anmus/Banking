import User_database as user
from random import randint


def transfer(unametransfer,unamebill1,unamebill2,unamesummtransfer):    #Функция 2) Перевод денег с одного счета на другой
    for row in user.user_all_database:
        if row[1]==unametransfer:
            if unamebill1==1 and unamebill2==2:
              if row[8]!='' and row[10]!='':
                row[9]-=unamesummtransfer
                row[11]+=unamesummtransfer
              else:
                  print("There is no first or second account :(")
            elif unamebill1==2 and unamebill2==1:
                if row[8]!='' and row[10]!='':
                 row[11] -= unamesummtransfer
                 row[9] += unamesummtransfer
                else:
                    print("There is no first or second account :(")

########################################################################################################################

def loan_processing_on_bill(unamekredit,usumkredit,timekredit):

    for row in user.user_all_database:                   #Функция оформления кредита
       if row[8]=="AZE" or row[8]=="USD" or row[8]=="usd" or row[8]=="aze" or row[10]=="AZE" or row[10]=="USD" or row[9]=="usd" or row[10]=="aze":
         if row[1] == unamekredit:
            row[13]+=usumkredit
            row[14]+=timekredit
            print("The loan was issued")
         #доделать
########################################################################################################################

def bloc_card(card_id):                     #Функция Блокировки карты
    for row in user.user_all_database:
        if row[12] == card_id:
            if row[12]==False:
                row[12]=True

########################################################################################################################
tmp_bill=2

def open_an_bill_with_a_client(unamecheck,unamebill):            #Открыть счёт клиенту

    global tmp_bill
    if tmp_bill>0:
     for row in user.user_all_database:
        if row[1]==unamecheck:
            if row[8]=='':
             row[8]=unamebill
             tmp_bill-=1
            else:
                row[10]=unamebill
                tmp_bill-=1
########################################################################################################################


uidcard = 999999999999999
def genNewCarID():                    #Генератор ид для карт
    global uidcard
    uidcard += 1
    return uidcard

def new_card_user(unamecheckcard):
    global uidcard
    genNewCarID()
    for row in user.user_all_database:
        if row[1]==unamecheckcard:

            if row[8]!=" ":
                row[15] = uidcard

            else:
                row[16] = uidcard
########################################################################################################################

def new_client_kredit():
 pass

########################################################################################################################


def zaloq_credit(unamecreditzaloq, zaloq):               #Кредит по Залогу
    for row in user.user_all_database:
        if row[1]==unamecreditzaloq:
            row[17]=zaloq
            row[18]=randint(1000,200000)
            print("You got a loan {} manat ".format(row[18]))

########################################################################################################################

def new_kredit_new_bill(unamebillnewname,unamebillnew,unamebillnewcredit,unamebillnewtime):
    for row in user.user_all_database:
        if row[1]==unamebillnewname:
            if row[8]=='' and row[10]=='':
                row[8]=unamebillnew
                row[9]+=unamebillnewcredit
                row[13]+= unamebillnewcredit
                row[14]+= unamebillnewtime




