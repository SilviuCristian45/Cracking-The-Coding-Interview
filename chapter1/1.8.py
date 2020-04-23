#Assume you have a method isSubstring which checks if one word is a substring of another . Given two strings, s1 and s2, write code to check if 
#s2 is a rotation of s1 using only one call to isSubstring
#(i e , “waterbottle” is a rotation of “erbottlewat”) 
#s1 = input("string1 = ")
#s2 = input("string2 = ")
s1 = "waterbottle"
s2 = "erbottlewat"

i = 0
#suppose that is not rotation
ok = 0
while i < len(s1):
    #cauta s1:i in s2 ca sa afli pozitia de la care incepe bottle in s2
    substring_s1_stanga = s1[0:i+1]
    substring_s1_dreapta = s1[i+1:]

    print(substring_s1_stanga + " " + substring_s1_dreapta)
    
    presupus_s2 = substring_s1_dreapta + substring_s1_stanga

    if s2 == presupus_s2 :
        ok = 1
    i += 1

if ok == 1:
    print("s2 is a rotation of s1")
else :
    print("s2 is NOT a rotation of s1")
