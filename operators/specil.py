#type 1) identity is,  is not
#n1=10
#n2=10

n1=[10,20,30,"sql"]
n2=[10,20,30,"sql"]
print("address of n1:",id(n1))
print("address of n2:",id(n2))
print(n1 is n2)
print(n1 is not n2)
#2) membership in, not in


n3=[10,20,30,"sql"]

n1="python"
n2="0"
print(n1 in n2)
print(n1 not in n2)

print(20 in n3)
print("java" not in n3)
