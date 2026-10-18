from sys import *
print(argv[1:])
a=argv[1]
b=argv[2]
c=argv[3]
print((a)if a>b and a>c else print(b) if b>c else print(c))
