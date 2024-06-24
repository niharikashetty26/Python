def merge_dicts(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        if k in merged:
            merged[k] += v
        else:
            merged[k] = v
    return merged

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(merge_dicts(d1, d2))
