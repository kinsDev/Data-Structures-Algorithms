# Challenge 2: Calculate the Student's Performance
class Student:
    # initializer
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    
    # methods
    def totalObtained(self):
        # instance variable
        marksObtained = self.phy + self.chem + self.bio 
        return marksObtained  # marksObtained is a local method within the totalObtained method
    # to get the total marks I should call the totalObtained method
    def percentage(self):
        return (self.totalObtained()/300) * 100

Obj1 = Student("Mark", 80, 90, 40)

print("Total marks obtained:", Obj1.totalObtained())
print("Percentage of total marks obtained:", Obj1.percentage())