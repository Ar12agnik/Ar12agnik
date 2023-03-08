a=int(input("enter a number: "))
last=a%10
if last%3==0:
    print("last digit of ",a," is divisable by 3")
else:
    print("last digit of ", a, " is not  divisable by 3")