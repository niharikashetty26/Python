def string_lengths(strings):
    result = {}
    for string in strings:
        if len(string) > 3:
            result[string] = len(string)
    return result

strings = ["apple", "bat", "cat", "dolphin", "egg"]
print(string_lengths(strings))