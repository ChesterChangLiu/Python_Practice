temp = input ('input the temperature you like to convert: ') #(e.g., 50C, 122F)
scale = temp[-1]
degree = int(temp[:-1])

def daily_temp(scale, degree):
    if  scale == "C":
        f = (degree*1.8)+32
        print( '%.0f Celsius is %.0f Fahrenheit' %(degree, f))
    elif scale == "F":
        c = ((degree-32)*5/9)
        print( '%.0f Fahrenheit is %.0f Celsius' %(degree, c))
    else:
        print( "Invalid input")
daily_temp(scale, degree)
