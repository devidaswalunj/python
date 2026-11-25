#3abstract method with no abstract method
#Note
#           if abstract class not have any abstract method we can create a object of that class
 #               in inheritance the parent class is abstract class but not abstract method we can create the object of parent class
  #                  but  that abstract parent class inherited by child and if child have at leat one abstract method we can not create 
  #                 the objet of child class beacuse of the child have abstract class (parent)
from abc import  *
class Parent(ABC):
    def show(self):
        print("this parent show method")

class Child(Parent):
    @abstractmethod
    def m1(self):
        print("this m1 of child")
        self.display()
# c=Child()
# c.m1()
p=Parent()
p.show()




#2 abstract class with abstract method
#note:- if an abstract clas has at leat one abstract method we can not create object of that class
#note:- if child class will not implement the abstract method of paent class then we can not create child class object

# from abc import  *
# class Parent(ABC):
#     def show(self):
#         print("this parent show method")

#     @abstractmethod
#     def m1(self):
#         print("abc")
#         pass

# class Child(Parent):
#     def display(self):
#         print("this display method")
#     def m1(self):
#         print("this m1 of child")
#         self.display()
# c=Child()
# c.m1()
# # p=Parent()
# # p.m1()
# # p.show()




# #1 abstract method
# from abc import *

# class Parent:
#     def show(self):
#         print("parent show method")

#     @abstractmethod
#     def m1(self):
#         pass

# class Child(Parent):
#     def m1(self):
#         print("this is child m1 method")

# c=Child()
# c.m1()
