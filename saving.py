#P4: Program that calculates savings 
initial_savings = 10000
interest_rate = 0.03
print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

years = int(input('Enter years: '))
savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings at beginning of year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable
    
#Input/Output:
#Enter years: 3
#Savings at beginning of year 1: $10000.00
#Savings at beginning of year 2: $10300.00
#Savings at beginning of year 3: $10609.00
