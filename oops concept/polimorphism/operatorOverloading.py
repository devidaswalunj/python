#Two different class then were write mazic method
class Employee:
    def __init__(self,name,sal_per_day):
        self.name=name
        self.sal_per_day=sal_per_day

    def __mul__(self,other):
        return self.sal_per_day*other.no_of_days

class Timesheet:
    def __init__(self,name,no_of_days):
        self.name=name
        self.no_of_days=no_of_days

e=Employee("tom",500)
t=Timesheet("tom",20)
print("total salary:",e*t)
    
















#operator overloading with 3 object
# class Book:
#     def __init__(self,pages):
#         self.pages=pages

#     def __add__(self,other):
#         s= self.pages+other.pages
#         return Book(s)
    
#     def __str__(self):
#         return str(self.pages)

# b1=Book(20)
# b2=Book(30)
# b3=Book(50)
# b4=b1+b2+b3
# print("total pages:", b4)


# #operator overloading with 2 parameter
# class Book:
#     def __init__(self,pages):
#         self.pages=pages

#     def __add__(self,other):
#         print("self: ", self.pages)
#         print("other: ",other.pages)
#         s= self.pages+other.pages
#         return s

# b1=Book(20)
# b2=Book(30)
# b3=b1+b2
# print("total pages:", b3)