# #static varible
# class text():
#     a=10 #staic variable 
#     def __init__(self):
#         self.b=100 #instance  variable
# print("a =", text.a)
# t1=text()
# print("b =", t1.b)


# #2
# class text():
#     a=10 #staic variable 
#     def __init__(self):
#         self.b=100 #instance  variable
# t1=text()
# t2=text()
# print("t1=", t1.__dict__)
# print("t2=", t2.__dict__)
# print("t1.a =", t1.a)
# print("t2.a =", t2.a)
# text.a=200
# print("t1.a =", t1.a)
# print("t2.a =", t2.a)
# t2.b=400
# print("t1.a =", t1.a, "t1.b=", t1.b)
# print("t2.a =", t2.a, "t2.b=", t2.b)

# t1.a=500 # it will not change the static vaiable it is the create instance varible or update
# print("t1.a =", t1.a, "t1.b=", t1.b)
# print("t2.a =", t2.a, "t2.b=", t2.b)

# print("t1=", t1.__dict__)
# print("t2=", t2.__dict__)


#declare static variable

# class text():
#     a=10
#     def __init__(self):
#         text.b=20
#     def m1(self):
#         text.c=30
#     @classmethod
#     def m2(cls):
#         text.d=40
#         cls.e=50
#     @staticmethod
#     def m3():
#         text.f=60
# print("a=", text.a)
# t1=text()
# print("b=", text.b)
# t1.m1()
# print("c=",text.c)
# text.m2()   #t1.m2()
# print("d=",text.d)
# print("e=",text.e)
# t1.m3()
# print("f=",text.f)



# #accessing the static variable
# class text():
#     a=10
#     def __init__(self):
#         self.a=100
#         print("a in cnstructor static: ",text.a)
#         print("a in cnstructor self call instance variable: ",self.a)
#     def m1(self):
#         print("a in instance method call class name: ",text.a)
#         print("a in instaance variable self call instance variable: ",self.a)

#     @classmethod
#     def m2(cls):
#         print("a in class method call class name: ",text.a)
#         print("a in class method call use cls: ",cls.a)

#     @staticmethod
#     def m3():
#         print("a in static method call class name: ",text.a)
        
        
# t1=text()
# t1.m1()
# t1.m2()
# t1.m3()

# #updating
# class text():
#     a=10
#     def __init__(self):
#         self.a=100
#         print("a in constructor static: ",text.a)
#         print("a in constructor self call instance variable: ",self.a)
#     def m1(self):
#         print("a in instance method call class name: ",text.a)
#         print("a in instaance variable self call instance variable: ",self.a)

#     @classmethod
#     def m2(cls):
#         print("a in class method call class name: ",text.a)
#         print("a in class method call use cls: ",cls.a)

#     @staticmethod
#     def m3():
#         print("a in static method call class name: ",text.a)

# text.a=5000 #update the static variable
# print("a out sidde the class: " , text.a)       
# t1=text()
# t1.a=400 #update the instance variable if not present it create 
# t1.m1()
# t1.m2()
# t1.m3()

#delete static varible
class text():
    a=10
    def __init__(self):
        self.a=100
        print("a in constructor static: ",text.a)
        print("a in constructor self call instance variable: ",self.a)
    def m1(self):
        print("a in instance method call class name: ",text.a)
        print("a in instaance variable self call instance variable: ",self.a)

    @classmethod
    def m2(cls):
        print("a in class method call class name: ",text.a)
        print("a in class method call use cls: ",cls.a)

    @staticmethod
    def m3():
        print("a in static method call class name: ",text.a)

del text.a    #delete the static variable
print("a out sidde the class: " , text.a)       
t1=text()
del t1.a #it delete the instance variable 
t1.m1()
t1.m2()
t1.m3()

