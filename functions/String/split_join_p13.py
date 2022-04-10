print('Enter file name: ')
path = input()
new_separator = input('Enter new separator: ')
tokens = path.split('/')
print(tokens)   
combined = new_separator.join(tokens) 
print(combined)

