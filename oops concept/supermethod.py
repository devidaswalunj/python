# #super() method  Accessing properties of parent class using super in child`s constructor


#3  access parent properties in child static method using super

class Parent():
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        print("m1 instance method")

    @classmethod
    def m2(cls):
        print("this is class method")

    @staticmethod
    def m3():
        print("this is static method")

class Child(Parent):
    a=100
    def __init__(self):
        self.b=200
        super().__init__()


    @staticmethod
    def chilstaticmehod():
        #we cant access the constructor and instance method of parent in child Static method
        super(Child,Child).m2()
        super(Child,Child).m3()
c=Child()
c.chilstaticmehod()


# #2 accessing  properties of parent class using super() in child  class method


# class Parent():
#     a=10
#     def __init__(self):
#         self.b=20

#     def m1(self):
#         print("m1 instance method")

#     @classmethod
#     def m2(cls):
#         print("this is class method")

#     @staticmethod
#     def m3():
#         print("this is static method")

# class Child(Parent):
#     a=100
#     def __init__(self):
#         self.b=200
#         super().__init__()


#     @classmethod
#     def chilclassmehod(cls):
#         #we cant access the constructor and instance method of parent in child clas method
#         super().m2()
#         super().m3()
# c=Child()
# c.chilclassmehod()
























# class Parent():
#     a=10
#     def __init__(self):
#         self.b=20

#     def m1(self):
#         print("m1 instance method")

#     @classmethod
#     def m2(cls):
#         print("this is class method")

#     @staticmethod
#     def m3():
#         print("this is static method")

# class Child(Parent):
#     a=100
#     def __init__(self):
#         self.b=200
#         super().__init__()
#         print("a of child: ",self.a)
#         print("a of parent:", super().a)
#         print("b :", self.b) #it depent upong the constructore call and  b =is initialize   order 
#                                     # we can not use super() method to  access the parent instance variable
#         super().m1()
#         super().m2()
#         super.m3()
# c=Child()
