#fresher
class Fresher():
    canHandleCall = True
#technical lead
class TL():
    canHandleCall = True
#project manager
class PM():
    canHandleCall = True
class Employees():
    freshers = []
    def __init__(self,fresher,tl,pm):
        self.freshers.append(fresher)
        self.tl = tl
        self.pm = pm
    def addFresher(self,fresh):
        self.freshers.append(fresh)
    def getCallHandler(self):
        i = 0
        for fresher in self.freshers: 
            if fresher.canHandleCall == True:
                print("The call was handled by fresher #"+str(i))    
                fresher.canHandleCall = False
                return
            i+=1
        if self.tl.canHandleCall == True:
            print("The call was handled by techlead ")    
            self.tl.canHandleCall = False
            return
        if self.pm.canHandleCall == True:
            print("The call was handled by project manager ")    
            self.pm.canHandleCall = False
            return
        
