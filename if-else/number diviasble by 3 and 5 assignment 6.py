n=int(input("enter a number: "))
while True:
    if n%15==0:
        print("number is diviasble by both 3 and 5")
    elif n%3==0and n%5!=0:
        print("number is only divisable buy 3")
    elif n%3!=0 and n%5==0:
        print("number only diviasble by 5 ")
    else:
        print("number is not divisable by 3 and 5")
    break