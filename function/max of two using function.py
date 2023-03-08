def max_of_two(x,y):
    if x>y:
        return x
    else:
        return y
x=int(input("enter a number: "))
y=int(input("enter another number: "))
max=max_of_two(x,y)
print(max)