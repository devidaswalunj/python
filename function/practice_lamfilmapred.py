from functools import *


#filter
#Q) You have a list of student roll numbers. Extract only even roll numbers.
numbers = [11, 20, 31, 42, 50, 63, 74, 85]
res=list(filter(lambda x: x%2==0,numbers))
print("even rol numbers are: ", res)


# Map
#Q)A company wants to increase every employee's salary by 10%.
salary = [15000, 20000, 25000, 30000, 40000]
res=list(map(lambda x: x*0.10+x,salary))
print("salary increment by 10 % is: ", res)


 #Filter – Remove failed students
#Q)Passing marks are 40 or above. Extract only passing marks.
marks = [35, 78, 25, 90, 40, 32, 65, 88]
res=list(filter( lambda x: True if x>=40  else False, marks))
print("passing student: ",res)


#Lambda – Find the largest number
#Q)Create a lambda function that accepts two numbers and returns the largest.
maximum=lambda a, b :  b if a <b else a
print("maximum:", maximum(10,20))


# Reduce – Total shopping bill
#Q)Calculate the total shopping bill using reduce().
prices = [100, 250, 150, 300, 200]
res=reduce(lambda x ,y: x+y ,prices)
print("total price is : ", res)

#Employee bonus
#Q)A company gives a 5% bonus to employees whose salary is above ₹25,000.
salary = [15000, 30000, 45000, 20000, 50000]
res=list(map(lambda x :  x*0.05+x if x>=25000 else x ,salary))
print(res)