class Car():
    def __init__(self):
        self.name="scorpio"
        self.model="s11"
        self.color="black"
    def cardata(self):
        print("car name:",self.name)
        print("car model:", self.model)
        print("car color: ", self.color)
class Employee():
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.c=Car()

    def showemployee(self):
        print("employee id:",self.eid)
        print("employee name: ",self.ename)
        print("employee salary: ", self.esal)
        self.c.cardata()


e=Employee(101,"ram",25000)
e.showemployee()