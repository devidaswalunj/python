# d=eval(input("enter the dictionary of data:  "))
# v=0
# for v in d.values():
#     v=v+v
# print(v)

#write a program to find number of ocurrences of each letter present in given string?

word=input("Enter any word: ") 
vowels={'a','e','i','o','u'} 
d={} 
for x in word: 
	if x in vowels: 
		d[x]=d.get(x,0)+1 
for k,v in sorted(d.items()): 
    print(k,"occurred ",v," times") 
