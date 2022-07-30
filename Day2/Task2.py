import datetime
a = 5
b = 0
try:
    print(a/b)
except ArithmeticError:
    open("Day2/log.txt","w").writelines("Arithmetic Error at "+str(datetime.datetime.now()))