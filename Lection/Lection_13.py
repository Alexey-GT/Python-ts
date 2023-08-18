def add_key(dct, ky, value):
    if ky in dct:
        raise KeyError(f'Перезаписывание существующего ключа запрещено. {dct[key] = }')
    dct[ky] = value
    return dct
data = {'one': 1, 'two': 2}
print(add_key(data, 'three', 3))
print(add_key(data, 'three', 3))