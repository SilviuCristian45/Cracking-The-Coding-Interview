#You are given a binary tree in which each node contains a value  
#Design an algorithm to print all paths which sum up to that value   
#Note that it can be any path in the tree - it does not have to start at the roo

class TreeNode():
    def __init__(self , info):
        self.data = info
        self.left = None
        self.right = None
#current sum - 0 at first call
#path - list of values
def ShowPossiblePaths(root,sum,current_sum,path):
    if root != None:
        current_sum += root.data
        #print(current_sum)
        path.append(root.data)
        if current_sum == sum:
            print(path)
        ShowPossiblePaths(root.left , sum , current_sum,path)
        ShowPossiblePaths(root.right , sum , current_sum,path)
        #scoatem din lista elementul asta pentru ca trebuie sa se genereze si alte path-uri
        #se executa dupa ce iese din recursivitate
        path.pop()

def InorderTransversal(root , sum):
    if root != None:
        #show the possible paths in the subtree
        path = [] 
        ShowPossiblePaths(root,sum,0,path)
        InorderTransversal(root.left,sum)
        InorderTransversal(root.right ,sum)


root = TreeNode(8)
a = TreeNode(9)
b = TreeNode(12)
c = TreeNode(14)
d = TreeNode(11)
e = TreeNode(15)
g = TreeNode(1)
h = TreeNode(0)

path = []

root.left = a
root.right = b
a.left = c
a.right = g
b.left = d
b.right = e
d.right = h

InorderTransversal(root,31)