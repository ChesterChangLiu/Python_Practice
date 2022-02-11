val_sum = 0
num_val = 0
curr_value = int(input('Enter any positive integer (-1 will stop): '))
while curr_value > 0 :
    val_sum += curr_value
    num_val = num_val + 1 
    curr_value = int(input('Enter any positive integer (-1 will stop): '))
print('Average of input integers', val_sum / num_val)
    
# num_val = N (no.of elements)
# val_sum = Sum of all elements
