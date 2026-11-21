class Math():
    a=10
    def __init__(self):
        self.b=20
    def sum(self):
        return self.a+self.b

class Call():
    def __init__(self):
        self.m=Math()


    def m1(self):
        print("a:",self.m.a)
        print("b: ", self.m.b)
        print("sum:", self.m.sum())
c=Call()
c.m1()