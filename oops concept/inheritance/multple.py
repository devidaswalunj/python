class parentA:
    def m1(self):
        print("parentB m1")

class parentB():
    def m2(self):
        print("parentB m2")


class child(parentA,parentB):
    def m3(self):
        print("child m3")

c=child()
c.m1()
c.m2()
c.m3()