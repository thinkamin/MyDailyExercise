class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def depth(root):
    if root is None:
        return 0
    else:
        return 1+max(depth(root.left),depth(root.right))

def output_in_order(root):
    if root is None:
        return 
    output_in_order(root.left)
    print(root.data)
    output_in_order(root.right)
    
def insert(root,new):
    if root is None:
        return new
    else:
        if new.data<root.data:
            root.left=insert(root.left,new)
        else:
            root.right=insert(root.right,new)
        return root
def delete(root,dltnode):
    if root is None:
        success=False
        return root

    print('dltnode',dltnode.data,type(dltnode))
    print('root',dltnode.data,type(root))
    if dltnode.data<root.data:
        root.left=delete(root.left,dltnode)
    elif dltnode.data>root.data:
            root.right=delete(root.right,dltnode)
    else:
        dltnode=root
        if not root.left:
            newroot=root.right
            success=True
            return newroot
        else:
            if not root.right:
                newroot = root.left
                success=True
                return newroot
            else: 
                exch=root.left
                while exch.right:
                    exch=exch.right
                hold = root
                root.data = exch.data
                exch=hold
                root.left=delete(root.left,exch)
    return root




n1 = node(5)
tree = insert(None,n1)
n2 = node(3)
tree = insert(tree,n2)
n3 = node(10)
tree = insert(tree,n3)
n4 = node(7)
tree = insert(tree,n4)
print('output_in_order',output_in_order(tree))
print('depth',depth(tree))

tree=delete(tree,n1)
print(output_in_order(tree))
