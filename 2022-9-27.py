# from my import gen_num
# from collections import namedtuple
#from my import G1,G2
#from collections import deque
# num_lst = gen_num()

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def depth(root):
    if root is None:
        return 0
    else:
        return 1+max(depth(root.left),depth(root.right))

def input_in_order(root):
    if root is None:
        return 
    input_in_order(root.left)
    print(root.data)
    input_in_order(root.right)

# 查找
def search1(root,value):
    if root is None or root.data=data:
        return root
    if root.data>value:
        return search1(root.left,value)
    if root.data<value:
        return search1(root.right,value)

def deletenode(root,value):
    if root is None:
        return False
    if value<root.data:
        return deletenode(root.left,value)
    elif value>root.data:
        return deletenode(root.right,value)
    else:
        #找到了 看是不是叶节点
        if root.left and root.right:
            temp = findmax(root.left)
            root.data=temp.data
            root.right = deletenode(root.left,temp.data)
        elif root.right ==None and root.left==None:
            root = None;
        elif root.right==None:
            root=root.left
        elif root.left ==None:
            root = root.right
    return root

def insert(root,value):
    if root == None:
        root = Node(value)
    elif value<root.data:
        root.left = insert(root.left,value)
    elif value>root.data:
        root.right= insert(root.right,value)
    return root
            




