# pythonでは基本的にデータ型の宣言をする必要はない
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 整数型のデータに文字列型のデータを代入すると、データ型が変わる
num = name
print(num, type(num))

# データ型の変換
name = '1'
new_num = int(name)
print(new_num, type(new_num))

# データ型を宣言することは可能ではあるが、そんなに使わないらしい
num: int = 1
name: str = '1'

# 変数宣言の最初に数字から始めると、エラーが発生　→ 1num
