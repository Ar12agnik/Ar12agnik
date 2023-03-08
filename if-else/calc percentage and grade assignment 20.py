Physics = int(input("Enter the marks of physics: "))
Chemistry = int(input("Enter the marks of chemistry: "))
Mathematics = int(input("Enter the marks of mathematics: "))
Biology = int(input("Enter the marks of biology: "))
Computer = int(input("Enter the marks of computer: "))
per = (Physics+Chemistry+Mathematics+Biology+Computer)/500
per = per*100
if per > 100:
    print("Grade AA")
elif per > 80:
    print("Grade A")
elif per > 60:
    print("Grade B")
elif per > 40:
    print("Grade C")
elif per > 20:
    print("Grade D")
else:
    print("FAIL")