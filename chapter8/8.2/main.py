#Imagine a robot sitting on the upper left hand corner of an NxN grid  
#The robot can only move in two directions: right and down  How many possible paths 
#are there for the robot?FOLLOW UPImagine  certain  squares  are “off  limits”,  such  that 
#the  robot  can  not  step  on  them  Design an algorithm to get all possible paths for the robot
n = 3
#matricea
matrix = [[0,0,1],
            [1,0,0],
             [1,0,0]]

def Number_possiblePaths(i , j):
    if i == n-1 or j == n-1:
        matrix[i][j] = 1
        return 1
    if matrix[i][j] != 0:
        return matrix[i][j]
    matrix[i][j] = ( Number_possiblePaths(i+1,j) + Number_possiblePaths(i,j+1) ) 
    return matrix[i][j]

def Number_possiblePaths_slow(i,j):
    if i == n-1 or j == n-1:
        return 1
    return Number_possiblePaths_slow(i+1,j) + Number_possiblePaths_slow(i,j+1)

path = [{0,0}]
def Get_possiblePaths(i , j):
    path.append({i,j})
    if (i+1) < n and matrix[i][j] != 1:
        Get_possiblePaths(i+1,j)
    if (j+1) < n and matrix[i][j] != 1:
        Get_possiblePaths(i,j+1)

Get_possiblePaths(0,0)
print (path)
#print(Number_possiblePaths(0,0))
#print (matrix[0][0])





