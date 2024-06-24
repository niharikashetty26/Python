def common_keys(d1, d2):
    return set(d1.keys()) & set(d2.keys())

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 3, 'c': 4, 'd': 5}
print(common_keys(d1, d2))
