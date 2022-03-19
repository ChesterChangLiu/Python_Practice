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

if __name__=="__main__":
    total=int(input("Enter total amount for your red packet: "))
    num=int(input("Enter the number of participants: "))
    redpacket(num,total)
