#try except
#single except block with multiple exception
try:
    n1=eval(input("enter the n1: "))
    n2=eval(input("enter the n2: "))
    n3=n1/n2
    print("n3: ",n3)
except (ArithmeticError, TypeError,NameError) as msg:
    print("error:: ", msg)
except:
    print("some error")


# #multiple excetion block
# try:
#     n1=eval(input("enter the n1: "))
#     n2=eval(input("enter the n2: "))
#     n3=n1/n2
#     print("n3: ",n3)
# except ArithmeticError:
#     print("divided number cannot be zero")
# except ZeroDivisionError:
#     print("nuber cannot be devided by zero")

# except TypeError:
#     print("divided should be a integer number")
# except:
#     print("some error")

print("code exicuted")