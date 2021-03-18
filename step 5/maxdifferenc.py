#  Find maximum difference between two elements of an array such that smaller number appears before the larger number.
def maxDiff(arr, n): 
    list1 = []
    for i in range (0, n-1): 
        num = arr[i+1] - arr[i] 
        list1.append(num)     
    max_diff = list1[0] 
    for i in range(1, n-1): 
        if (list1[i-1] > 0): 
            list1[i] += list1[i-1] 
        if (max_diff < list1[i]): 
            max_diff = list1[i]   
    return max_diff
num=int(input("how many element you want in array"))
arr=[]
i=1
while i <=num:
    num1=int(input("enter the numeber"))
    arr.append(num1)
    i+=1
print(arr)
n = len(arr) 
print(maxDiff(arr, n))
