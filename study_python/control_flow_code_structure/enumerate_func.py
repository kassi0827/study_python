i = 0
for fruit in ['apple', 'banana', 'orange']:
    print(i, fruit)
    i += 1

# この書き方では長くなるので、以下のようにすることも可能
# 配列にインデックスを付与する関数

print('###############################')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
