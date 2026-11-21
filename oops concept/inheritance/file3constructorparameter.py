class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def persondetails(self):
        print("name: ",self.name)
        print("age: ", self.age)
class Employee(Person):
    def __init__(self,empid,salary, name, age):
        super().__init__(name, age)
        self.empid=empid
        self.salary=salary

    def empdetails(self):
        print("empid: ", self.empid )
        self.persondetails()
        print("salary: ",self.salary)

e=Employee(101,25000, "tom", 25)
e.empdetails()