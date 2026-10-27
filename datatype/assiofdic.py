#write a program to enter name and percentage marks in a dictionary and display information on the screen
d={}
number_of_student=eval(input("enter number of student: "))
for i in range(number_of_student):
    name=input("enter a name:")
    percentage=eval(input("enter the percentage:"))
    d[name]=percentage
print(d)



d={}
number_of_student=eval(input("enter number of student: "))
while i<=number_of_student:
    name=input("enter a name:")
    percentage=eval(input("enter the percentage:"))
    d[name]=percentage
    i=i+1
