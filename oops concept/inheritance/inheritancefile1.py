class Parent():
    a=10 
    def __init__(self):
        print("parent constructor")
    def isinstance(self):
        print("parent instance method")
    @classmethod
    def clasmethod(cls):
        print("parent class method")
    @staticmethod
    def statmethod():
        print("parent static method")

class Child(Parent):
    pass

c1=Child() #this is child class
print("a in parent: ",Child.a)# a is static variable  in parent class
print("a in parent: ",c1.a)#a is static variable  in parent class
print("______________________________________________________")
c1.isinstance() #parent method
print("______________________________________________________")
Child.clasmethod()#parent method
print("______________________________________________________")
Child.statmethod()#parent method
print("______________________________________________________")
c1.statmethod()# static method call usig class name and object refernces
    