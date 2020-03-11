# Write a program to implement Byte Array, Range, Set and STRING function.


# 1. Byte Array:
str = "Saurabh Joshi"
a = bytearray(str, 'utf-8')
b = bytearray(str, 'utf-16')
print(a)
print(b)

print('------------/------------')

# 2. Range:
a = range(5, 51, 5)
for i in a:
    print(i)

print('------------/------------')

# 3. Set:
thisset = {"apple", "banana", "cherry"}
print(type(thisset))

print('------------/------------')

# 4. STRING functions:
t3 = 1, 2, 3, 4
t1 = (1, 2, 'pvpp', [1, 2], 'Hello World')

print(type(t3))
print(t3[1])

for i in t1:
    print(i)

t4 = t1 + t3
print(t4)
print(t4[1: 3])
print(t4[3][0:])
print(t4[::-1])


