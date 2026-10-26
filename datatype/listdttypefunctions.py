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




# #operator
# #mathematicl + ,*
# l1=[10,20,30,40,60]
# l2=[10,20,30,70,50]
# print(l1+l1)
# print(l1*3)

# #relational op <,> ,<=,=>,!=
# l1=["python", "da", "ds"]
# l2=["Python", "java"]
# print(l1<l2)


# #special operator
# #membership op in, not in  check item present or not
# l1=["python", "da", "ds"] 
# l2=["Python", "java"]
# print("python" in l1)
# print("cloud" in l2)

# #identity op  is, is not ===check address
# l1=["python", "da", "ds"]
# l2=["Python", "java"]
# print(l1 is not l2)



#nasted list
# l1=["python", "da", "ds",["Python", "java"]]
# print(l1[3][1])


#####
print("++++++++++++++++++++++++++++++++++++")
#list comprehension
#print 1 to 10 number using list comprehension
# l1=[i for i in range(1,11)]
# print(l1)

# #print even number 1 to 10 number using list comprehension
# l1=[i for i in range(1,11) if i%2==0]
# print(l1)

# #print squre of list items using list comprehension
# l1=[1,2,3,4,5,6]
# l2=[i**2 for i in l1 ]
# print(l2)


#Q1) create new list with element that are present in num1 but not in num2 list
# num1=[10,20,30,40]
# num2=[30,40,50,60]
# num3=[i for i in num1 if i not in num2]
# print(num3)

#s="The quick brown  fox jumps over a lazy dog"
s="python is easy"
l1=s.split()
l2=[]
for i in l1:
    le=len(i)
    l2.append([i,le])
print(l2)
#another way using list comprehension
l2=[ [i,len(i)] for i in l1]
print(l2)