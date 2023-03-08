matrix=[]
r=int(input("enter the number of rows in the matrix: "))
c=int(input("enter the number of collums: "))
for i in range(r):
    l=[]
    for j in range(c):
        x="Enter the "+str(i+1)+' '+str(j+1)+"th element: "
        element=int(input(x))
        l.append(element)
    matrix.append(l)
s=0
r_n=1
for i in matrix:
    s=0
    for j in i:
        s+=j
    print("the sum of  row ",r_n," is ",s)
    r_n+=1