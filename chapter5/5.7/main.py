#An array A[1   n] contains all the integers from 0 to n except for 
#one number which is missing   In this problem, we cannot access an
#entire integer in A with a single opera-tion   The elements of A are 
#represented in binary, and the only operation we can use to access 
#them is “fetch the jth bit of A[i]”, which takes constant time   
#Write code to find the missing integer   Can you do it in O(n) time

A = []
n = 0
NumberAppearing = {}

def GetBit(number , position):
    number = (1 << position) & number
    if number != 0:
        return 1;
    else :
        return 0;
def MarkApearingNumber():
    for number in A:
        #convert number in decimal 
        decimal_number = 0
        for i in range(32):
            decimal_number = decimal_number + (2 ** i) * GetBit(number,i)
        #it means that this number is appearing in A
        NumberAppearing[decimal_number] = 1 
def FindMissingNumber():
   #intiialize NumberAppearing dictionarry
   for i in range(n+1):
        NumberAppearing[i] = 0
   MarkApearingNumber()
   #search from [0,n]
   for num in range(n+1):
      if NumberAppearing[num] != 1:
        return num

#main code
n = int(input("n = "))
for i in range(n):
    current_number = int(input("number "+str(i)+" = "))
    A.append(current_number)

print(str(FindMissingNumber()))