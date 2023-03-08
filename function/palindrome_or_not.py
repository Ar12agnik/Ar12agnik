def palindrome_or_not(number):
    n=0
    number_copy=number
    while number!=0:
        n=n*10+(number%10)
        number=number//10
    if number_copy==n:
        return True
    else:
        return False
n=int(input("enter a number: "))
print(palindrome_or_not(n))

