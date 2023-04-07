class node:
    def __init__(self,data):
        self.lson=None
        self.rson=None
        self.data=data 
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        newNode=node(data)
        if self.root is None:
            self.root=newNode
        else:
            temp=self.root
            while temp is not None:
                prev=temp
                if data>temp.data:
                    temp=temp.rson
                else:
                    temp=temp.lson
            if data>prev.data:
                prev.rson=newNode
            else:
                prev.lson=newNode
    def inorder(self,root):
        if root.lson is not None:
            self.inorder(root.lson)
        print(root.data)
        if root.rson is not None:
            self.inorder(root.rson)
    def preorder(self,root):
        print(root.data)
        if root.lson is not None:
            self.inorder(root.lson)
        if root.rson is not None:
            self.inorder(root.rson)
    def postorder(self,root):
        if root.lson is not None:
            self.postorder(root.lson)
        if root.rson is not None:
            self.postorder(root.rson)
        print(root.data)       
t=Tree()
t.insert(59)
t.insert(21)
t.insert(31)
t.insert(69)
t.insert(6)
t.insert(0)
t.inorder(t.root)    
t.preorder(t.root)
t.postorder(t.root)