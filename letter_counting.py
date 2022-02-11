print('Enter a line of text:::')
t=input()
i=0
nr=0
while i<len(t):
   if (t[i] != ' ' and t[i] != '.' and t[i] != ','):
      nr += 1
   i += 1
print('Numbers present in the user given text',nr)
