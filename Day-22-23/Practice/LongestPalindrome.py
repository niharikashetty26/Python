def isPalindrome(temp):
    i = 0
    j = len(temp) - 1
    while (i < j):
        if temp[i] != temp[j]:
            return False
        i = i + 1
        j = j - 1
    return True


s = "abcdabbcacd"
n = []
for i in range(0, len(s)):
    for j in range(i + 1, len(s) + 1):
        n.append(s[i:j])
# print(n)
new = []
for z in range(len(n) - 1):
    if isPalindrome(n[z]):
        new.append(n[z])
# print(new)

# count={}
# for p in new:
#     count[p]=len(p)
# print(count)
# print(max(count, key=count.get))

count = new[0]
for i in range(1, len(new)):
    if len(count) < len(new[i]):
        count = new[i]
print(count)





