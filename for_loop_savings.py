initial_savings = 10000

interest_rate = float(input('Enter rate of interest: '))

years = int(input('Enter years: '))

savings = initial_savings

for i in range(1, years+1):

    print(' Savings in year {}: ${:.2f}'.format(i, savings))

    savings = savings + (savings*interest_rate)

