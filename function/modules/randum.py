from random import *

##1 randum() - generates a random float number between 0.0 to 1.0
# x= random()
# print(x)
# for i in range(3):
#     print(random())


##2randint() - generates a random integer number between the given range
# x=randint(20,40)
# print(x)

# for i in range(3):
#     print(randint(20,40))

##3  uniform() - generates a random float number between the given range
# x=uniform(20,40)
# print(x)
# for i in range(3):
#     print(uniform(20,40))

# #4 randrange() - generates a random integer number between the given range
# x=randrange(20,40)   
# print(x)

# for i in range(3):
#     print(randrange(20,40))


# #5 choice() - generates a random element from the given sequence
# l=[1,2,3,4,5,6,7,8,9]
# x=choice(l)
# print(x)

# for i in range(3):
#     print(choice(l))    

# #6 choices() - generates a random element from the given sequence with the given weight
# l=[1,2,3,4,5,6,7,8,9]
# x=choices(l,k=3) # here k=3 means 3 random elements will be selected from the list
# print(x)

# #7 sample() - generates a random element from the given sequence with the given weight
# l=[1,2,3,4,5,6,7,8,9]
# x=sample(l,3) # print any 3 random elements from the list
# print(x)

# s="devidas walunj "
# x=sample(s,3)# print any 3 random elements from the string
# print(x)

# #8 shuffle() - shuffles the given sequence
# l=[1,2,3,4,5,6,7,8, 9]
# print(l)
# shuffle(l)
# print(l)


# #9 triangular() - generates a random float number between the given range with the given mode
# for i in range(3):
#     print(triangular(10,100,2))


# # generate the 6 digit otp
# x=randint(100000,999999)
# print("Your OTP is:",x)

#print(chr(randint(65,90)), chr(randint(97,122)),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")

#generate a random string of fix length
import string
c=[]
def random_string(strlength=10):
    letters=string.ascii_lowercase
    for i in range(10):
        x=choices(letters)
        print(c.append(x))

random_string()