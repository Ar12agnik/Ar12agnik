class node:
    #create a node
    def __init__(self,data):
        self.data=data
        self.adress=None
class LinkedList:
    def __init__(self):
        #assigning head,last None because till now no node is created
        self.head=None
        self.last=None
    def createList(self,data):
        newnode=node(data)
        #create a node and assign the adress to newnode
        if self.head is None:#checks if the node created is 1st node or not
        #if node created is first node then head,last will point at the first
        #node
            self.head=newnode
            self.last=newnode
        else:
            #if node created is not the first node
            #then assign the new node's adress to last node and make the last 
            #point at the new node
            self.last.adress=newnode
            self.last=newnode
    def printList(self):
        temp=self.head
        str1=''
        while temp is not None:
            str1+=str(temp.data)+'-->'
            temp=temp.adress
        print(str1)
    def find_element_at_index(self,index):
        count=0
        temp=self.head
        if index==0:
            print(f"Element at index {index} is {temp.data}")
        while temp is not None:
            
            count+=1
            temp=temp.adress
            if (count==index-1):
                print(f"element at index {index} is{temp.adress.data}")
                break
            
x=LinkedList()
x.createList(9)
x.createList(10)
x.createList(11)
x.createList(12)
x.createList(13)
x.createList(14)
x.createList(15)
x.createList(16)
x.createList(17)
x.find_element_at_index(int(input("enter index number: ")))
x.printList()