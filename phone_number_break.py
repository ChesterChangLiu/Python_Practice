phone_number = int(input())
line_number = phone_number % 10000
area_code_prefix = phone_number // 10000
area_code = area_code_prefix // 1000
prefix = area_code_prefix % 1000
print('(',area_code,')',' ',prefix,'-',line_number, sep='')
