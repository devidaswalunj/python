# #list


# #creating a list
# #empty list
# l1=[]
# print(type(l1))

# #intializing list with values
# l2=[1,2,3,4,5]  
# print(l2)   
# print(type(l2))



# #dynamic input
# #input from user

# l3=eval(input("Enter the item of the list: "))
# print(l3)

# #split()
# s="python is eazy"
# l4=s.split()
# print(l4)

# #typecasting
# t1=(10,20,30,40)
# print(t1)
# print(type(t1))
# l4=list(t1)
# print(l4)
# print(type(l4))

#accessing
#index
# l1=[10,20,30,40]
# print(l1[2])


#slicing
# l1=[10,20,30,40]
# print(l1[2:8:3])



#traversing
# l1=[10,20,30,40]
# for i in l1:
#     print(i)

# l1=[10,20,30,40]
# e=len(l1)
# s=0
# while (s<e):
#     print(l1[s])
#     s+=1
#built-in function
#count()
# l1=[10,20,30,40,50,10,10,60]
# print(l1.count(10))

#index()
# l1=[10,20,30,40,50,60]
# print(l1.index(50)) #it return the item index number index(item)

#append()
# l1=[10,20,30,40,50,60]
# l1.append("python")
# print(l1)

#insert()
# l6=[10,20,30,40,50,60]
# l6.insert(2,500)
# print(l6)

#extend()
# l1=[10,20,30,40,50,60]
# l2=[700,800]
# l1.extend(l2)
# print(l1)

# l3="java"
# l1.extend(l3)
# print(l1)

# l1=[10,20,30,40,50,60]
# l2=[500,600]
# l1.append(l2)   #it add at it is in the list
# print(l1)


#remove()
# l1=[10,20,30,40,50,60]
# print(l1)
# l1.remove(10) #removing the 1st data in the list
# print(l1)
#pop(),
#l1=[10,20,30,40,50,60]
# print(l1)
# l1.pop() #removing the last data in the list
#pop(index)
# l1=[10,20,30,40,50,60]
# l1.pop(2)  # index 2 item was delete
# print(l1)

# #clear()
# l1=[10,20,30,40,50,60]
# # l1.clear()
# # print(l1)


# #del l1[4]
# print(l1)

# del l1
# print(l1)  #error


# # reverse()
# l1=[10,20,30,40,50,60]
# print(l1)
# l1.reverse()
# print(l1)

# print("+++++++++++++++++++")

# #sort

# l1=[10,20,30,40,50,60]
# print(l1)
# l1.sort()  # by default ascending
# print(l1)

# l1.sort(reverse=True) #descending
# print(l1)



# #IMP
# #aliasing and cloning
# #1 aliasing use =
# l1=[10,20,30,40]
# l2=l1
# print("address of l1:", id(l1))
# print("address of l2:", id(l2))
# l1[2]=100
# print(l1)
# print(l2)



# #cloning use slicing and copy()
# #slicing
# l1=[10,20,30,40]
# l2=l1[:]
# print("address of l1:", id(l1))
# print("address of l2:", id(l2))
# l1[2]=100
# print(l1)
# print(l2)

# #copy()
# l1=[10,20,30,40]
# l2=l1.copy()
# print("address of l1:", id(l1))
# print("address of l2:", id(l2))
# l1[2]=100
# print(l1)
# print(l2)