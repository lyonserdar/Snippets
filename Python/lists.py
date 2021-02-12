# Reversing a list
a = [1, 2, 3, 4, 5]
print(a[::-1])

# Create a single string from all the elements in list
a = ["Join", "this", "please."]
print(" ".join(a))

# Find the most frequent value in a list
test = [1, 2, 3, 4, 5, 5, 5, 6, 1, 2]
print(max(set(test), key=test.count))

# Store all values of the list in new variables
a = [1, 2, 3]
x, y, z = a
print(x)

# String input to list
raw_input = "1 2 3 4"
result = list(map(lambda x: int(x), raw_input.split()))
print(result)

