# #type of argument
# #1postional argument
# #2keyword argument
# #3default argument
# #4variable length argument





# #positional argument
# print("positional argument")
# def person(name, age,sal):
#     print(f"{name} is of {age} years old and earning is {sal}. ")
# person("tom", 23,20000)

# print()

# #keyword argument
# print("keyword argument")
# def person(name, age,sal):
#     print(f"{name} is of {age} years old and earning is {sal}. ")
# person( name="tom",sal=20000, age=23)

# print()
# #default argument
# print("default argument")
# def person(name="guest", age=0, sal=21000):
#     print(f"{name} is of {age} years old and earning is {sal}. ")
# person( name="tom", age=23)
# person()

# print()
# #variable length argument


# def summ(*n):
#     total=0
#     for i in n:
#         total=total+i
#     print(total)
# summ()
# summ(10)
# summ(10,20)
# summ(10,20,30)

# #variable length with postional argument

# def person(*n,name):
#     print(n)
#     print(name)
# person(10,20,30,name="tom")


# def person(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# person(name="tom", age=23,sal=200000, nation="india")


