
# #print even number usinf filter()


# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         False

# l=[10,14,7,8,9,6,5,2,3]
# res=list(filter(iseven,l))
# print(res)


# #using lambda
# l=[10,14,7,8,9,6,5,2,3]
# res=list(filter(lambda x:x%2==0 ,l))
# print(res)



# # not print 't'
# inp_list=['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
# res=list(filter(lambda a:  False if  a=='t' else True, inp_list))
# print(res)

# inp_list=['t', 'u', 't', 'o', 'r', 'i', 'a', 'l']
# res=list(filter(lambda a:  a!='t', inp_list))
# print(res)



l1=[5,10,20,30,40,'a','x',50]
l2=[10,40,'a']

res=list(filter(lambda x: x not in l2,l1))
print(res)
