# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
def removeElement( nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
            continue
        i +=1 
    return len(nums)
print(removeElement([0,1,2,2,3,0,4,2], 2))
