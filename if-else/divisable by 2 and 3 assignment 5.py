a=int(input("enter a number:  "))
if a%6==0:
    print("number is both divisable by 2 and 3")
elif a%2==0 and a%3!=0:
    print("number is only divisable by 2")
elif a%3==0 and a%2!=0:
    print("number is only divisable by 3 ")
