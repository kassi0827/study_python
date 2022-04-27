def test_func(x, l=[]):
    l.append(x)
    return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)

# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)

r = test_func(100)
print(r)

r = test_func(100)
print(r)

# リストは参照渡しなので

print('####################')


def test_func_sec(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func_sec(100)
print(r)

r = test_func_sec(100)
print(r)
