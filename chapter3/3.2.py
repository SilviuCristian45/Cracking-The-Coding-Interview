#pg 111 3 2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element?
#Push, pop and min should all operate in O(1) time

#Algorithm
#the idea is to keep the in each node of the stack the number smaller than him
#we build the stack this way .
#and when we return the minimum element we just return the minValue of the top node of the stack
#and that operates in O(1) time

class Node():
    data = 0
    next = None
    minValue = 32000
    def __init__(self,data):
        self.data = data
        next = None

class Stack():
    top = Node(0)
    def __init__(self,top):
        self.top.data = top
        self.top.next = None
        self.top.minValue = top

    def push(self,top):
        t = Node(top)
        t.next = self.top
        minValue = min(top , self.min())
        t.minValue = minValue
        self.top = t
        
    def pop(self):
        if self.top != None :
            item = self.top.data
            self.top = self.top.next
            return item
        else :
            return None
    def min(self):
        return self.top.minValue
        
s = Stack(5)
s.push(25)
s.push(2)
s.push(720)

print(s.min())