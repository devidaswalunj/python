class Employee:
    def accept(self):
        self.emp_id = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.salary = float(input("Enter Employee Salary: "))
        
    def display(self):
        print("Employee ID: ", self.emp_id)
        print("Employee Name: ", self.name)
        print("Employee Salary: ", self.salary)

e1 = Employee()
e1.accept()
e1.display()
print("--------------------------------------------------")
e2 = Employee()
e2.accept()
e2.display()
print("--------------------------------------------------")

e3 = Employee()
e3.accept()
e3.display()