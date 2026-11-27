# #case 1  
# #SyntaxError: expected 'except' or 'finally' block
# try:
#     print("try")

# #case 2
# #SyntaxError: invalid syntax
# except:
#     print("hello")

# #case 3
# # valid;  try
# try:
#     print("try")
# except:
#     print("except")

# #case 4
# # SyntaxError: expected 'except' or 'finally' block
# try:
#     print("try")
# fainally:
#     print("finally")


# #case 5
# # valid;  try else
# try:
#     print("try")
# except:
#     print("except")
# else:
#     print("else")


# #case 6
# # SyntaxError: expected 'except' or 'finally' block
# try:
#     print("try")
# else:
#     print("else")

# #case 7
# # SyntaxError: expected 'except' or 'finally' block
# try:
#     print("try")
# else:
#     print("else")
# finally:
#     print("finally")

# #case 8
# # SyntaxError: default 'except:' must be last
# try:
#     print("try")
# except:
#     print("except")
# except yyyy:
#     print("except")


# #case 9
# #SyntaxError: invalid syntax
# try:
#     print("try")
# except:
#     print("except")
# else:
#     print("else")
# else:
#     print("else")

# #case 10
# # SyntaxError: expected 'except' or 'finally' block
# try:
#     print("try")
# print("hello")
# except:
#     print("except")

#case 11
# valid;  try else
try:
    print("try")
except:
    print("except")
if 10>20:
    print("if")
else:
    print("else")