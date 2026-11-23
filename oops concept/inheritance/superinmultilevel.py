#using super() method in multilevel inheritance

class A():
    def m1(self):
        print("A class m1")

class B(A):
    def m1(self):
        print("B class m1")

class C():
    def m1(self):
        #A.m1(self)
        #super(B).m1()
        super().m1(self)
        print("this c m1 method")
c=C()
c.m1()
