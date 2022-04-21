t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))

#  タプルには新しい値を入れることはできない　t[0] = 100

print(t[0])
print(t[-1])
print(t[2:5])
print(t)

print(t.index(1))
print(t.index(1, 1))
print(t.count(1))

t = ([1, 2, 3], [4, 5, 6])
print(t)
# tupleには値の代入はできない
print(t[0][0])

# 以下のように宣言することも可能
t = 1, 2, 3
print(type(t))
print(t)

t = 1,
print(type(t))
print(t)

# タプルの表現方法は注意
