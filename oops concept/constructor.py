#without parameter
from os import name


class student():
    def __init__(self):
        self.rno=eval(input("enter roll no: "))
        self.name=input("enter name: ")

    def show(self):
        print("roll no :", self.rno)
        print("name: ",self.name)
s1=student()
print()
s2=student()
print("***********************")
s1.show()
print()
s2.show()


#with parameter
class student():
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name

    def show(self):
        print("roll no :", self.rno)
        print("name: ",self.name)
s1=student(101,"dev")
print()
s2=student(102,"Ram")
print("***********************")
s1.show()
print()
s2.show()

#we can create multiple constructor in class but call or activate last one
class student():
    def __init__(self):
        self.rno=eval(input("enter roll no: "))
        self.name=input("enter name: ")


        def __init__(self,rno,name):
            self.rno=rno
        self.name=name

    def show(self):
        print("roll no :", self.rno)
        print("name: ",self.name)
s1=student()
