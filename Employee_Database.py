employee_database=[["Aslan",hash(123)],["Tural",hash(1234)],["Emil",hash(12345)]]


def employee_verification(login,password):
    for i in employee_database.__iter__():
        if i[0]==login and i[1]==password:
            return True





