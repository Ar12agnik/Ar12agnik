def insert(n):
    global rear 
    global front
    if rear-front==9:
        print("overflow!!")
        return
    else:
        rear+=1
        x[rear%10]=n
        print(f"{n} was inserted in the queue!")
def delete():
    global rear
    global front
    if front>rear:
        print("UNDERFLOW!")
        return
    else:
        print(f"{x[front%10]} was deleted!")
        front+=1

import numpy as np
x=np.zeros(10,dtype='int16')
front=0
rear=-1
while True:
    ch=int(input("<1 push><2 pop><3 exit>"))
    if ch==1:
        n=int(input("enter a number: "))
        insert(n)
    elif ch==2:
        delete()
    elif ch==3:
        break
    else:
        print("invalid choice!")
