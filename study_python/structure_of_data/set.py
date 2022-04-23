# DarkDream: pg kashimataichi$ python

# WARNING: Python 2.7 is not recommended.
# This version is included in macOS for compatibility with legacy software.
# Future versions of macOS will not include Python 2.7.
# Instead, it is recommended that you transition to using 'python3' from within Terminal.

# Python 2.7.16 (default, Mar 25 2021, 03: 11: 28)
# [GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20)(-macos10.15-objc - on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >> > a={1, 2, 2, 3, 4, 4, 4, 5, 6}
# >> > a
# set([
#     1, 2, 3, 4, 5, 6])
# >> > type(a)
# < type 'set' >
# >> > b={2, 3, 3, 6, 7}
# >> > b
# set([2, 3, 6, 7])
# >> > a - b
# set([1, 4, 5])
# >> > b - a
# set([7])
# >> > a & b
# set([2, 3, 6])
# >> > a + b
# Traceback(most recent call last):
# File "<stdin>", line 1, in <module >
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# >> > a | b
# set([
#     1, 2, 3, 4, 5, 6, 7])
# >> > a ^ b
# set([1, 4, 5, 7])
# >> >
