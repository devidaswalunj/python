class outer():
    def __init__(self):
        print("this is the outer constructor")
    class inner():
        def __init__(self):
            print("this is inner construcor")
        def m1(self):
            print("inner method")
    def m2(self):
        print("outer method")


outer().m2()
outer().inner().m1()
print("************************************")
o=outer()
o.m2()
i=o.inner()
i.m1()