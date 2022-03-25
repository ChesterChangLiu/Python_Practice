def split_join(apath, aseparator): 
    tokens = path.split('/')
    combined = new_separator.join(tokens)
    return combined

path = input( 'Enter file name (path): ')
new_separator = input('Enter new separator: ')
thepath = split_join(path, new_separator)
print(thepath)

"""
print('Enter file name: ')
path = input()
new_separator = input('Enter new separator: ')
tokens = path.split('/')
print(tokens)
combined = new_separator .join(tokens)
print(combined)
"""
