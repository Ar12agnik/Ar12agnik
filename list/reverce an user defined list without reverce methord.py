a=int(input("How many elements do you want in the list: "))
l=[]
temp=[]
for i in range(a):
    b=input("enter the element: ")
    l.append(b)
for j in range(len(l)-1,-1,-1):
    temp.append(l[j])
l=temp.copy()
print("reverced list: ",l)