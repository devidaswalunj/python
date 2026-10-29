# def f1(name):
#     print("name",name)
# f1("tom")
# print("address of f1:", id(f1))
# wish=f1
# print("address of wish:", id(wish))
# f1("mira")
# wish("rohan")




#nested function
def outer():
    print("start outer")
    def inner():
        print("this is inner")
    print("end out")

outer()

print()
#inner function calling in out side the function
print("inner function calling in out side the function")

def outer():
    print("start outer")
    def inner():
        print("this is inner")
    print("end out")
    return inner

inn=outer()
inn()