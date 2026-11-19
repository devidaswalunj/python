#accessing the instance variable
class text():
    def __init__(self):
        self.a=10
        self.b=10
        print("a in constructore:", self.a)
        print("b in constructore:", self.b)
    def show(self):
       print("a in method:" ,self.a)

t1=text()
t1.show()
print("a in outside the class:", t1.a)

#updating the instance varible 
print("_____________________________________________")
class text():
    def __init__(self):
        self.a=10
    def show(self):
      self.a=10000
      print("a " ,self.a)

t1=text()
t2=text()
print("instance variable in class t1:" , t1.__dict__)
print("instance variable in class t2:" , t2.__dict__)
t1.show()
print("instance variable in class t1:" , t1.__dict__)
print("instance variable in class t2:" , t2.__dict__)
t2.show()
print("instance variable in class t2:" , t2.__dict__)
t2.a=5000# using this we can create instance variable or update 
print("instance variable in class t2:" , t2.__dict__)

 #deleting the instance variable
print("_____________________________________________")
class text():
    def __init__(self):
        self.a=10
    def show(self):
     del self.a
      

t1=text()
t2=text()
print("instance variable in class t1:" , t1.__dict__)
print("instance variable in class t2:" , t2.__dict__)
t1.show()
print("instance variable in class t1:" , t1.__dict__)
print("instance variable in class t2:" , t2.__dict__)
print("instance variable in class t2:" , t2.__dict__)
del t2.a
print("instance variable in class t2:" , t2.__dict__)