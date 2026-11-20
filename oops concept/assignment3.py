class Person():

    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dd=dd
        self.mm=mm
        self.yyyy=yyyy
    def display(self):
        print("hiii",self.name)
        dob=self.Dob(self.dd,self.mm,self.yyyy)
    class Dob():
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
            self.dob()
        def dob(self):
            print("your birth day is on {}/{}/{}".format(self.dd,self.mm,self.yyyy))

p=Person("ram",10,"aug",2004)
p.display()
























# class Person():

#     def __init__(self,name,dd,mm,yyyy):
#         self.name=name
#         self.dob=self.Dob(dd,mm,yyyy)
#     def display(self):
#         print("hiii",self.name)
#         self.dob.dob()
#     class Dob():
#         def __init__(self,dd,mm,yyyy):
#             self.dd=dd
#             self.mm=mm
#             self.yyyy=yyyy

#         def dob(self):
#             print("your birth day is on {}/{}/{}".format(self.dd,self.mm,self.yyyy))

# p=Person("ram",10,"aug",2004)
# p.display()
