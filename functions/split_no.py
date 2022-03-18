def get_num(num):
    numbers = []
    ui = input('Enter 3 integers')
    for token in ui.split():
        number = int(token)
        numbers.append(number)
    return numbers
