year=int(input("enter a year: "))
if (year%400==0) and (year%4==0):
    if year%100!=0:
        print("leap year")
else:
    print("year is not a leap year!")
##doubt
#year%400 and year%4 and year%100 same
