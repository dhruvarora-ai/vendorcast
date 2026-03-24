class Item:
    def __init__(self,name): #we create attributes here for future  objects which will be created for the class
        print(f"An instance created: {name}")
    def calc_total_price(self,x,y):
        return x*y
item1 = Item("Phone") #each time the object calls init function
item1.name = "Phone"
item1.price = 100
item1.quantity  = 5

item2 = Item("Laptop")
item2.name = "Laptop"
item2.price = 500
item2.quantity = 10

print("Wait")
#we use self in the init method to prevent the manual assignment of attributes to the class objects
#class attributes- applicable to all objects- eg sale attribute to every item
class Item:
    pay_rate = 0.8 #this is class attribute. The pay rate after 20% discount is 0.8.

    def __init__(self,name:str,price:float,quantity=0): #we create attributes here for future  objects which will be created for the class
    #we can give default values to attributes of objects and change them in object declaration
    #we never want negative price aur quantity entry
        assert price >0, f"price {price} is not greater than zero" # to solve this we use assert, this sets rules for object attributes
        assert quantity>=0 ,f"quantity is not 0 more" #this prints assertion error
        self.name = name #the name attribute gets the declared value in object declataion
        self.price = price
        self.quantity = quantity

    def calc_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate #using the class attribute to apply discount
item1 = Item("Phone",100,25) #each time the object calls init function


item2 = Item("Laptop",500,10)

item1.has_numpad = False #we can make attributes outside the classes still
print(item1.quantity)
print(item2.quantity)
print(item1.has_numpad)

print(Item.pay_rate) #access the class attribute from class
print(item1.pay_rate) #access the class attribute from object
#since class attribute can be applied to all objects

print(Item.__dict__) #all attributes of class level
print(item1.__dict__) #all attributes of object

print("Item 2 price:",item2.calc_total_price())
item2.apply_discount() #first alter the price using class attribute
print("Item 2 discounted price: ",item2.calc_total_price()) #prints discounted amount

#for diff items we want diff discounts, So instead assign class attribute to the object
item1.pay_rate = 0.7
item1.apply_discount()
print(item1.calc_total_price())

