#4
class Animal():
    def sound(self):
        print("animal soutes")
class Birds():
    def sound(self):
        print("birds sings")
class Pet():
    def sound(self):
        print("pet cry")

def f1(obj):
    for i in obj:
        i.sound()
lobj=[Animal(), Birds(), Pet()]
f1(lobj)








#3using list
# class Animal():
#     def sound(self):
#         print("animal soutes")
# class Birds():
#     def sound(self):
#         print("birds sings")
# class Pet():
#     def sound(self):
#         print("pet cry")

# def f1(obj):
#     for i in obj:
#         i.sound()
# lobj=[Animal(), Birds(), Pet()]
# f1(lobj)






#2 using function

# class Animal():
#     def sound(self):
#         print("animal soutes")
# class Birds():
#     def sound(self):
#         print("birds sings")
# class Pet():
#     def sound(self):
#         print("pet cry")

# def f1(obj):
#     obj.sound()
# f1(Animal())
# f1(Birds())
# f1(Pet())

#1.using retrive class
# class Animal():
#     def sound(self):
#         print("animal soutes")
# class Birds():
#     def sound(self):
#         print("birds sings")
# class Pet():
#     def sound(self):
#         print("pet cry")

# class Retrive():
#     def __init__(self,obj):
#         obj.sound()

# Retrive(Animal())
# Retrive(Birds())
# Retrive(Pet())

# a=Animal()
# r1=Retrive(a)
# b=Birds()
# r1=Retrive(b)
# p=Pet()
# r1=Retrive(p)