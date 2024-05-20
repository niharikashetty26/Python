def isPalindrome(S):
    n = S[::-1]
    if n == S:
        return 1
    else:
        return 0
s="aba"
print(isPalindrome(s))