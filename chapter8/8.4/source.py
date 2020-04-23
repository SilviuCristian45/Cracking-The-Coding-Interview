#Write a method to compute all permutations of a string
import itertools

string = "abcd"

def Permuration_N(n):
    return list(itertools.permutations(string,n))

print (Permuration_N(len(string)))