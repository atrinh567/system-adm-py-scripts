import time
import datetime

name = input("What is your name? ")
birthdate = input("What is your birthdate? MM/DD/YYYY ")

def checkDate(name, birthdate):
    date = birthdate.split("/")

    if len(date) != 3:
        return False

    if int(date[0]) < 1 or int(date[0]) > 12:
        return False
    elif int(date[1]) >= 1 or int(date[1]) <= 31:
        if int(date[1]) == 31 and int(date[0]) not in [1,3,5,7,8,10,12]:
            return False
        elif int(date[1]) == 30 and int(date[0]) not in [4,6,9,11]:
            return False
    elif int(date[2]) <= 1970 or int(date[2]) > datetime.datetime.now().year:
        return False
    
    seconds = time.time() - time.mktime(datetime.date(int(date[2]), int(date[0]), int(date[1])).timetuple())
    print("{}, are {} years old!".format(name, int(seconds / 31556952)))

checkDate(name, birthdate)