a=int(input("enter a number :"))
b=int(input("enter another number:"))
c=int(input("enter another number:"))
if (a>b)and (a>c):
    print(a,"is the greatest ")
elif (b>a)and (b>c):
    print(c,"is the greatest among 3")
elif (c>a)and (c>b):
    print(c,"is the greatest number among 3")
else:
    print("error")
