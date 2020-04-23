#107 2 4 You have two numbers represented by a linked list, where each node contains a single digit   
# The digits are stored in reverse order, such that the 1’s digit is at the head of the list  
#  Write a function that adds the two numbers and returns the sum as a linked list EXAMPLE  Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
class Node():
    next = None
    data = 0
    # constructor
    def __init__(self,data):
        self.data = data

    def insert_node(self,val):
        x = Node(val)
        first = self
        while first.next != None:
            first = first.next
        first.next = x

    def display_list(self):
        current = self
        while current.next != None:
            print(current.data)
            current = current.next
        print(str(current.data))

    def generate_number(self):
        power = 0
        number = self
        generated_number = 0

        while number.next != None:
            generated_number = generated_number + pow(10,power)*number.data
            number = number.next
            power+=1
        
        generated_number = generated_number + pow(10,power)*number.data

        return generated_number



    def sum(self, number2): 
        number1 = self
        transport = 0

        the_sum = Node( (number1.data + number2.data)%10 )
        transport = (number1.data + number2.data)/10

        number1 = number1.next
        number2 = number2.next

        while number1.next != None  and number2.next != None:
            the_sum.insert_node(int((number1.data + number2.data + transport)%10))
            transport = int((number1.data + number2.data + transport)/10)
            number1 = number1.next
            number2 = number2.next

        #take care for the last digit
        the_sum.insert_node(int((number1.data + number2.data + transport)%10))
        transport = int((number1.data + number2.data + transport)/10)
        if transport != 0 :
            the_sum.insert_node(transport)

        return the_sum


#main code
num1 = int(input("number1 = "))
num2 = int(input("number2 = "))

num1_list = Node(num1%10)
num1 = int(num1/10) 

while num1 != 0:
    cifra = num1%10
    num1_list.insert_node(cifra)
    num1 = int(num1 / 10)

num2_list = Node(num2%10)
num2 = int(num2/10)

while num2 != 0:
    num2_list.insert_node(num2%10)
    num2 = int(num2/10)

sum_list = num1_list.sum(num2_list)

the_sum = sum_list.generate_number()

print("the sum of the two numbers is = " + str(the_sum))