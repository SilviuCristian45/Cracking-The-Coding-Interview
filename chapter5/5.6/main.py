#Write a program to swap odd and even bits in an integer with as 
#few instructions as possible (e g  , bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc)
n = 23

def Solve(num):
    #0xAAAAAAAA is the 32 bit number where
    #0 is positioned to an odd bit
    #1 is positioned to an even bit
    
    #get all even bits of num
    n1 = (0xAAAAAAAA & num) >> 1
    #get all odd bits of num
    n2 = (0x5555555 & num) << 1
    return n1 | n2
    

print (Solve(n))