L = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
max = 0
window_sum = 0
N = []
for i in range(k):
    window_sum = window_sum + L[i]
N.append(window_sum)
for i in range(len(L) - k):
    window_sum = window_sum - L[i] + L[i + k]
    if window_sum > max:
        N.append(window_sum)
print(N)

