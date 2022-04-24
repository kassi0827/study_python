a = 5
b = 10

# aがbと等しい
a == b

# aがbと異なる
a != b

# aがbよりも小さい
a < b

# aがbよりも大きい
a > b

# aがb以下である
a <= b

# aがb以上である
a >= b

# aかつb
if a > 0:
    if b > 0:
        print('a and b are positive')

if a > 0 and b > 0:
    print('a and b are positive')

# aまたはb
a = -1
b = 1

if a > 0:
    print('a or b is positive')
elif b > 0:
    print('a or b is positive')

if a > 0 or b > 0:
    print('a or b is positive')
