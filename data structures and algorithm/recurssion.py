#print 1 to 10 ruccersively
def print_1_to_10_recursively(n):
    if n==10:
        print(10)
    else:
        print(n)
        return print_1_to_10_recursively(n+1)
print_1_to_10_recursively(1)
#factorial of a given number
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter a number: "))
print(f"factorial of {num} is {factorial(num)}")
#summesion 1-10
def summesion_1_to_10(n):
    if n==1:
        return 1
    else:
        return n+summesion_1_to_10(n-1)
n=10
print(f"The summesion of 1 to 10 is {summesion_1_to_10(10)}")
#summesion given range
def summesion_given_range(start,stop):
    if start==stop:
        return stop
    else:
        return start+summesion_given_range(start+1,stop)
start=int(input("enter the start value: "))
stop=int(input("enter the end value: "))
print(f"The summesion from {start} to {stop} is {summesion_given_range(start,stop)}")
