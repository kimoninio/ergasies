import datetime

def find_days_of_year(d,m,y,lY):
    total = y * 365 + lY
    total += d
    if m == 1:
        total += 0
    elif m == 2:
        total += 31
    elif m == 3:
        total += 59
    elif m == 4:
        total += 90
    elif m == 5:
        total += 120
    elif m == 6:
        total += 151
    elif m == 7:
        total += 181
    elif m == 8:
        total += 212
    elif m == 9:
        total += 243
    elif m == 10:
        total += 273
    elif m == 11:
        total += 304
    elif m == 12:
        total += 334
    return total

now = datetime.datetime.now()
today = str(now.day)
if now.month <=9:
    today += str(0) +str(now.month)
else:
    today += str(now.month)
today += str(now.year)
print("Η σημερινή μέρα είναι : " + today)
print("Γράψτε την ημερομηνία πχ αν είναι 14/02/2013 γράψτε 14022013")
youredate = int(input("Γράψτε την ημερομηνία όπως προαναφέρθηκε : "))
cd = True
while cd:
    dl = 0
    youredate1 = youredate
    if (youredate // 1000000) >=1 and (youredate // 1000000) <=9:
        dl+=1
    while youredate1 > 0:
        youredate1 = youredate1 // 10
        dl += 1

    if dl != 8:
        print("Λάθος τρόπος προσπαθήστε ξανά")
        youredate = int(input("Γράψτε την ημερομηνία όπως προαναφέρθηκε : "))
    elif (youredate // 10000 % 100) <= 0 or (youredate // 10000 % 100) >= 13:
        print("Λάθος τρόπος προσπαθήστε ξανά")
        youredate = int(input("Γράψτε την ημερομηνία όπως προαναφέρθηκε : "))
    elif (youredate // 1000000) <=0 or (youredate // 1000000) >=32:
        print("Λάθος τρόπος προσπαθήστε ξανά")
        youredate = int(input("Γράψτε την ημερομηνία όπως προαναφέρθηκε : "))
    else:
        cd = False


year = youredate % 10000
print("Τυχαία ημερομηνία : " + str(year))
lp = year//4
daysOfRandomDate = (youredate // 1000000)
print("Ο επιλεγμένος χρόνος έχει  " + str(daysOfRandomDate) + " μέρες")
month = youredate // 10000 % 100
print("και " + str(month) + " μήνες")
RandomDateInDays = find_days_of_year(daysOfRandomDate, month, year, lp)
# from now on we are talking about the current date
lp = now.year//4
currentDateInDays = find_days_of_year(now.day, now.month, now.year, lp)
difInDays = abs(int(RandomDateInDays) - int(currentDateInDays))
print("Οι δύο ημερομηνιές έχουν " + str(difInDays) + " μέρες απόσταση")
difInMinutes=difInDays*24
print("Οι δύο ημερομηνιές έχουν " + str(difInMinutes) + " λεπτά απόσταση")
difInSeconds=difInMinutes*60
print("Οι δύο ημερομηνιές έχουν " + str(difInSeconds) + " δευτερόλεπτα απόσταση")
if month == 1:
    daysOfTheMonth = 31
elif month == 2:
    if year % 4 == 0:
        daysOfTheMonth = 28
    else:
        daysOfTheMonth = 29
elif month == 3:
    daysOfTheMonth = 31
elif month == 4:
    daysOfTheMonth = 30
elif month == 5:
    daysOfTheMonth = 31
elif month == 6:
    daysOfTheMonth = 30
elif month == 7:
    daysOfTheMonth = 31
elif month == 8:
    daysOfTheMonth = 31
elif month == 9:
    daysOfTheMonth = 30
elif month == 10:
    daysOfTheMonth = 31
elif month == 11:
    daysOfTheMonth = 30
elif month == 12:
    daysOfTheMonth = 31

print("Ο επιλεγμένος μήνας έχει  " + str(daysOfTheMonth) + " μέρες")