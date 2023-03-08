def insert(n):
    global rear
    if rear==9:
        print("overflow!!")
        return
    else:
        x[rear]=n
        rear+=1
def delete():
    global front,rear
    if front>rear:
        print("Underflow")
    else:
        print(x[front])
        front+=1

import numpy as np
x=np.zeros(10,dtype='int16')
rear=-1
front=0
while True:
    ch=int(input("<1 insert>\n<2 delete>\n<3 exit>"))
    if ch==1:
        n=int(input("enter a number: "))
        insert(n)
    elif ch==2:
        delete()
    elif ch==3:
        break