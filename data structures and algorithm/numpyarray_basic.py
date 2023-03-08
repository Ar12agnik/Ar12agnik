import numpy as np
x=np.zeros(10,dtype='int16')#creates an array of len 10 contaning all zeros
#adding elements to the array 
for i in range(0,10):
    y=int(input("enter a number: "))
    x[i]=y
    sum=0
for i in range(0,10):
    sum+=x[i]
print(f"the avarage of the given numbers is {sum/10}")