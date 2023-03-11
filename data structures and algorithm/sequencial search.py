import numpy as np
x=[2,4,6,8,18,22,23,29,37,40]
x=np.array(x)
find=int(input("enter a number: "))
found=0
for i in range(0,len(x)):
    if x[i]==find:
        print(f"element found at {i}th position ")
        found =1
        break
if found!=1:
    print("Element not found!!")
    