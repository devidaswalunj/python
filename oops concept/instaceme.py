class calcuator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("add: ",self.a+self.b)
        self.sub()
    def sub(self):
        print("sub: ",self.a-self.b)
c=calcuator(30,20)
c.add()