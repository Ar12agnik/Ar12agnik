class List:
    def __init__(self,data):
        self.data=data
        self.adress=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def create(self,data):
        newNode=List(data)
        if self.head is None:
            self.head=newNode
            self.last=newNode
        else:
            self.last.adress=newNode
            self.last=newNode
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.adress
    def insert_at_front(self,data):
        newNode=List(data)
        newNode.adress=self.head
        self.head=newNode
    def insert_at_random_pos(self,data,pos):
        newNode=List(data)
        temp=self.head
        pos-=2
        while pos>0:
            pos-=1
            temp=temp.adress
            
        newNode.adress=temp.adress
        temp.adress=newNode
    def insert_at_last(self,data):
        self.create(data)
    def delete_from_front(self):
        self.head=self.head.adress
    def delete_at_position(self,pos):
        if pos>1:
            pos-=1
            temp=self.head
            while pos>0:
                prev=temp
                temp=temp.adress
                pos-=1
            prev.adress=temp.adress
    def delete_from_last(self):
        temp=self.head
        while temp is not self.last:
            prev=temp
            temp=temp.adress
        prev.adress=None
    def find_element(self,element):
        c=0
        f=False
        temp=self.head
        while temp is not None:
            if temp.data==element:
                f=True
                return c
            else:
                c+=1
                temp=temp.adress
        if f==False:
            return "Not Found"

    def get_len(self):
        temp=self.head
        c=0
        while temp is not None:
            temp=temp.adress
            c+=1
        return c
    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.adress
            curr.adress = prev
            prev = curr
            curr = next_node
            

        head = prev
        return head
l=LinkedList()
l.create(10)
l.create(20)
l.create(30)
l.create(40)
l.create(50)
l.print_list()
l.reverse()
l.print_list()
print(l.last)