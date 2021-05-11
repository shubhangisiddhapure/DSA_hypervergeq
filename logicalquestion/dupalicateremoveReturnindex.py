

# all dupalicate in sorted array and return index
def allduplicate(nums):
   number= 1
   if len(nums)==0:
        return 0
   for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[number] = nums[i]
            number +=1
   return number
list1=[0,0,1,1,1,2,2,3,3,4]

print(allduplicate(list1))
