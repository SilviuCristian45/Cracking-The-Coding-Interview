#Write  a  function  to  determine  the  number  
#of  bits  required  to
#convert  integer  A  to integer BInput: 31, 14Output: 2
a = 31
b = 14
bit_pos = 0
nr = 0

def GetBit(number , position):
    val = (1 << position) & number
    if val == 0:
        return 0
    else :
        return 1

while bit_pos < 32:
    #ia bitul de pe pozitia bit_pos din A
    bit_a = GetBit(a,bit_pos)
    #ia bitul de pe pozitia bit_pos din B
    bit_b = GetBit(b,bit_pos)
    #daca is diferiti bitii , cresti nr++ 
    if bit_a != bit_b:
        nr+=1
    bit_pos+=1

print(str(nr))