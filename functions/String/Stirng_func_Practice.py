str1='Boo Hoo!'        
print(str1.find('!'))         #7 index value of '!’
print(str1.find('Boo'))   #0 index of the start of substring 
print(str1.find('oo'))      #1 index of start of the first 'oo’ 
print(str1.find('oo', 2))  #5 index of start of 'oo' in a search starting at index 2
print(str1.rfind('oo'))    #5 index of start of the first 'oo' in a search in reverse order 
print(str1.count('ooH'))  #0 the number of sub-strings 'oo'
str1 = str1.replace('Boo', 'Boo Boo')
print(str1)