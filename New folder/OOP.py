class Item():
    def __init__(self,name,price,quantity=0):
        # run validations to the recived arguments
        assert price>=0, f"Price {price} is not greater than 0!!!!!!"
        assert quantity>=0
        
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity
    
item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())


























# class  Item():
#     def __init__(self,name,price,quantity): 
#         self.name = name # if we use this we dont have to assign name for each object
#         self.price = price
#         self.quantity = quantity
# can also do def __init__(self,name,price,quantity=0)        
# now we dont need to add value for quantity below
# item1 = Item("phone",100,5)
# item2 = Item("Laptop",45,36)



# print(item2.name)
# print(item1.name)

# print(item2.price)
# print(item2.quantity)



# you can assign attributes to specific instances individually 


# print(item1.price)
# print(item1.quantity)
















# class Item():
#     def __init__(self):
#         print("I AM CREATED")


# item1 = Item() # instance/item 1 allows init method to be called
# item2 = Item() # instance/item2 allows init method to be called





















# class Item():
#     def calculate_total_price(self,x,y):
#      return x*y
# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price,item1.quantity))

# item2 = Item()
# item2.name = 'Laptop'
# item2.price = 1000
# item2.quantity = 3


# functions inside classes are methods
# def init also called constructor




















# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))
# # each data type is an object that has been instantiated earlier by some class
# # for item1 variable that has been instantiated by string type class
# # price quantity and total have been instantiated by int class


# # FIRST WE WILL CREATE A CLASS
# # AND THEN WE WILL INSTANTIATE SOME OBJECTS OF THIS CLASS
# # creating an instance and creating an object means the same thing

# class Item:
#     pass
# item1 = Item() # we have just created an instance of a class
# randomstr = str(4) random str is instance of str class


    

    



