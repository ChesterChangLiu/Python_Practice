word = input()

password = ''

#checking for and modifying user's password if containing the characters: i, a, m, B, or s

for character in word: # update password rather than word

    if(character=='i'): #if user's password contains the letter i change to 1
        password += '1'
    
    elif(character=='a'): #if user's password contains the letter a change to @
        password += '@'
        
    elif(character=='m'): #if the user's password contains the letter m change to M
        password += 'M'
        
    elif(character=='B'): #if the user's password contains the letter B change to 8
        password += '8'
        
    elif(character=='s'): #if the user's password contains the letter s change to $
        password += '$'
        
    else: # add else statement for when symbols do not get replaced 
        password += character

print(password+'!')
