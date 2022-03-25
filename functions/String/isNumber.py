user_string = input("Please enter: ")

def isNumber(s):
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
    return True
    
if isNumber(user_string):
    print("Yes, this is a number")
else:
    print("No, this is a string")
    
'''
input = 666
input = '666'
def isNumber(in_p):
    if type(in_p) == int:
         return True
    else:
         return False
         
if isNumber(input):
    print("yes")
else:
    print("no")
'''
