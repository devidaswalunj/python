# #dictionary- mutable
# #empty dictionary
# # d={}
# # print(d)
# # print(type(d))

# # #initialise
# # d={1:"python", 2:"java", 'a': 2000}
# # print(d)
# # print(type(d))

# # #dict()
# # d=[(1,"python"), (2,"java"), ('a',2000)]
# # print(d)
# # print(type(d))
# # di=dict(d)
# # print(di)
# # print(type(di))

# # #dynamic =user input
# # d=eval(input("enter the data of dictionary: "))
# # print(d)
# # print(type(d))

# # #accessing item
# # d={1:"python", 2:"java", 'a': 2000}
# # print(d[1])
# # d[1]="cloud"   #it will update
# # print(d)

# #update key
# d={1:"python", 2:"java", 'a': 2000}
# d[1]="cloud"   #it will update
# print(d)
# d[3]="sql"  # it create new key value
# print(d)

# #del
# d={1:"python", 2:"java", 'a': 2000}
# del d[2] #delete 2 key item
# print(d)

# #del d #delete dictionary
# print(d)

# #clear
# d={1:"python", 2:"java", 'a': 2000}
# d.clear() #delete all itrm present in dictionary
# print(d)

# #len()
# d={1:"python", 2:"java", 'a': 2000}
# print(len(d))


# #get(k),get(k,default value)
# d={1:"python", 2:"java", 'a': 2000}
# #x=d.get(1)
# #x=d.get(4)# it not give a error it give a none
# x=d.get(5,"guest") #is present give value not present give guest
# print(x)


# #pop(), popitem()
# d={1:"python", 2:"java", 'a': 2000}
# # x=d.pop(2) # it delete specific key and return value of delete
# # print(x)
# # print(d)

# x=d.popitem()# it delete any key value and return tuple of key value
# print(x)
# print(d)

# #keys(), values(), items()
# d={1:"python", 2:"java", 'a': 2000}
# print(d.keys())
# for k in d.keys():
#     print(k)

# print(d.values())
# for v in d.values():
#     print(v)


# print(d.items())
# for k, v in d.items():
#     print(k,"==",v)


# # copy()

# d={1:"python", 2:"java", 'a': 2000}
# d1=d
# print(d)
# print(d1)
# d[3]="java"
# print(d)
# print(d1)


# d={1:"python", 2:"java", 'a': 2000}
# d1=d.copy()
# print(d)
# print(d1)
# d[3]="java"
# print(d)
# print(d1)


# #setdefault()   it use to if key not present it add if key are present it not change or replace the key and values
# d={1:"python", 2:"java", 'a': 2000}
# print(d)
# d.setdefault(3,"da") 
# d.setdefault(2,"ds")
# print(d)


#update()
d={1:"python", 2:"java", 'a': 2000}
d1={3:"da"}
d.update(d1)# it add the key value or replace it
print(d)

#dictionary comprehension
d={x:x*x for x in range(1,6)}
print(d)







