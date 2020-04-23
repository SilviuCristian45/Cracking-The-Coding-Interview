class board_box():
    isOccupied = False
    line = 0
    column = 0
    piece = ""
    team = ""
    def __init__(self,line,column,piece,team):
        self.line = line
        self.column = column
        self.isOccupied = False
        self.piece = piece
        self.team = team
class board():
    boxes = []
    def __init__(self):
        #up team is black
        matrix = [["t","h","b","q","k","b","h","t"],
                ["p","p","p","p","p","p","p","p"] ,
                [" "," "," "," "," "," "," "," "] ,
                [" "," "," "," "," "," "," "," "] ,
                [" "," "," "," "," "," "," "," "] , 
                [" "," "," "," "," "," "," "," "] ,
                ["p","p","p","p","p","p","p","p"], 
                ["t","h","b","q","k","b","h","t"]
                ]
        for i in range(8):
            line = []
            for j in range(8):
                box = board_box(i,j,matrix[i][j],"")
                if i <= 1:
                  box.team = "w" #white team
                else :
                  if i >= 6:
                    box.team = "b" #black team
                line.append(box)
            self.boxes.append(line)
                
    def print(self):
        for i in range(8):
           print()
           for j in range(8):
                print(self.boxes[i][j].piece,end=" ")