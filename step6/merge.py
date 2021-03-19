def merge(left,right):
    result=[]
    i,j=0,0
    while  i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result +=left[i:]
    result +=right[j:]
    return result

def mergesort(num):
    if(len(num)<=1):
        return num
    mid = int(len(num)/2)
    left=mergesort(num[:mid])
    right=mergesort(num[mid:])
    return merge(left,right)
n=int(input("enter the size of the array"))
list1=[]
i=1
while i<=n:
    num1=int(input("enter the number"))
    list1.append(num1)
    i+=1
print(mergesort(list1))