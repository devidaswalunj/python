from functools import *

# l1=[10,20,30,40]
# res=reduce(lambda x,y:x+y,l1)
# print(res)

#product of all number from 1 to 10
l1=[1,2,3,4,5,6,7,8,9,10]
res=reduce(lambda x,y: x*y ,l1)
print(res)

res=reduce(lambda x,y: x*y , range(1,11))
print(res)