a=int(input("How many elements do you want in the list: "))
l=[]
for i in range(a):
    b=int(input("enter the element: "))
    l.append(b)
max_el=0
for j in l:
    if j>max_el:
        max_el=j
print("max element ",max_el)