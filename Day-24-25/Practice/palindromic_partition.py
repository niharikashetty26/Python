def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def generate_partitions(s, i, current_partition, result):
    if i == len(s):
        result.append(current_partition[:])
        return

    for j in range(i, len(s)):
        if is_palindrome(s, i, j):
            current_partition.append(s[i:j + 1])
            generate_partitions(s, j + 1, current_partition, result)
            current_partition.pop()


def all_palindromic_partitions(s):
    result = []
    generate_partitions(s, 0, [], result)
    return result
s = "madam"

result = all_palindromic_partitions(s)

for partition in result:
    print(' '.join(partition))
