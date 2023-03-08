def list_sum(numbers):
    s=0
    for i in numbers:
        s+=i
    return s
l1=[]
n=int(input("how many numbers? "))
for i in range(n):
    temp=int(input("enter a number: "))
    l1.append(temp)
sum=list_sum(l1)
print(sum)
