L=[100,200,300,400,500,600,700]
k=3
max=0
window_sum=0
for i in range(k):
    window_sum=window_sum+L[i]
max=window_sum
for i in range(len(L)-k):
    window_sum=window_sum-L[i]+L[i+k]
    if window_sum>max:
        max=window_sum
print(max)