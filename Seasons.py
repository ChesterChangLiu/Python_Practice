input_month = input()
input_day = int(input())
month_days = {
    "January": (1, 31), "February": (2, 28), "March": (3, 31), "April": (4, 30),
    "May": (5, 31), "June": (6, 30), "July": (7, 31), "August": (8, 31),
    "September": (9, 30), "October": (10, 31), "November": (11, 30), "December": (12, 31)
}

if input_month in month_days and 1 <= input_day <= month_days[input_month][1]:
    # convert input to date
    date = (month_days[input_month][0], input_day)
    # convert season boundaries to date
    if (3, 20) <= date <= (6, 20):
        print("Spring")
    elif (6, 21) <= date <= (9, 21):
        print("Summer")
    elif (9, 22) <= date <= (12, 20):
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
