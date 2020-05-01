
user_all_database = []

uid = 99999

def genNewID():
    global uid
    uid += 1
    return uid


def add_user(uname,uSurname, uYearofbirth, uphonenumber, uresidence, ulogin, upassword):
    mas = []
    genNewID()


    mas.append(uid)
    mas.append(uname)
    mas.append(uSurname)
    mas.append(uYearofbirth)
    mas.append(uphonenumber)
    mas.append(uresidence)
    mas.append(ulogin)
    mas.append(upassword)
    mas.append('')         #Первый счет индекс 8
    mas.append(0)       #Баланс первого счёта индекс 9
    mas.append('')         #Второй счёт индекс 10
    mas.append(0)       #Баланс второго счёта индекс 11
    mas.append(False)         #Блокировка карты индекс 12
    mas.append(int())         # Суммма кредита индекс 13
    mas.append(int())         # Время кредита индекс 14
    mas.append(int())         # Первый карт ид  индекс 15
    mas.append(int())         # Второй карт ид  индекс 16
    mas.append('')              # Предмет залога идекс 17
    mas.append(int())                # Сумма залога по подсчтетам залога индекс 18
    user_all_database.append(mas)
    print("\nThe client has been added to the database")


def Print():
    for i in user_all_database.__iter__():
        print("\nId: {}\nName: {}\nSurname: {}\nYear Customer Birth: {}\nClient's number: {}\nСlient's place of residence: {}\nClient Login: {}\nClient password: {}\nClient bill the first: {}\nBalans: {}\nClient bill second: {}\nBalans: {}\nCredit amount: {}\nCredit term: {}\nFirst card id: {}\nId of the second card: {}\nPledge: {}\nThe amount of the loan according to the calculation of collateral: {}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[13],i[14],i[15],i[16],i[17],i[18]))


