class node:
    def __init__(self,Data):
        self.data=Data
        self.adress=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,Data):
        newNode=node(Data)
        if self.top is None:
            self.top=newNode
        else:
            newNode.adress=self.top
            self.top=newNode
        print(Data,"Inserted!")
    def pop(self):
        if self.top==None:
            print("UNDERFLOW!!")
        else:
            print(self.top.data,"Deleted")
            self.top=self.top.adress
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

