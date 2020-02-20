number= int(input("βάλε αριθμό:"))
num=number
while num > 9 :
    number = number * 3
    number = number +1 
    r=0
    while number > 0 :
        re = number % 10
        r = r + re
        number = int(number//10)
    print ("το αποτέλεσμα το αριθμών είναι:",r)
    number=r
    num=r