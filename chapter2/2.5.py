#pg 108 2 5 Given a circular linked list, implement an algorithm which returns node at the beginning of the loop DEFINITION Circular linked list: 
# A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list EXAMPLE input: A -> B -> C -> D -> E -> C 
# [the same C as earlier] output: 

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def append_node(self , data):
        node = self
        new_node = Node(data)
        while node.next != None:
            node = node.next
        node.next = new_node

    def display_list(self):
        node = self
        while node.next != None:
            print(str(node.data))
            node = node.next
        print(str(node.data))

lista1 = Node(4)
lista1.append_node(65)
lista1.append_node(45)

lista1.display_list()