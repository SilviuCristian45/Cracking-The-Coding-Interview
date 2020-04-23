#You  have  two  very  large  binary  trees: T1,  with  millions  of  nodes,  
#and T2,  with  hun-dreds of nodes   Create an algorithm to decide if T2 is a subtree of T

class TreeNode():
    def __init__(self , info):
        self.data = info
        self.left = None
        self.right = None
#a,b - TreeNodes
def checkIdenticalTrees(a , b):
    if a == None and b == None:
        #daca a ajuns pana aici inseamna ca toate cheile sunt egale , deci pana aici arborii sunt identici
        return True
    if (a == None and b != None ) or (a != None and b == None):
        return False
    if a.data != b.data:
        return False
    return checkIdenticalTrees(a.left , b.left) and checkIdenticalTrees(a.right , b.right)

#t1,t2 - TreeNodes - roots of trees t1 and t2
#returns if t2 is subtree of t1
def IsSubTree(t1 , t2):
    if t1 == None:
        return False
    else :
        if t1.data == t2.data:
            is_subTree =  checkIdenticalTrees(t1 , t2)
            if is_subTree == True:
                return True
        return IsSubTree(t1.left , t2) or IsSubTree(t1.right , t2)
#Noduri arbore 1
root = TreeNode(7)
a = TreeNode(6)
b = TreeNode(6) 
c = TreeNode(2) 
d = TreeNode(9) 
e = TreeNode(2) 
f = TreeNode(9) 
g = TreeNode(12) 
h = TreeNode(43) 
i = TreeNode(24) 
j = TreeNode(99) 
#Legaturi arbore 1
root.left = a
root.right = b
a.left = c
a.right = d

b.left = e
b.right = f

c.left = g
c.right = h

e.left = i
e.right = j
#Noduri arbore 2
root2 = TreeNode(2)
a2 = TreeNode(24)
b2 = TreeNode(99) 
#Legaturi arbore 2
root2.left = a2
root2.right = b2
print("arbori identici test")
print(checkIdenticalTrees(e,root2))
print("e arborele t2 subarborele lui t1")
print(IsSubTree(root,root2))