#dictionary- mutable
#empty dictionary
# d={}
# print(d)
# print(type(d))

# #initialise
# d={1:"python", 2:"java", 'a': 2000}
# print(d)
# print(type(d))

# #dict()
# d=[(1,"python"), (2,"java"), ('a',2000)]
# print(d)
# print(type(d))
# di=dict(d)
# print(di)
# print(type(di))

# #dynamic =user input
# d=eval(input("enter the data of dictionary: "))
# print(d)
# print(type(d))

# #accessing item
# d={1:"python", 2:"java", 'a': 2000}
# print(d[1])
# d[1]="cloud"   #it will update
# print(d)

#update key
d={1:"python", 2:"java", 'a': 2000}
d[1]="cloud"   #it will update
print(d)
d[3]="sql"  # it create new key value
print(d)

#del
d={1:"python", 2:"java", 'a': 2000}
del d[2] #delete 2 key item
print(d)

#del d #delete dictionary
print(d)

#clear
d={1:"python", 2:"java", 'a': 2000}
d.clear() #delete all itrm present in dictionary
print(d)

#len()
d={1:"python", 2:"java", 'a': 2000}
print(len(d))


#get(k),get(k,default value)
d={1:"python", 2:"java", 'a': 2000}
#x=d.get(1)
#x=d.get(4)# it not give a error it give a none
x=d.get(5,"guest") #is present give value not present give guest
print(x)