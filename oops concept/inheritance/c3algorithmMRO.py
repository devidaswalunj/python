class D():
    def m1(self):
        print("D m1 called")

class E():
    def m1(self):
        print("E m1 called")

class F():
    def m1(self):
        print("F m1 called")

class B(D,E):
    def m1(self):
        print("B m1 called")


class C(D,F):
    def m1(self):
        print("C m1 called")

class A(B,C):
    def m1(self):
        print("A m1 called")


a=A()

print("MRO(A): ", A.__mro__)



































# class A():
#     def m1(self):
#         print("a m1 called")

# class B():
#     def m1(self):
#         print("b m1 called")

# class C():
#     def m1(self):
#         print("C m1 called")
# class X(A,B):
#     def m1(self):
#         print("b m1 called")

# class Y(B,C):
#     def m1(self):
#         print("Y m1 called")

# class P(X,Y,C):
#     def m1(self):
#         print("P m1 called")
# p=P()

# print(P.__mro__)

