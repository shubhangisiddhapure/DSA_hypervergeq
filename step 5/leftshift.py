def leftshift(arr1,m,n):
    dictionary={}
    for i in range(m):
        key=m+i-n
        if key < m:
            dictionary[key]=arr1[i]
        elif key>=m:
            dictionary[key-m]=arr1[i]
    len2=len(dictionary)
    for j in range(m):
        arr1[j]=dictionary[j]
    return print("left shift ",arr1)

    
len1=int (input("enter the size of array 1"))
arr1=[int(input(" enter the elements of array")) for each in range(len1)]
num=int(input("enter the no by which you want to shift the array elements"))
arr2=arr1.copy()
print(arr1)
arr1.reverse()
print(arr1)
leftshift(arr1,len1,num)
