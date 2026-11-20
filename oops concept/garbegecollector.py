import gc
import time

class test():
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("performing clean up activity")

    def m1(self):
        print("name: ", self.name)
t=[test("ram"),test("shyam"),test("om")]
for obj in t:
    obj.m1()
print("***************************")




import sys
class gc1():
    def __init__(self):
        print("object is created")
    def __del__(self):
        print("performing clean up activities")
g=gc1()
g1=g
g2=g1

#find how many object are created 
print("total variable create :", sys.getrefcount(g))








# class gc1():
#     def __init__(self):
#         print("object is created")
#     def __del__(self):
#         print("performing clean up activities")
# g=gc1()
# g1=g
# g2=g1
# print("3 object is created")
# del g
# time.sleep(5)
# print("object not distroyed")
# del g1
# time.sleep(5)
# print("object not distroyed")
# del g2
# time.sleep(5)
# print("object  distroyed")


# print("application close")












# class gc():
#     def __init__(self):
#         print("object is created")
#     def __del__(self):
#         print("performing clean up activities")
# g=gc()
# time.sleep(5)
# g1=gc()
# time.sleep(5)
# print("work done with g")
# print("work done with g")
# g=None
# time.sleep(5)
# g1=None
# time.sleep(5)
# print("application close")









# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())