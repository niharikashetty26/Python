def invert_dict(d):
    return {v: k for k, v in d.items()}

d = {'a': 1, 'b': 2, 'c': 3}
print(invert_dict(d))
