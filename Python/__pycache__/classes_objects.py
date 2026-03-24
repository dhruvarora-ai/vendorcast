#not all things can be represted bin strings, int, list, bools
#so we can create our own datatype in python eg- we can create a datatype for our phone
#we do this by using classes and objects

#eg- model a student
class Student: # a student class. we can create attributes for a student in this class using in built python datatypes  
    def __init__(self, name, major,gpa, is_on_probation): #initialize function, in this function we can map out attributes of student - name, gpa, major,(students attributes are defined)
        self.name = name
        self.major = major 
        self.gpa =  gpa
        self.is_on_probation = is_on_probation
    #class is just defining what student datatype is, whereas object is a real student having those datatype values filled
    