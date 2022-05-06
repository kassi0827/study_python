l = [1, 2, 3]
i = 5

try:
    l[5]
except IndexError as ex:
    print(format(ex))
except NameError as ex:
    print(format(ex))
except Exception as ex:
    print(format(ex))
else:
    print('done')
finally:
    print('clean up')
