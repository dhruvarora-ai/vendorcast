item0 = "Phone"
item0_price = 100
item0_quantity = 5
item0_total_price = item0_price*item0_quantity 
#all these are just variables for python

class Item:
    def calc_total_price(self,x,y):
        return x*y
    

item1 = Item() #onbject of class
item1.name = "Phone" #All these are attributes of the object defined in class 
item1.quantity = 5
item1.price = 100
print(item1.calc_total_price(item1.quantity,item1.price))



