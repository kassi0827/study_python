def say_something_fir(*args):
    print(args)
    print('#################')
    for arg in args:
        print(arg)


say_something_fir('Hi!', 'Mike', 'Nancy')


def say_something_sec(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)


say_something_sec('Hi!', 'Mike', 'Nancy')
