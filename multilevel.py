#multilevel inheritance : grand parent => parent=> child kind of relatonship
"""
class a is parrent of class b and class b is parrent of class c
class c can access the methods an attributee of class b and a also through b
"""
class emp:
    def __init__(self, name, email_id):
        self.name=name
        self.email_id=email_id
    def emp_details(self):
        print(f"{self.name} with email {self.email_id} joined the company")

class lead(emp):
    def __init__(self, name, email_id,emp_count,project_name):
        super().__init__(name, email_id)
        self.emp_count=emp_count
        self.project_name=project_name
    def project_details(self):
        print(f"{self.name} is leading a team of {self.emp_count} employees and working on {self.project_name}")

class manager(lead):
    def __init__(self, name, email_id, emp_count, project_name, client):
        super().__init__(name, email_id, emp_count, project_name)
        self.client=client

    def client_details(self):
        super().emp_details()
        super().project_details()
        print(f"{self.name} is now working as manager for {self.client} client")

m1=manager("ram", "ram@gmail.com", 13, "banking", "hdfc")
print("multilevel inheritance")
print(m1.name)
print(m1.project_name)
m1.client_details()