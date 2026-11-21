class Parent():
    def m(self):
        print("this is parent m method")

class child1(Parent):
    def m1(self):
        print("this is child1 m1 method")

class child2(Parent):
    def m2(self):
        print("this is child2 m2 method")

class child3(Parent):
    def m3(self):
        print("this is child3 m3 method")

c1=child1()
c1.m1()
c1.m()
c2=child2()
c2.m2()
c2.m()
c3=child3()
c3.m3()
c3.m()
