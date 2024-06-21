dicts = [
    {'a': 1, 'b': 2},
    {'a': 2, 'c': 3},
    {'a': 3, 'b': 1, 'c': 1}
]
res = {}
for i in dicts:

    for a, b in i.items():
        if a in res:
            res[a] += b

        else:
            res[a] = b
print(res)



