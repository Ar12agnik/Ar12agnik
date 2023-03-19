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
    def delete_from_front(self):
        temp=self.head
        newnode=temp.adress
        self.head=newnode
    def delete_from_end(self):
        temp=self.head
        while temp is not self.last:
            prev=temp
            temp=temp.adress
        prev.adress=None
        print(prev.data)
        self.last=prev
    def del_at_given_node(self,pos):
        temp=self.head
        pos-=1
        while pos>0:
            prev=temp
            temp=temp.adress
            pos-=1
        prev.adress=temp.adress
s=LinkedList()
while True:
    choice=int(input("1)insert into linked list\n2)print the linked list\n3)delete from the linked list\n4)get length of the list\n5)print the maximum element\n6)exit\nenter your choice:"))
    if choice==1:
        choice_2=int(input("1)insert at front\n2)insert at the back\n3)insert at a position\nenter your choice:"))
        if choice_2==1:
            elements=int(input("how many elements? "))
            for i in range(elements):
                s.insert_at_front(int(input("enter the number: ")))
        elif choice_2==2:
            elements=int(input("how many elements? "))
            for i in range(elements):
                s.insert_at_last(int(input("enter a number: ")))
        elif choice_2==3:
            s.insert_at_index(int(input("enter the position: ")),int(input("enter the data: ")))
    elif choice==2:
        s.printList()
    elif choice==3:
        choice_2=int(input("1)delete at front\n2)delete at the end\n3)delete at position\nenter your choice:"))
        if choice_2==1:
            s.delete_from_front()
        elif choice_2==2:
            s.delete_from_end()
        elif choice==3:
            s.del_at_given_node(int(input("enter the position to be deleted: ")))
    elif choice==4:
        s.count_element()
    elif choice==5:
        s.max_element_found()
    elif choice==6:
        break
    else:
        print("Invalid Choice")