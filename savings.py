#Program calculates savings at 5% interest rate
initial_savings = 15000
interest_rate = 0.05

print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

years = int(input('Enter years: '))
savings = initial_savings
i = 1  
while i <= years:  
    print(' Savings at the beginning of year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1
