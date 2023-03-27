import numpy as np
x=[2,4,6,7,10,12,14,16,18,20]
array=np.array(x)
low=0
high=len(array)-1
search=int(input("enter an element to be searched: "))
found=0
while (low<=high):
    pos=round(low+((search-x[low])/(x[high]-x[low]))*(high-low))
    if array[pos]==search:
        found=1
        print(f"Element found at {pos}")
        break
    elif array[pos]>search:
        high=pos-1        
    elif array[pos]<search:
        low=pos+1    
if found==0:
    print("element not found!")

