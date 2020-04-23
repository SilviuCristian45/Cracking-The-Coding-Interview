class TreeNode():
    def __init__(self,info):
        self.data = info
        self.left = None
        self.right = None
        self.parent = None

def GetNodeLevel(root , a , level):
    if root == None:
        return 0
    if(root.data == a.data):
        return level
    else :
        l = GetNodeLevel(root.left , a , level+1)
        #ideea aici e ca de exemplu daca il gaseste in stanga
        #chiar daca il returneaza sus , el se intoarce la linia
        # cu apelul getNodeLevel(root.right) . si il tot cauta 
        # dar nu il mai gaseste 
        # ideea e ca dupa apelul in subarborele stang 
        # tre verficat daca a fost gasit inca odata 
        # si la fel si dupa apelul in subarborele drept 
        # asta e treaba
        if l != 0: return l
        l = GetNodeLevel(root.right , a , level+1)
        return l

#a ,b - TreeNodes
#a_level , b_level - integers 
def firstAncestor(a , b , a_level , b_level):
    #print("lv_a" + str(a_level))
    #print("lv_b" + str(b_level))
    if a.parent == None:
        return 
    if a.parent.data == b.parent.data:
        return a.parent.data
    if a_level > b_level:
        return firstAncestor(a.parent , b , a_level-1 , b_level)
    else :
        if a_level < b_level:
            return firstAncestor(a , b.parent , a_level , b_level-1)
        else :
            return firstAncestor(a.parent , b.parent , a_level , b_level)


#Noduri arbore
root = TreeNode(7)
a = TreeNode(6)
b = TreeNode(10) 
c = TreeNode(2) 
d = TreeNode(9) 
e = TreeNode(3) 
f = TreeNode(15) 
g = TreeNode(22) 
#Legaturi arbore
root.left = a
root.right = b
a.parent = root
b.parent = root

a.left = c
a.right = d
c.parent = a
d.parent = a

b.left = e
b.right = f
e.parent = b
f.parent = b

e.left = g
g.parent = e

#print(GetNodeLevel(root , e , 0))

firstNode = e
secondNode = f
firstNode_level = GetNodeLevel(root , firstNode , 0)
secondNode_level = GetNodeLevel(root , secondNode , 0)

print("first common ancestor ")
print(firstAncestor(firstNode,secondNode,firstNode_level,secondNode_level))