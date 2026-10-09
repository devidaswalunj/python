#range immutable
# 3 way
# 1 one arg=(stop), syntax= range(stop)
r1=range(10)
print(type(r1))
for i in r1:
    print(i)
#2 two arg=(start, stop), syntax= range(start, stop)
r1=range(10,30)
print(type(r1))
for i in r1:
    print(i)
#3 three arg=(start, stop,step), syntax= range(start, stop,step)

r1=range(10,101,10)
print(type(r1))
for i in r1:
    print(i)