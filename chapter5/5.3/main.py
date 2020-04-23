#Given an integer, print the next smallest and next largest number that 
#have the same number of 1 bits in their binary representation 

n = int(input("n = "))
#get current bit (in number num ) at position pos
def GetBit(num , pos):
    val = (1 << pos) & num
    if val != 0:
        return 1
    return 0

#if current bit is 0 , set it to 1 . if current bit is 1 , set it to 0
def SetBit(num , pos):
    return (1 << pos) ^ num

def GetNextMax(number):
    index = 0
    while index < 32:
        bit_right = GetBit(number,index)
        index+=1
        bit_left = GetBit(number,index)
        if bit_right == 1 and bit_left == 0:
            index -= 1
            number = SetBit(number , index)
            index += 1
            number = SetBit(number , index)
            return number

def GetNextMin(number):
    index = 0
    while index < 32:
        bit_right = GetBit(number,index)
        index+=1
        bit_left = GetBit(number,index)
        if bit_right == 0 and bit_left == 1:
            index -= 1
            number = SetBit(number , index)
            index += 1
            number = SetBit(number , index)
            return number


print("next max : " +  str(GetNextMax(n)))
print("next min : " +  str(GetNextMin(n)))