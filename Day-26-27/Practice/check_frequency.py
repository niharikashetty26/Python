def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_frequency(lst))
