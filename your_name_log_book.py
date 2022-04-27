log = {'Ellen Hank': [100.00, 85.00, 93.61],
           'Markus Smith': [83, 95.12, 91.30],
           'Joseph Depp': [83.45, 77.20, 79.88],
           'Roger Leo': [96, 90.10, 92.80]}
ave_all = 0
max_value=0
basic_salary = 2450
for i in log.values():
    ave = (i[0]+i[1]+i[2])/3
    ave_all+=ave
    print("%.2f"%ave)
    if ave > max_value:
        max_value = ave

print('max average is: Roger Leo', max_value)
bonus = basic_salary * (1+0.125)
print('bonus: ', bonus)
ave1 = ave_all/4
print('ave for all', ave1)
print('Roger Leo got the bonus and his salary is: ', bonus + max_value)


    
    
