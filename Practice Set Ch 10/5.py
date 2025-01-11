# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

class Train: 
    name = ""
    def __init__(self,name):
        self.name = name 
    
    def book(self):
        name = self.name
        print(f"The Train {name} is Booked")
    
    def getStatus(self):
        name = self.name
        print(f"The Train {name} time is []")
    
    def getInfo(self):
        name = self.name
        print(f"The Train {name} Info is []")
        

o = Train("A")
o.book()
o.getStatus()
o.getInfo()
