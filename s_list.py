from turtle import clear


numbers = [3, 7, 1, 4, 2, 8, 5, 6]
numbers *= 2
print(numbers.index(5, 7)) # Output: 14=index of the number 5 in a search which starts at index=7(at number 6)
#P3
# Specifying a Slice with Starting and Ending Indices
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers[2:6]) # Output: [5, 7, 11, 13]

# Specifying a Slice with Only an Ending Index
print(numbers[:6])  # Output: [2, 3, 5, 7, 11, 13] 
print(numbers[0:6]) # Output: [2, 3, 5, 7, 11, 13]

# Specifying a Slice with Only a Starting Index
print(numbers[6:])             # Output: [17, 19]
print(numbers[6:len(numbers)]) # Output: [17, 19]

# Specifying a Slice with No Indices
print(numbers[:]) # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Slicing with Steps
print(numbers[::2]) # Output:[2, 5, 11, 17]

# Slicing with Negative Indices and Steps
print(numbers[::-1])     # Output: [19, 17, 13, 11, 7, 5, 3, 2]
