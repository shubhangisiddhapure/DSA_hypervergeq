# Learner Challenge : Finding Duplicates in a Unsorted Array
def unsorted(arr1,n):
    hash=[]
    for i in range(n):
        if arr1[i] not in hash:
            hash.append(arr1[i])
        else:
            print("duplicate element ",arr1[i])

num=int (input("enter the size of array 1"))
arr1=[]
i=1
while i<=num:
    num1=int(input('enter the number'))
    arr1.append(num1)
    i+=1
unsorted(arr1,num)
