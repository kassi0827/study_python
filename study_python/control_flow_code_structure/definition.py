# シンプルな関数
def say_something():
    print('hi')


say_something()


# 関数の結果を変数に代入
def say_something():
    s = 'hi'
    return s


result = say_something()
print(result)


# if文を中で使用する
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('green')
print(result)
