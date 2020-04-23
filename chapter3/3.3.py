 #pg 113 3 3 Imagine a (literal) stack of plates   If the stack gets too high, it might topple  
 #Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold  
 #Implement a data structure SetOfStacks that mimics this   SetOfStacks should be composed of several stacks, and should create 
 #a new stack once the previous one exceeds capacity   SetOfStacks push() and SetOfStacks pop() should behave identically
 #to a single stack (that is, pop() should return the same values as it would if there were just a single stack) 
 #FOLLOW UP Implement a function popAt(int index) which performs a pop operation on a specific sub-stack 
class Node():
    data = 0
    next = None
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack():
    top = Node(0)
    def __init__(self,data):
        self.top.data = data
        self.top.next = None
    def push(self,data):
        t = Node(data)
        t.next = self.top
        self.top = t
    def pop(self):
        t = self.top.data
        self.top = self.top.next
        return t
    def lenght(self):
        l = 0
        while (self.top != None):
            l = l+1
            self.pop()
        return l
    def display(self):
        while self.top.next != None:
            print(self.pop())
        print(self.pop())

class SetOfStacks():
    stacks = []
    capacity = 5
    def __init__(self , s):
        self.stacks.append(s)
    
    def push(self , data):
        #if current stack is not at the max capacity
        current_stack = self.stacks[len(self.stacks)-1]
        print("current stack lenght of the stack : "+ str(len(self.stacks)-1) +" "+ str(current_stack.lenght()) + " " + str(data))
        if current_stack.lenght() < self.capacity:
            #add to last stack the data
            self.stacks[len(self.stacks)-1].push(data)
        else:
            #if last stack is at full capacity then i create a new stack . easy boy
            print("new stack")
            new_stack = Stack(data)
            self.stacks.append(new_stack)

    def display(self):
        i = 0
        for stack in self.stacks:
            print("stack : #"+str(i))
            stack.display()
            i += 1
    
            
s = Stack(25)
s.push(41)
s.push(27)  

set_of_stacks = SetOfStacks(s)

set_of_stacks.push(56)
set_of_stacks.push(70)
set_of_stacks.push(89)

set_of_stacks.display()



