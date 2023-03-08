a=int(input("How many elements do you want in the list: "))
l=[]
for i in range(a):
    b=input("enter the element: ")
    l.append(b)
for i in range(0,len(l),2):
    print(l[i])

