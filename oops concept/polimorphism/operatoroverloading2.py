
class Number:

    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        return Number(self.value + other.value)


    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)


    def __floordiv__(self, other):
        return Number(self.value // other.value)


    def __mod__(self, other):
        return Number(self.value % other.value)


    def __pow__(self, other):
        return Number(self.value ** other.value)

    def __iadd__(self, other):
        self.value += other.value
        return self


    def __isub__(self, other):
        self.value -= other.value
        return self


    def __imul__(self, other):
        self.value *= other.value
        return self


    def __itruediv__(self, other):
        self.value /= other.value
        return self


    def __lt__(self, other):
        return self.value < other.value


    def __le__(self, other):
        return self.value <= other.value


    def __gt__(self, other):
        return self.value > other.value


    def __ge__(self, other):
        return self.value >= other.value


    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __str__(self):
        return str(self.value)


a = Number(20)
b = Number(10)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
print("\nLess Than:", a < b)
print("Less Than Equal:", a <= b)
print("Greater Than:", a > b)
print("Greater Than Equal:", a >= b)
print("Equal:", a == b)
print("Not Equal:", a != b)





# A ilable magic methods for operators:

# +	🡪	__add__(self, other)
# - 	🡪	__sub__(self, other)
# *	🡪	__mul__(self, other)
# /	🡪	__truediv__(self, other)
# //	🡪	__floordiv__(self, other)
# %	🡪	__mod__(self, other)
# **	🡪	__pow__(self, other)
# +=	🡪	__iadd__(self, other)
# -=	🡪	__isub__(self, other)
# *=	🡪	__imul__(self, other)
# /=	🡪	__idiv__(self, other)
# <	🡪	__lt__(self, other)
# <=	🡪	__le__(self, other)
# >	🡪	__gt__(self, other)
# ==	🡪	__eq__(self, other)
# !=	🡪	__ne__(self, other)


