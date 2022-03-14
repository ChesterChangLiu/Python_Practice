def mph(miles_per_hour, minutes_traveled):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled

a = float(input('Enter miles per hour: '))
b = float(input('Enter minutes traveled: '))
print(f'Miles: {mph(a,b):f}')
