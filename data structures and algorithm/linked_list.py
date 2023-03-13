class list:
    def __init__(self,n):
        self.data=n
        self.adress=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,n):
        newNode=list(n)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.adress=newNode
            self.last=newNode
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.adress
s=LinkedList()
s.create(10)
s.create(20)
s.printList()


