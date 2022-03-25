def get_numbers(num):
    numbers = []
    user_input = input('Enter 3 integers in a single line: ')
    for token in user_input.split():   #split separates tokens
       number = int(token)
       numbers.append(number)
    return numbers
nums = get_numbers(3)
print(nums)
