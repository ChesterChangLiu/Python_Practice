str1='   this is a long string'
print(str1.strip().upper())  #output:‘THIS IS A LONG STRING’
print(str1.title())          #output:’   This Is A Long String’  
print(str1.capitalize())     #output:’   This is a long string’  
user_input = input('Enter command:\n').strip().lower()   #input:’  HELLO’
print(user_input)                                        #output:’hello’
