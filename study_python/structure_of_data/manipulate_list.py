s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)

print(s[0])
s[0] = 'X'
print(s)

print(s[2:5])
s[2:5] = ['C', 'D', 'E']
print(s)

s[2:5] = []
print(s)
print(s[:])

s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)

n.append(100)
print(n)

n.insert(0, 200)
print(n)

n.pop()
print(n)

n.pop(0)
print(n)

del n[0]
print(n)

n = [1, 2, 2, 2, 3]
n.remove(2)
n.remove(2)
n.remove(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)

a += b
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
