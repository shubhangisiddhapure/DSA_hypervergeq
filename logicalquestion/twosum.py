# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def twosum(num,target):
    if len(num) < 2:
        pass
    r = []
    for i in range(len(num)):
        comp = target - num[i]
        if comp in r:
            return [num.index(comp),i]
        r.append(num[i])
num=[2,3,4,6,1]
print(twosum(num,5))