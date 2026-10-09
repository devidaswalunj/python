#byte datatype: immutable range(0-256) similar to array it is a collection of similar data type
'''
x=[10,20,30]
print(x)
print("datatype of x:",type(x))
b=bytes(x)
print(b)
print("datatype of b:",type(b))
'''

#bytearray datatype: mutable range(0-256) similar to array it is a collection of different data type

x=[10,20,30]
print(x)
print("datatype of x:",type(x))
ba=bytearray(x)
print(ba)
print("datatype of ba:",type(ba))
print("ba[0]",ba[0])
ba[0]=100
print("ba[0]",ba[0])