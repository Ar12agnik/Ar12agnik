class node:
    def __init__(self,Data):
        self.data=Data
        self.adress=None
class Stack:
    def __init__(self):
        self.head=None
        self.top=None
    def push(self,Data):
        newNode=node(Data)
        if self.head is None:
            self.head=newNode
            self.top=newNode
        else:
            self.top.adess=newNode
            self.top=newNode
        print("element inserted!")
    def pop(self):
        if self.head is None:
            print("UNDERFLOW!!")
        temp=self.head
        while temp is not self.top:
            prev=temp
            temp=temp.adress
        print(f"{temp} deleted!")
        prev.adress=None
        self.top=prev
stack=Stack()
while True:
    choice=int(input("1)push\n2)pop\n3)exit\nenter your choice: "))
    if choice==1:
        stack.push(int(input("enter an element")))
    elif choice==2:
        stack.pop()
    elif choice==3:
        break
    else:
        print("Invalid Input!!")

