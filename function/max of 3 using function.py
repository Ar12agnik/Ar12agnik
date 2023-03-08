def max_of_three(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z
x=int(input("enter a number:"))
y=int(input("enter another number"))
z=int(input("enter yet another number: "))
maz=max_of_three(x,y,z)
print(maz)
