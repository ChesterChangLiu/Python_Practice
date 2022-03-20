import random

def redpacket(num,total):
    already=0
    each=[]
    for i in range(1,num):
        t=random.randint(1,(total-already)-(num-i))
        each.append(t)
        already=already+t
    each.append(total-already)
    myformat="The {0} person gets {1} dollars".format
    i=[i for i in range(1,num+1)]
    print(list(map(myformat,i,each)))
'''
def ordinal(value):

    try:
        value = int(value)
    except ValueError:
        return value

    if value % 100//10 != 1:
        if value % 10 == 1:
            ordval = u"%d%s" % (value, "st")
        elif value % 10 == 2:
            ordval = u"%d%s" % (value, "nd")
        elif value % 10 == 3:
            ordval = u"%d%s" % (value, "rd")
        else:
            ordval = u"%d%s" % (value, "th")
    else:
        ordval = u"%d%s" % (value, "th")

    return ordval
    '''

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print("Ordinal number:", ordinal(num))
if __name__=="__main__":
    total=int(input("Enter total amount for your red packet: "))
    num=int(input("Enter the number of participants: "))
    redpacket(num,total)
