#inheritance- we create a class then create another class and inherit the other classes' attributes and functions in new class

class Chef:
    def make_chicken(self):
        print("The chef can make chicken")
    def make_salad(self):
        print("The chef makes a salad")
    def make_special_dish(self):
        print("The chef makes bbq ribs")
mychef = Chef()#object is created
mychef.make_special_dish() #obj used func of class


#creating a chinese chef class...it can already do what a normal chef can do and also do extra things
#so we inherit all the attributes and functions of normal chef
class ChineseChef(Chef): #it inherits all functions and attributes of chef class in it
    def make_special_dish(self):
        print("Make orange chicken") #we can change inherited funtions for the new class
    def make_fried_rice(self):
        print("The chef makes fried rice.")
my_chinese_chef = ChineseChef() #object of chinese chef class
my_chinese_chef.make_fried_rice() #function defined in the class
my_chinese_chef.make_salad() #by inheritance the objects have access to inherited classes' functions
my_chinese_chef.make_special_dish()