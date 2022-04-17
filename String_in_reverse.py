while True:
    
    a = input()
    if (a == 'Done' or a == 'done' or a == 'd'):
        break
    else:
        for a in reversed(a):
            print(a, end = '')
        print()
