def insertionsort(arr,num):
    for i in range(1, num):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
    print(arr)

num=int(input("enter the size of the array"))
list1=[]
i=1
while i<=num:
    num1=int(input("enter the number"))
    list1.append(num1)
    i+=1
insertionsort(list1,num) 