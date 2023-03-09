import numpy as np
x=[2,4,6,8,18,22,23,29,37,40]
element=int(input("enter a number: "))
low=0
high=len(x)-1
while low<=high:
    
    mid=((low+high)//2)
    print (low,high,mid)
    if x[mid]==element:
        
        break
    elif x[mid]<element:
        low=mid+1
    elif x[mid]>element:
        high=mid-1
    
if x[mid]==element:
    print(f"element found at {mid}")
else:
    print("element not found")