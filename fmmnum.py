l1=[11,22,12,33,55,23,21,32,14]
#print(max(l1))
l2=l1[0]
for i in l1:
    if i > l2:
        l2=i
        
print("maximum",l2)

l3=l1[0]
for i in l1:
    if i<l3:
        l3=i
print("minmum",l3)

for k in range(6):
    for l in range(6):
        print("*",end="")
    print()
    
