class gparent:
    def m1(self):
        print("gparent m1")

class parent(gparent):
    def m2(self):
        print("parent m2")
class child(parent):
    def m3(self):
        print("child m3")

c=child()
c.m1()
c.m2()
c.m3()