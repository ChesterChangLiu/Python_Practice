# This program uses a list of strings; an alternative to using the #   replace() function for strings
w1 = input("Enter original word: ")
w2 = input("Enter replacement word: ")
s = input("Enter sentence:")
words = s.split(' ')

lst=[]
for t in words:
  lst.append(t)  #this adds all the words to the list
i=0
while i<len(lst):
     if lst[i] == w1:   # this code does the replacement
        lst[i] = w2
     i += 1

print(' '.join(lst)) # change from a list to a string
