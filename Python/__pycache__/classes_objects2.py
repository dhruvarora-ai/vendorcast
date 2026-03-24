from classes_objects import Student

student1 = Student("Jim","Business",3.1,False) #student object is an instance of a class, it is a real student which has all defined attributes filled with values
student2 = Student("Dhruv","Cse",4.0,True)
print(student1.name) #printing attributes of students
print(student1.gpa)
print(student2.is_on_probation)

#the initialize function defines attributes of the Student datatype

