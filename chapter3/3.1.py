#Describe how you could use a single array to implement three stacks 

#first stack would be from 0 to n/3-1
#second stack would be from n/3 to 2*n/3-1
#third stack would be from 2*n/3 to n-1
        #0 1 2 3 4 5 6
class Node():
    data = 0
    next = None
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack():
    top = Node(0)
    def __init__(self,top):
        self.top.data = top
        self.top.next = None

    def push(self,top):
        t = Node(top)
        t.next = self.top
        self.top = t
    
    def pop(self):
        if self.top != None :
            #delete the top
            the_data = self.top.data
            self.top = self.top.next
            #return the top data 
            return the_data
        else :
            return None

array = [4,5,6,7,21,231,43,6]
n = len(array)
i = 1
s1 = Stack(array[0])
#first stack
while i <= n//3:
    s1.push(array[i])
    i+=1

s2 = Stack(array[i])
while i <= 2*n//3:
    s2.push(array[i])
    i+=1

s3 = Stack(array[i])
while i < n:
    s3.push(array[i])
    i+=1









