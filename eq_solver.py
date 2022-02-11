import math

input_1 = 21
input_2 = 813
b = math.sqrt(input_1)
a = math.sin(input_2)
x = math.pow((a*a+b)/(b*b+a*a),1/3)
print('input_1: ', input_1, '\ninput_2: ', input_2,'\nb: ', b, '\na: ', a,
      '\nx: ', x)
