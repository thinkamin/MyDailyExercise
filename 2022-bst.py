class node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class bst:
    def __init__(self,root=None):
        self.root=root
        self.count=0

    def compare(self,node1,node2):
        return node1.data-node2.data

    def insert(self,node):
        if self.count==0:
            self.root=node
        else:
            self._insert(node)
        self.count+=1

    def _insert(self,node):
        if self.compare(node,self.root)>0:
            self.root.left=self._insert(self.root.left,node)
        else:
            self.root.right=self._insert(self.root.right,node)

n1 = node(5)
bst= bst()
bst.insert(n1)
print(bst.count)
n2 = node(3)
bst.insert(n2)
print(bst.count)



