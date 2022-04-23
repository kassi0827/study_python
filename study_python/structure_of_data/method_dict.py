# Python 2.7.16 (default, Mar 25 2021, 03: 11: 28)
# [GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20)(-macos10.15-objc - on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >> > d={'x': 10, 'y': 20}
# >> > d
# {'y': 20, 'x': 10}
# >> > d.keys()
# ['y', 'x']
# >> > d.values()
# [20, 10]
# >> > d2={'x': 1000, 'j': 500}
# >> > d2
# {'x': 1000, 'j': 500}
# >> > d.update(d2)
# >> > d
# {'y': 20, 'x': 1000,
#     'j': 500}
# >> > d['x']
# 1000
# >> > d.get('x')
# 1000
# >> > d['z']
# Traceback(most recent call last):
# File "<stdin>", line 1, in <module >
# KeyError: 'z'
# >> > d.get('x')
# 1000
# >> > d.get('z')
# >> > r=d.get('z')
# >> > r
# >> > type(r)
# < type 'NoneType' >
# >> > d
# {'y': 20, 'x': 1000,
#     'j': 500}
# >> > d.get('x')
# 1000
# >> > d
# {'y': 20, 'x': 1000,
#     'j': 500}
# >> > d.pop('x)
# File "<stdin>", line 1
# d.pop('x)
# ^
# SyntaxError: EOL while scanning string literal
# >> > d.pop('x')
# 1000
# >> > d
# {'y': 20, 'j': 500}
# >> > del d['y']
# >> > d
# {'j': 500}
# >> > del d
# >> > d
# Traceback(most recent call last):
# File "<stdin>", line 1, in <module >
# NameError: name 'd' is not defined
# >> > d={'a': 100, 'b': 200}
# >> > d
# {'a': 100, 'b': 200}
# >> > d.clear()
# >> > d
# {}
# >> > d={'a': 100, 'b': 200}
# >> > d
# {'a': 100, 'b': 200}
# >> > 'a' in d
# True
# >> > 'j' in d
# False
