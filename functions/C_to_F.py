c = int(input("Enter a Centigrade: "))
def daily_temp(c):
    f = (c*1.8) + 32
    return f
print( '%.0f Celsius is %.0f Fahrenheit' %(c, daily_temp(c)))
   


