#Imagine you have a call center with three levels of employees: 
#fresher, technical lead (TL), product manager (PM)  
#There can be multiple employees, but only one TL or PM 
#An  incoming  telephone  call  must  be  allocated 
#to  a  fresher  who  is  free     If  a  fresher can’t  
#handle  the  call,  he  or  she  must  escalate  the  call 
#to  technical  lead     If  the TL  is not free or not able
#to handle it, then the call should be escalated to PM  
#Design the classes and data structures for this problem  
#Implement a method getCallHandler() 
from Employees import Fresher
from Employees import TL
from Employees import PM
from Employees import Employees

fresher = Fresher()
fresher1 = Fresher()
fresher2 = Fresher()
fresher3 = Fresher()
techlead = TL()
projectmanager = PM()

employees = Employees(fresher,techlead,projectmanager)
employees.addFresher(fresher1)
employees.addFresher(fresher2)
employees.addFresher(fresher3)

employees.getCallHandler()