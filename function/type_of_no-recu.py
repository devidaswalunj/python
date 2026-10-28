# #1 no return and no argument
# def add():
#     num1=int(input("enter the 1 number: "))
#     num2=int(input("enter the 2 number: "))
#     num3=num1+num2
#     print("addition of 2 number:",num3)
# add()



# #2 with return and no argument
# def add():
#     num1=int(input("enter the 1 number: "))
#     num2=int(input("enter the 2 number: "))
#     num3=num1+num2
#     return num3
# s=add()
# print("addition of 2 number:",s)

# #return with multiple variable
# def add():
#     num1=int(input("enter the 1 number: "))
#     num2=int(input("enter the 2 number: "))
#     num3=num1+num2
#     return num3,num2,num1
# s=add()
# print(s) # return in tuple format


# #3 no return and with argument
# def add(x,y):
#     sum=x+y
#     print("sum of 2 number:",sum)
# n1=int(input("enter the 1 number: "))
# n2=int(input("enter the 2 number: "))
# add(n1,n2)


#4 with return and with argument
def add(x,y):
    sum=x+y
    return sum


n1=int(input("enter the 1 number: "))
n2=int(input("enter the 2 number: "))
a=add(n1,n2)
print("sum of 2 number:", a)



