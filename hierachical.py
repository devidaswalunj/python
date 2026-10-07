"""
hierarchical inheritance: one parent clas and multiple child classes 
clas a is parent of class b and class c can access method and attribute of class a 

"""
class company:
    def __init__(self, company_name, location):
        self.company_name=company_name
        self.location=location

    def company_details(self):
        print(f"welcome to {self.company_name} location is {self.location}")

    def work_time(self):
        print("9:00 to 6:00")

class developer(company):
    def __init__(self, company_name, location,salary):
        super().__init__(company_name, location)
        self.salary=salary

    def language(self):
        super().company_details()
        super().work_time()
        print(f"developer is working on python and salary is {self.salary}rs ")

class tester(company):
    def __init__(self, company_name, location, salary):
        super().__init__(company_name, location)
        self.salary=salary

    def testing(self):
        super().company_details()
        super().work_time()
        print(f"tester is working on selenium and salary is {self.salary}rs")

print("hierachical inheritance")
d1=developer("tcs", "pune", 800000)
t1=tester("infosys","mumbai", 570890)
d1.language()
t1.testing()