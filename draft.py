a = []
b = a

print(id(a))
print(id(b))

a.append(123)
print(a)
print(b)