class Employee:
    def accept(self,emp_id,name,salary):
        self.emp_id =emp_id
        self.name = name
        self.salary =salary 
        
    def display(self):
        print("Employee ID: ", self.emp_id)
        print("Employee Name: ", self.name)
        print("Employee Salary: ", self.salary)

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = eval(input("Enter Employee Salary: "))

e4=Employee()
e4.accept(emp_id,name,salary)
e4.display()
print("--------------------------------------------------")

e1=Employee()
e1.accept(101,"Ram",25000)
e1.display()
print("--------------------------------------------------")
e2 = Employee()
e2.accept(102,"Mayur",30000)
e2.display()
print("--------------------------------------------------")
e3 = Employee()
e3.accept(103,"Rohit",35000)
e3.display()