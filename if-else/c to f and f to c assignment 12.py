choice=int(input("1)CELCIUS TO FARENHEIGHT \n2)FARENHEIGHT TO CELCIUS\nEnter Your Choice: "))
if choice==1:
    cel=int(input("enter temp in celcius: "))
    faren=(cel*(9/5))+32
    print("converted temp is ",faren)
elif choice==2:
    faren=int(input("enter temp in farenheight: "))
    cel=(faren-32)*(5/9)
    print("converted temp ",cel)
else:
    print("enter a valid choice!!")