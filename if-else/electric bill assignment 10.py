unit=int(input("enter units consumed: "))
if unit in range(1,100):
    print("RS 5")
elif unit in range(101,200):
    print("RS 7")
elif unit in range(201,300):
    print("RS 10")
elif unit>300:
    print("15")
else:
    print("please enter a positive number!!!!!!!")
