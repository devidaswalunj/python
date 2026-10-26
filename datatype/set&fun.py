#set-immutable
#==write{}
#order is unpreserved
#indexing not alowed
#hetrogenius data
#typecasting=use set() function
#empty set
se=set()
print(type(se))

#initialise 
s={10,20,30,"python", "ds"}
print(s)
print(type(s))

#typecasting
l1=["python", "da", "ds"]
print(l1)
print("l1:",type(l1))
se=set(l1)
print(se)
print("se:",type(se))