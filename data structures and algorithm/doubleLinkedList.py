class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def create(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            newNode.prev=self.last
            self.last=newNode
    def insert_at_front(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode
    def insert_at_end(self,data):
        self.create(data)
    def insert_at_random_pos(self,pos,data):
        pos-=2
        temp=self.head
        newNode=node(data)
        while pos>0:
            pos-=1
            temp=temp.next
        newNode.prev=temp.next.p
        newNode.next=temp.next
        temp.next=newNode
        
        temp.next.prev=newNode
    def printL(self):
        temp=self.head
        temp2=self.last
        while temp is not None:
            print(temp.data)
            temp=temp.next
        print("---------------------------------------------------------------------------------------------------------------------------------")
        while temp2 is not None:
            print(temp2.data)
            temp2=temp2.prev

c=DLinkedList()
c.create(10)
c.create(20)
c.create(30)
c.create(40)
c.create(50)
c.insert_at_random_pos(3,19)
c.printL()

    


