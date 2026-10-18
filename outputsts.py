#1. print():- create a empty  new line
print("devidas")
print()
print("welcome to ")
print("=================")

#2 with variable, sep="" :-divide using sep =","
a,b,c=10,20,30
print("given number is:",a,b,c,sep=",")

print("=================")
#3 end=" " not start new statement in new line
print("devidas",end="  ")
print("walunj")

#4 replacement ot=  format()
name="Tom"
age=30
sal=40000
print(name,"is earning rs.",sal,"and age is ",age)
print("{} is earning rs.{}and age is {}".format(name,sal,age))
print("{x} is earning rs.{y}and age is {z}".format(z=age,y=sal,x=name))
print(f"{name} is earning rs.{sal}and age is {age}")

