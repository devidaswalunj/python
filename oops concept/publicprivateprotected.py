#accesing the private member outside the class
class  Parent():
    __a=10
    def __init__(self):
        self.__b=20
    def display(self):
        print("__a",Parent.__a)
        print("__b",self.__b)
class Child(Parent):
        def display(self):
            self.p1=Parent()
            print("__a",self.p1._Parent.__a)
            print("__b",self.p1._Parent.__b)
c=Child()
c.display()
# p=Parent()
# p.display()
# print("out side class __a", p._Parent__a)
# print("out side class __b", p._Parent__b)



#protected
# class  Parent():
#     _a=10
#     def __init__(self):
#         self._b=20
#     def display(self):
#         print("_a",Parent._a)
#         print("_b",self._b)
# class Child(Parent):
#         def display(self):
#             print("_a",Parent._a)
#             print("_b",self._b)
# c=Child()
# c.display()
# p=Parent()
# p.display()
# print("a outside :", Parent._a)
# print("b outside :", p._b)
 




#private 

# class  Parent():
#     __a=10
#     def __init__(self):
#         self.__b=20
#     def display(self):
#         print("__a",Parent.__a)
#         print("__b",self.__b)
# class Child(Parent):
#         def display(self):
#             print("__a",Parent.__a)
#             print("__b",self.__b)
# c=Child()
# c.display()
# # p=Parent()
# # p.display()
 

 #public
# class  Parent():
#     a=10
#     def __init__(self):
#         self.b=20
#     def display(self):
#         print("a",Parent.a)
#         print("b",self.b)
# class Child(Parent):
#         def display(self):
#             print("a",Parent.a)
#             print("b",self.b)
# c=Child()
# c.display()
# p=Parent()
# p.display()
# print("a outside :", Parent.a)
# print("b outside :", p.b)