# This program runs through 2 loops - nested into each other
# One is while - outerloop
# One is for   - inner loop

num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))
    if num >= 0:
        print('Depicted graphically:')
        for i in range(num):
           print('*')
        print('For loop ends here')
print('Goodbye!')
