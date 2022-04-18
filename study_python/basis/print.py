print('Hi')

print('Hi', 'Mike')

print('Hi', 'Mike', sep=',')

print('Hi', 'Mike', sep=',', end='\n')

# デフォルトはend=にはバックスラッシュnが入っており、勝手に改行してくれる
print('Hi', 'Mike', sep=',', end='')
print('Hi', 'Mike', sep=',', end='')

# 以下で毎回改行の前に任意の文字を入力することができる
print('Hi', 'Mike', sep=',', end='.\n')
