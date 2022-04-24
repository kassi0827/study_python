# break ループを完全に抜けて終了
# continue 次の行以降をすっ飛ばして、ループの最初に
count = 0

while True:
    if count >= 5:
        break

    # if count == 2:
    #     count += 1
    #     continue

print(count)
count += 1
