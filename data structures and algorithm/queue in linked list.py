class node:
    def __init__(self,Data):
        self.data=Data
        self.adress=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def push(self,Data):
        newNode=node(Data)
        if self.front is None:
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.adress=newNode
            self.rear=newNode
        print("element inserted!")
    def pop(self):
        if self.front is None:
            print("UNDERFLOW!!!")
        else:
            print(f"{self.front.data} Deleted")
            self.front=self.front.adress
        
    def printList(self):
        temp=self.front
        while temp is not None:
            print(temp.data)
            temp=temp.adress
Queue=Queue()
while True:
    choice=int(input("1)push\n2)pop\n3)exit\nenter your choice: "))
    if choice==1:
        Queue.push(int(input("enter an element")))
    elif choice==2:
        Queue.pop()
    elif choice==3:
        break
    else:
        Queue.printList()

