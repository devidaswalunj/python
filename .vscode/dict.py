#dictionary - mutable
d={} #empty dictionary
print(d)
print("type of d:",type(d))



d={ 101:"python",102:"java",103:"c++", 'a':22, 'b':33}
print(d)
print("type of d:",type(d))
print(d[102])
print(d['a'])

d={ 101:"python",102:"java",103:"c++", 'a':22, 'b':33}
print(d)
print("type of d:",type(d))
d[104]="SQl"  #add new key and value in dictionary
print(d)

d={ 101:"python",102:"java",103:"c++", 'a':22, 'b':33,101:"python"} #new value replace the old value
print(d)
