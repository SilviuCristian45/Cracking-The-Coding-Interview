#Write an algorithm to find the ‘next’ node (i e , in-order successor) of a given node in a binary search tree 
# where each node has a link to its parent.
from TreeNode import TreeNode

def InsertNode(root , new_node):
    if(root.left == None and root.right == None):
        if new_node.data > root.data:
            root.right = new_node
        else :
            root.left = new_node
        if new_node.data < root.data:
            return InsertNode(root.left , new_node)
        else:
             return InsertNode(root.right , new_node)


# Case I : when the node has a subtree
# works
def MinKeyNode(root):
    #if root its a leaf
    if root.left == None and root.right == None:
        return root.data
    else :
        return MinKeyNode(root.left)

#Case II : when the node has not a subtree
def CaseII(root):
    if root.parent.left == root:
        return root.parent.data
    else :
        return CaseII(root.parent)

#In Binary Search Tree, Inorder Successor of an input node can also be defined as the node with the smallest
#key greater than the key of input node. So, it is sometimes important to find next node in sorted order.
#root - TreeNode 
def InOrderSuccesor(root):
    #it means that a subtree exists
    if root.right != None:
        print(MinKeyNode(root.right))
    else :
        print(CaseII(root))


#main
root = TreeNode(20)
a = TreeNode(8)
b = TreeNode(22)
c = TreeNode(4)
d = TreeNode(12)
e = TreeNode(10)
f = TreeNode(14)
#legaturi arbore
root.left = a
root.right = b
a.parent = root
b.parent = root
a.left = c
a.right = d  
c.parent = a
d.parent = a
d.left = e
d.right = f
e.parent = d
f.parent = d

u = TreeNode(16)
InsertNode(root , u)
print(InOrderSuccesor(a))