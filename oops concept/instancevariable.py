#declaring instance variables
#a.in the constructor we can declare instance variables using self keyword
#b. we can declare instance variables oonside instance methods using self keyword
#c. we can declare instance variables ioutside the class using object reference variable
#example  objectname.instancevariablename=value,==t1.a=1010


#a.in the constructor we can declare instance variables using self keyword
print("inside the class using constructor")
class text():
    def __init__(self):
        self.a=10
        self.b=10
    def show(self):
       print(self.a+self.b)

t1=text()
t1.show()

#b. we can declare instance variables oonside instance methods using self keyword
print("inside the class using instance method")
class text():
    def __init__(self):
        self.a=200
        self.b=100
    def  imethod(self):  #instance method
        self.c=400
    def show(self):
        print(self.a+self.b+self.c)
t1=text()
print("instance variable in class:" , t1.__dict__)
t1.imethod()
print("instance variable in class:" , t1.__dict__)
t1.show()

#c. we can declare instance variables outside the class using object reference variable
print("outside the class using object reference variable")
class text(): 
    def __init__(self):
        self.a=100
        self.b=200
    def show(self):
        self.e=7877
        print(self.a+self.b)

t1=text()
print("instance variable in class t1:" , t1.__dict__)
t1.c=20 
print("instance variable in class t1:" , t1.__dict__)
t1.d=5454
print("instance variable in class t1:" , t1.__dict__)
t1.show()
print("instance variable in class t1:" , t1.__dict__)

t2=text()
print("instance variable in class t2:" , t2.__dict__)
t2.a=1000
print("instance variable in class t2:" , t2.__dict__)
t2.show()
print("instance variable in class t2:" , t2.__dict__)