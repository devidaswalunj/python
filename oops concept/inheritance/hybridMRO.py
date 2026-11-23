class A():
    def m1(self):
        print("a m1 called")

class B(A):
    def m1(self):
        print("b m1 called")

class C(A):
    def m1(self):
        print("acm1 called")
class D(B,C):
    pass
    # def m1(self):
    #     print("D m1 called")

d=D()
d.m1()
print("MRO(D)=",D.__mro__)