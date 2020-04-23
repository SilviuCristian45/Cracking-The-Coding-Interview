#You  are  given  two  32-bit  numbers,  N  and  M,  and  two  bit  positions,  i  and  j  Write  a method to set all bits between i and j in N equal to M 
#(e g  , M becomes a substring of N located at i and starting at j)   EXAMPLE:Input: N = 10000000000, M = 10101, i = 2, j = 6Output: N = 10001010100

#N = int(input("N = "))
#M = int(input("M = "))
N = 21
M = 0
j = 3
i = 1
#k - number of bits in M 
k = j-i
def GetBit(number,position):
    val =  (1 << position) & number
    if val != 0:
        return 1
    else:
        return 0
#if current Bit is 0 then it changes it to 1
# if current bit is 1 then it changes it to 0 
def setBit(number,position):
    val = number
    val = (1 << position) ^ number
    return val
#!!!!!!!!!!!!!!!!!!         TESTING FUNCTIONS           !!!!!!!!!!!!!!!!!!!!
#print (GetBit(5,0))
#val = setBit(5,0)
#print(val)

while j >= i:
    bit_curent_N = GetBit(N , j)
    bit_curent_M = GetBit(M , k)
    if bit_curent_M != bit_curent_N:
        N = setBit(N,j)
    j -= 1
    k-=1
    
print(bin(N))