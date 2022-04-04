f = open('mydata.txt')
contents = f.read()
tokens = contents.split(',’)  
print('Closing file')
f.close()  

i=0
while i < len(tokens):  
  nr = tokens.count(tokens[i]) 
  print(tokens[i], nr)
  i += 1
 
