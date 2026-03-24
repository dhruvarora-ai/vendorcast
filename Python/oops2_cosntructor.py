class Item:
    pay_rate = 0.8 
    all = [] #it is made to contain all objects

    def __init__(self,name: str, price: float, quantity=0):
        assert price>0 
        assert quantity>=0
        
        self.name = name
        self.price = price
        self. quantity = quantity

        Item.all.append(self) #self-each instance when created, the list will be appended with the instances/objects
    def calc_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
         return f"Item('{self.name},{self.price},{self.quantity}')"

item1 = Item("Phone",100,1)
Item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",58,5)
item5 = Item("Keyboard",75,5)

#to store multiple objects in a list. We create a list of all objects in the class

print(Item.all) #prints the list of all objects

for instance in Item.all:
    print(instance.name)
    instance.apply_discount()
    print("Total price:",instance.calc_total_price())


class Product:
    pay_rate = 0.8
    def __init__(self,name:str,price:float,quantity:int):
        assert price>0
        assert quantity>=0
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calc_total_amount(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
products = []
n = int(input("Enter no of objects you want"))
for i in range(n):
    p_name = input("Enter product name: ")
    p_price = float(input("Enter product price: "))
    p_quantity = int(input("Enter Product Quantity"))
    product = Product(p_name,p_price,p_quantity)
    products.append(product)

for item in products:
    if item.name.lower() == "car":
        item.pay_rate = 0.7
        print("Original total price of",item.name,"is",item.calc_total_amount())
        item.apply_discount()
        print("Price after discount",item.calc_total_amount())

    else: 
        print("Original total price of",item.name,"is",item.calc_total_amount())
        item.apply_discount()
        print("Price after discount",item.calc_total_amount())
