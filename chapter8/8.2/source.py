f = open("input.txt","r")
matrix = []
n = 0

class Point():
    def __init__(self,i,j):
        self.i = i
        self.j = j

def Read():
    n = int(f.readline())
    line = f.readline()
    while (line):
        line = line.split(' ')
        number_line = []
        for num in line:
            number_line.append(int(num))
        matrix.append(number_line)
        line = f.readline()
    return n

def Print_Matrix():
    for i in range(0,n):
        print(matrix[i])

def isOk(i , j):
    #check if it is in the bounds and if the element(ij) is not a wall
    if i <= (n-1) and j <= (n-1) and matrix[i][j] != 0:
        return True
    return False

def Print_path(path):
    for point in path:
        print(str(point.i) + " " + str(point.j))

path = []
def GetPath(i , j):
    path.append(Point(i,j))
    if i == (n-1) and j == (n-1):
        #afisam drumul
        print("path = ")
        Print_path(path)
    #south neighbour
    if isOk(i+1,j):
        GetPath(i+1,j)
    #east neighbour
    if isOk(i ,j+1):
        GetPath(i,j+1)
    #daca a ajuns aici inseamna ca nu face parte din drum     
    path.pop()

n = Read()
GetPath(0,0)

