class Student:
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self): #we can create a func inside a class and all student objects can access that
        if self.gpa >= 3.5: #if students objects gpa>=3.5
            return True
        else:
            False
    #using functions in classes help us to perform various tasks on its objects
