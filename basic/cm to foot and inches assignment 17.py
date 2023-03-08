cm=int(input("enter height in centimeters:"))
temp_inch=cm/2.54
feet=temp_inch//12
inch=temp_inch-(12*feet)
inch=int(inch)
print(cm,"cm in foot and inches are: ",feet,"foot and ",inch,"inches ")