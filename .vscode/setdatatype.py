#1.set - mutable
p=set()
# set()function use to create empty set
print(p)
print("type of p:",type(p))

s={10,20,"python"}
print(s)
print("type of s:",type(s))

s={10,20,"python",10,10,"python"}
print(s)
print("type of s:",type(s))
s.add("SQl")    #add() function use to add element in set
print(s)


#==========================================================================
#2.frozenset - immutable
s={10,20,"python"}
print(s)
print("type of s:",type(s))
fs=frozenset(s)   #frozenset() function use to create frozenset
print(fs)
print("type of fs:",type(fs))
# add() function use to add element in set but not in frozenset
#remove() function use to remove element in set but not in frozenset