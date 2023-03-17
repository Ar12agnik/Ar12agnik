class List:
    def __init__(self,n):
        self.data=n
        self.adress=None
class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,n):
        newNode=List(n)
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
    def max_element_found(self):
        maximum=self.head.data
        temp=self.head
        while temp is not None:
            if temp.data>maximum:
                maximum=temp.data
            temp=temp.adress
        print(f"The maximum element found is {maximum}")
    def count_element(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.adress
        print(f" no of elements found {count}")
    def insert_at_front(self,data):
        old_head=self.head
        newnode=List(data)
        newnode.adress=old_head
        self.head=newnode
    def insert_at_index(self,position,n):
        newNode=List(n)
        position-=2
        temp=self.head
        while position>0:
            temp=temp.adress
            position-=1
        newNode.adress=temp.adress
        temp.adress=newNode
        
    def insert_at_last(self,data):
        self.create(data)

                    
                
            
s=LinkedList()
i=int(input("how many elements?\n "))
for j in range(i):
    s.create(int(input("enter the element: ")))
s.max_element_found()
s.count_element()
s.insert_at_front(int(input("enter the element to be inserted at first: ")))
s.insert_at_index(int(input("enter the  position")),int(input("enter the data")))
s.insert_at_last(12)
print("The elements of the linked list are:-")
s.printList()