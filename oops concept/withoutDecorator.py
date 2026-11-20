class sta():

    def __init__(self):
        self.y=100
     #here we can not use any decorator and call using instance variable or class name
    def stamethod(cls):
       print(cls)
s=sta()
s.stamethod() # it is consider the instance method
sta.stamethod("hii")# it is consider the static method
