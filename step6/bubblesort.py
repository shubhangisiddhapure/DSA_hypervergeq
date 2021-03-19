def bubbleSort(arr,n): 

    for i in range(n): 

        for j in range(0, n-i-1): 

            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

num=int(input("enter the size of the array"))
list1=[]
i=1
while i<=num:
    num1=int(input("enter the number"))
    list1.append(num1)
    i+=1
bubbleSort(list1,num)
