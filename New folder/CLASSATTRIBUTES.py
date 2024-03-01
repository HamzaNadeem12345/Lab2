import csv


class Item():
    pay_rate = 0.8 # This a class attribute
    all = []
    def __init__(self,name,price,quantity=0):
        # run validations to the recived arguments
        assert price>=0, f"Price {price} is not greater than 0!!!!!!"
        assert quantity>=0
        
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity
    

    def apply_discount(self):
        self.price = self.price*self.pay_rate # payrate cant be changed without using self.payrate
    
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point 0 ex 5.0,10.0 etc
        # count out the floats that are point zero
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            False
    
    
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price},{self.quantity})"





# item1 = Item("Phone",100,1)
# # item2 = Item("Laptop",1000,3)

# # print(item1.calculate_total_price())
# # print(item2.calculate_total_price())
# # print(Item.pay_rate)
# # print(item1.pay_rate)
# # print(item2.pay_rate)
# item1.apply_discount()
# print(item1.price)

# item2 = Item("Laptop",1000,3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,55)

print(Item.all)

for instance in Item.all:
    print(instance.name)



print(Item.is_integer(7.0))


























































# YOU WANT TO MAKE USE OF AN ATTRIBUTTE THAT IS GLOBAL OR ACROSS ALL THE INSTANCES
# YOU WANT TO APPLY A SALE ON YOUR SHOP
# Having the control to apply a discount to each one of the items
# this is a good candidatee of  creating an attribute that can be shared across all the instances
# class attribute is an attribute that belongs to the ckass itself
# however you can also access this attribute from the instance level as well


# WHEN TO USE CLASS METHOD AND WHEN TO USE STATIC METHOD