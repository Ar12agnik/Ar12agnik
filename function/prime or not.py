def prime_or_not(number):
    for i in range(number):
        if i==1:
            pass
        elif i>1:
            if number%i==0:
                t= False
                break
            else:
                t=True
                pass
    if t==False:
        return False
    else:
        return True
a=int(input("enter a number: "))
c=prime_or_not(a)
print(c)
