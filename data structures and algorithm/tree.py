class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class Tree:
    def __init__(self):
        self.root=None
    def create(self,data):
        newNode=node(data)
        current_root=self.root
        if current_root is None:
            self.root=newNode
        else:
            while True:
                if data>current_root.data:
                    if current_root.right is None:
                        current_root.right=newNode
                        break
                    else:
                        current_root=current_root.right
                else:
                    if current_root.left is None:
                        current_root.left=newNode
                        break
                    else:
                        current_root=current_root.left
t=Tree()
t.create(12)
t.create(16)
t.create(13)
t.create(1)
t.inorder_traversal(t)