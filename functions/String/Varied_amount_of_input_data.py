user_input = input().split()

def ave(a):
    sum = 0
    count = 0
    for i in user_input:
        sum += int(i)
        count += 1
    ave = sum / count
    return ave

def find_max(m):
    max = None
    for i in user_input:
        i = int(i)
        if max is None or i > max:
            max = i
    return max    
        
print(round(ave(user_input)), find_max(user_input))

