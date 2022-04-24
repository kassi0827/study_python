# 最初にひっかかた行のコードが実行される

x = 10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
    # このケースでは以下の実装が実行される
elif x == 10:
    print('100000000000000000')
elif x == 10:
    print('10')
else:
    print('positive')

a = -4
b = 10

# 1行目がfalseなら、それ以降のコードは実行されない
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')
