# Write a method that returns all subsets of a set
import itertools 

Set = set((1,2,3))

#return a list of subsets of n lenght
def Return_nSubsets(n):
    return list(itertools.combinations(Set,n))
#print all subsets of set 
def Print_allSubsets():
    for i in range(1,len(Set)+1):
        print(Return_nSubsets(i))

Print_allSubsets()