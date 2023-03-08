"""Question
x=[4,-2,8,9,-12,14,11,16]
1)print the count of the negetive numbers
2)print the max number
3)print the min number
4)check weather a given number exists or not"""
#1)
x=[4,-2,8,9,-12,14,11,16]
neg=0
for i in x:
    if i<0:
        neg+=1
print(f"Number of negetive integers are {neg}")
#2)
x=[4,-2,8,9,-12,14,11,16]
max=x[0]
for i in x:
    if i>max:
        max=i
print(f"The maximum number in the list {x} is {max} ")
#3)
x=[4,-2,8,9,-12,14,11,16]
min=x[0]
for i in x:
    if i<min:
        min=i
print(f"The minimum number in the list {x} is {min} ")
#4)
x=[4,-2,8,9,-12,14,11,16]
Element=int(input("enter a number: "))
counter=0
found=False
for i in x:
    counter+=1
    if i==Element:
        found=True
if found:
    print(f"{Element} Found at {counter}th position")
else:
    print("element not found")