# #tuple -immutalble
# #1 empty tupe
# t1=()
# print("type of t1:",type(t1))

# #2 initialise value to tupe
# #single value
# t1=(10) # it wil be a integer
# t1=(10,)
# print("type of t1:",type(t1))
# print(t1)
# #multiple value
# t1=(10,20, "python", 3.14)
# print("type of t1:",type(t1))
# print(t1)

# #3 type casting
# l1=[10,20,30,40,60]
# print("type of l1:",type(l1))
# t1=tuple(l1)
# print("type of t1:",type(t1))
# print(t1)

# #4 dynamic input
# t1=eval(input("enter the data"))
# print("type of entered data:",type(t1))
# print(t1)

# #5 accessing tuple
# t1=(10,20,30,40,"python", "da")
# print(t1[2])

# #using for loop
# for i in t1:
#     print(i)


# #6 operator +,*
# t1=(10,20,30,40)
# t2=(50,60,70)
# print(t1+t2)
# print(t1*3)

# #7 built-in functions
# #sorted, len,max,min, 
## count():  only this function count() tuple
# t1=(10,70,10,20,50,30,80,40,10)
# print(sorted(t1))
# print(sorted(t1, reverse=True))
# print(len(t1))
# print(max(t1))
# print(min(t1))
# print(t1.count(10))


#8 tuple packing and un packing
#packing
a,b,c=10,20,30
t1=a,b,c
print(type(t1))
print(t1)
#unpacking
x,y,z=t1
print(x,y,z,sep=",")