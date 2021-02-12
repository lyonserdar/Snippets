# Ternary operator
x = 1
y = 1 if x < 0 else 0

# Big numbers can be written with _
x = 100_000_000
print(x)
print(f"{x:,}")

# In-place swapping of two numbers
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)


# Reversing  a string
b = "Reverse this string"
print(b[::-1])


# Chaining of comparaion operators
n = 10
a = 1 < n < 20
print(a)

# Print the file path of imported modules
import os

print(os)

# Inspect an object in Python
test = [1, 2, 3, 4]
print(dir(test))

# Makeshift enums in python
class Animals:
    Cat, Dog, Elephant = range(3)


print(Animals.Cat)

# Return multiple values from functions
def x():
    return 1, 2, 3, 4


a, b, c, d = x()
print(x())
print(a, b, c, d)


# Check the memory useage of an object
import sys

x = 1
print(sys.getsizeof(x))

# Print string N times
n = 2
a = "This is a string"
print(a * n)


# For loop with index
x = ["a", "b", "c"]
for index, value in enumerate(x, start=1):
    print(index, value)

# ZIP
# TODO: zip

# Tuple unpacking
a, b, *_ = (1, 2, 3, 4)
print(a, b)
a, b, *c = (1, 2, 3, 4)
print(a, b, c)
a, b, *_, c = (1, 2, 3, 4, 5, 6)
print(a, b, c)

# Setattr and Getattr
# TODO: Setattr and Getattr
