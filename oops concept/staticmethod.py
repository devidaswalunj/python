class sta():
    a=10
    def __init__(self):
        self.y=100
    @staticmethod
    def stamethod():
        a=10
        b=30
        print("addition:",a+b)
s=sta()
s.stamethod()
sta.stamethod()
#s.stamethod(10,20)