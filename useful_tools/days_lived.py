from datetime import datetime

def birth_days(birth):
    birth = datetime.strptime(birth, "%Y/%m/%d")
    currdate = datetime.now()
    diff = (currdate - birth).days
    return diff

birth = input("Please input your birthday (year/month/day): ") #input have to be year/month/day
print("You have lived", birth_days(birth),"days")