

class Parent():
    def __init__(self):
        self.a=10
        print("this is parent constructor")

    def m1(self):
        print("parent m1")

class Child(Parent):
    def __init__(self):
        super().__init__()#call parent constructor
        self.b=20
        print("child constructor")

    def m2(self):
        print("sum: ",self.a+self.b)

c=Child()
c.m2()