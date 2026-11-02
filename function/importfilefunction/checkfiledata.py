
#dir() function is used to give the data in the file or module

import file1
print(dir(file1)) # give the data in the file1.py file
print(dir()) # give the data in the current file

import math
print(dir(math)) # give the data in the math module
print("factorial of 5 is:",math.factorial(5)) # give the factorial of 5
print(math.sqrt(16)) # give the square root of 16
print("pi value is:",math.pi) # give the value of pi



import string
print(dir(string)) # give the data in the string module
print(string.ascii_letters) # give the ascii letters