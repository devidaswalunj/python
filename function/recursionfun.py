# def factorial(x):
#     if x == 1 or x == 0:
#         f = 1
#     else:
#         f = x * factorial(x-1)

#     return f


# n = int(input("Enter the number: "))
# res = factorial(n)
# print(f"Factorial of {n} is {res}")






def summ(n):
    if n == 5:
        s=5
    else:
        s = n + summ(n + 1)
        return s

n = int(input("Enter the number: "))

res = summ(n)
print(res)