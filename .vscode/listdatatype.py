#list-mutable

l=[]
print("l=",l)
print(type(l))
#print(l[-6:-4:-1])
l=[10, 20, 30,5,8,7,99,4,5]
print(l[1:6])
print(l[-1:-6])
print(l[-1:-6:-1])
print(l[2])
l[4]=555
print(l[4])

print(l)