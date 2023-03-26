class List:
    def __init__(self,Data):
        self.data=Data
        self.address=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def create(self,n):
        newNode=List(n)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.address=newNode
            self.last=newNode
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.address
    def insert_at_front(self,data):
        old_head=self.head
        newNode=List(data)
        newNode.address=old_head
        self.head=newNode
    def insert_at_index(self,position,n):
        newNode=List(n)
        position-=2
        temp=self.head
        while position>0:
            temp=temp.address
            position-=1
        newNode.address=temp.address
        temp.address=newNode
    def insert_at_last(self,data):
        self.create(data)
    def delete_from_front(self):
        temp=self.head
        newNode=temp.address
        self.head=newNode
    def delete_from_end(self):
        temp=self.head
        while temp is not self.last:
            prev=temp
            temp=temp.address
        prev.address=None
        self.last=prev
    def delete_at_node(self,position):
        temp=self.head
        position-=1
        while position>0:
            prev=temp
            temp=temp.address
            position-=1
        prev.address=temp.address
s=LinkedList()
s.create(12)
s.create(14)
s.create(16)
s.create(18)
s.create(20)
s.create(26)
s.create(45)
print('The linked list: ')
s.printList()
s.insert_at_front(5)
print('after insertion')
s.printList()
s.insert_at_index(3,16)
print('after insertion')
s.printList()
s.insert_at_last(22)
print('after insertion at last')
s.printList()
s.delete_from_front()
print('after deletion from front')
s.printList()
s.delete_from_end()
print('after deleting from end')
s.printList()
s.delete_at_node(3)
print('after deleting')
s.printList()