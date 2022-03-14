f = int(input("Enter a Fahrenheit: "))
def daily_temp(f):
    c = ((f-32)*5/9)
    return c
print( '%.0f Fahrenheit is %.0f Celsius' %(f, daily_temp(f)))
