class test():
    def __init__(self):
        self.a=10
    def m1(self):
        print("self:",self)
        print("a=",self.a)
        print("++++++++++++++++++++++")
    @classmethod
    def clamethod(cls):
        print("cls:", cls)
        print("++++++++++++++++++++++")
        test.b=50
        cls.m=30
test.clamethod()
t1=test()
t1.m1()
t1.clamethod()