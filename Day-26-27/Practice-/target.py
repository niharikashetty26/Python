# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2, 7, 11, 15,1]
target = 8
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)



# hashmap
dict={}
for i, num in enumerate(nums):
    res=target-num
    if res in dict:
        print(dict[res],i)
    dict[num]=i