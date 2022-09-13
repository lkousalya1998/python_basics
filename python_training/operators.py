from tkinter import Y


x = 10
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)
x %= y
print(x)
x //= y
print(x)
x **= y
print(x)

x = 10
x &= 6
print(x)

x |= y
print(x)
x ^= y
print(x)
x >>= y
print(x)
x <<= y
print(x)

#logical operators:

print(x < 5 and x < 100)
print(x < 5 or x < 100)
print(not(x < 5 and x < 10))

#identity operators

#Returns True if both variables are the same object
print(x is y)

#Returns True if both variables are not the same object
print(x is not y)

#membership operators

#Returns True if a sequence with the specified value is present in the object
x = ["kousalya", "lakshmanan"]

print("kousalya" in x)
print("kousi" in x)

#Returns True if a sequence with the specified value is not present in the object

print("kousalya" not in x)
print("kousi" not in x)


# RESULTS

# 15
# 5
# 50
# 2.0
# 0
# 100000
# 2
# 15
# 10
# 50
# 10.0
# 0.0
# 0.0
# 0.0
# 2
# 7
# 2
# 0
# 0
# True
# True
# False
# False
# True
# True
# False
# False
# True