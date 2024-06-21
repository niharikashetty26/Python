def isPalindrome(n):
    newS = []
    i = 0
    while (i < len(n)):
        if n[i] == n[i][::-1]:
            newS.append(n[i])
        i = i + 1
    return newS


def format(newS):
    for item in newS:
        if len(item) > 1:
            print(' '.join(item))


def cutPalindrome(s):
    n = []
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            n.append(s[i:j])
            # print(n)
    return isPalindrome(n)


s = "madam"
find = cutPalindrome(s)
format([find])