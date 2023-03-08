#stack using numpyarray

def push(n):
    global top
    if top==9:
        print("OVERFLOW!!")
        return
    else:
        top+=1
        stack[top]=n
def pop():
    global top
    if top==-1:
        print("UNDERFLOW!!")
        return
    else:
        print(stack[top])
        top-=1

import numpy as np
stack=np.zeros(10,dtype='int16')
top=-1
while True:
    ch=int(input("<1 push><2 pop><3 exit>"))
    if ch==1:
        x=int(input("Enter a number: "))
        push(x)
    elif ch==2:
        pop()
    elif ch==3:
        break
    else:
        print("invalid input try again")
        pass
