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
        self.head.prev=newNode
        newNode.next=self.head
        self.head=newNode
    def insert_at_end(self,data):
        self.create(data)
    def insert_at_random_pos(self,pos,data):
        pos -= 2
        temp = self.head
        newNode = node(data)
        while pos > 0:
            pos -= 1
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
    def delete_at_front(self):
        print(f"{self.head.data} has been deleted!")
        self.head=self.head.next
        self.head.prev=None
    def delete_from_end(self):
        self.last.prev.next=None
        self.last=self.last.prev
    def delete_at_pos(self,pos):
        pos-=1
        temp=self.head
        while pos>0:
            pos-=1
            temp=temp.next
        temp.prev.next=temp.next
        temp.next.prev=temp.prev



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
print("Original list: ")
c.printL()
print("after inserting at the front: ")
c.insert_at_front(11)
c.printL()
print("after deleting from front: ")
c.delete_at_front()
c.printL()
print("After inserting at the end: ")
c.insert_at_end(100)
c.printL()
print("after deleting from last: ")
c.delete_from_end()
c.printL()
print("afterinserting at random position: ")
c.insert_at_random_pos(3,1000000000)
c.printL()
print("after deleting from random position: ")
c.delete_at_pos(3)
c.printL()
print("\nThe End")
    


