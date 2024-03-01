class Item():
 pass
# WE USE STATIC METHOD WHEN WE WANT TO DO SOMETHING THAT SHOULD NOT BE UNIQUE PER INSTANCE
# ISinteger only checks if a number is integer or not
# we cant we just write method normally?
# this is a method that has nothing to do with the instance its somehow related to item class
# if we want to instantiate an instance from structural data that we own we use class method
# for example creating a class method that is responsible to read the csv final
# class methods used to manipulate different structures of data to instantiate objects

# DIFFERENCE BETWEEN CLASS METHODS AND STATIC METHODS
# static method are not passing the object reference as the first argument in the backround
# class methods and static methods can only be called from the class level. But however, those also couldbe called from instances.
# so as you can see, I can instantiate the object
