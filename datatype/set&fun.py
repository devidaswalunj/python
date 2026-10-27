# #set-immutable
# #==write{}
# #order is unpreserved
# #indexing not alowed
# #hetrogenius data
# #typecasting=use set() function
# #empty set
# se=set()
# print(type(se))

# #initialise 
# s={10,20,30,"python", "ds"}
# print(s)
# print(type(s))

# #typecasting
# l1=["python", "da", "ds"]
# print(l1)
# print("l1:",type(l1))
# se=set(l1)
# print(se)
# print("se:",type(se))

# #built-in function
# #add
# s={10,20,30,40}
# s.add("python")
# print(s)

# #updaate

# l1=[10,20,30,40]
# s={"python", "java"}
# s.update(l1,"da")
# print(s)

# #pop
# s={30,"python", "java",10,20}
# s1=s.pop()
# print("pop item is :",s1)
# print(s)


# #remove
# s={30,"python", "java",10,20}
# s.remove(20)# it give the error when the item is not present
# print(s)


# #discard
# s={30,"python", "java",10,20}
# s.discard(20)# it not give the error when the item is not present
# print(s)

# #clear
# s={30,"python", "java",10,20}
# s.clear() #it clear the all item present in set
# print(s)

# #alicing and cloning
# s={30,"python", "java",10,20}
# s1=s  #alicing
# print(s1)
# s.add(500)
# print(s)
# print(s1)

# s={30,"python", "java",10,20}
# s1=s.copy() #cloning
# print(s1)
# s.add(500)
# print(s)
# print(s1)


#mathematical function
# s1={10,20,30,40,50}
# s2={40,50,60,70}
#union  or |
# s3=s1.union(s2)
# print(s3)
# s3=s1 | s2
# print(s3)

#intersection  or &

s1={10,20,30,40,50}
s2={40,50,60,70}
# s3=s1.intersection(s2)
# print(s3)

# s3=s1&s2
# print(s3)


#differnce or -
# s1={10,20,30,40,50}
# s2={40,50,60,70}
# s3=s1.difference(s2)
# print(s3)

# s3=s1-s2
# print(s3)

#Symentric_differnce or ^     not a same element in both set
# s1={10,20,30,40,50}
# s2={40,50,60,70}
# s3=s1.symmetric_difference(s2)
# print(s3)

# s3=s1^s2
# print(s3)n



#intersectiom_update()
# s1={10,20,30,40,50}
# s2={40,50,60,70}
# s1.intersection_update(s2)
# print(s1)

# #difference_update()
# s1={10,20,30,40,50}
# s2={40,50,60,70}
# s1.difference_update(s2)
# print(s1)

# #symentric_differnce_update()
# s1={10,20,30,40,50}
# s2={40,50,60,70}
# s1.symmetric_difference_update(s2)
# print(s1)


#isdisjoin()   all diffence element is both set 
# s1={10,20,30,40}
# s2={79,80}
# print(s1.isdisjoint(s2))


# #issubset
# s1={10,20,30,40}
# s2={10,20,30,40,50,60}
# print(s1.issubset(s2)) 


# #issubset
# s1={10,20,30,40}
# s2={10,20,30,40,50,60}
# print(s1.issuperset(s2)) 

#membership op
# s={"python", 10,20}








#print even number 1 to 20
s={ i for i in range (2,21,2)  }
print(s)


#create a set of unique vowel of given string
s="vaishali"
s1=set(s)
vowel={"a","e","i","o","u"}
s3=vowel.intersection(s1)
print(s3)