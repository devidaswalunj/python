# #global variable



# a=10  #global variable
# def f1():
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()


# #local variable

# a=10   #global variable
# def f1():
#     print(a)
# def f2():
#     a=20 #local variable
#     print(a)
# f1()
# f2()


# #local variable

# a=10   #global variable
# def f1():
#     print(a)
# def f2():
#     a=20 #local variable peference than global
#     print(a)
# f1()
# f2()

#global variable in function creation

def f1():
    global a
    a=10001
    print(a)
def f2():
    #a=20 #local variable
    print(a)
f1()
f2()

#both acessing local and globaln
a=100
def f1():
    a=10
    print("local a",a)
    print("global a", globals()['a'])  #globals()[key]
f1()