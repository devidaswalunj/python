

# method 4 to import using alice
# #alice file name
# import file1 as f

# res=f.substraction(10,20)
# print(res)

#alice usinspecific propertice
from file1 import substraction as s, radius as r
print("radius :",r)
res=s(10,20)
print(res)



# method 3 to import specific  propertice

# from file1 import x, add

# print("x =",x)
# #print("y =",y)

# res=add(10,100)
# print("addition is:" ,res)








# method 2 to import file 
#from file1 import *

# print("x =",x)
# print("y =",y)

# res=add(10,100)
# print("addition is:" ,res)

# method 1 to import file 

# import file1

# print("x =",file1.x)
# print("y =",file1.y)