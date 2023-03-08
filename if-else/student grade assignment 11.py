a=int(input("enter marks: "))
b=int(input("enter full marks: "))
per=(a/b)*100
if per>=98:
    print("A+")
elif 90 <= per < 98:
    print("A")
elif 85<= per <90:
    print("B+")
elif 80<=per<85:
    print("B")
elif 70< per <80:
    print("C")
elif 50<= per <70:
    print("D")
elif per<50:
    print("Fail!")


