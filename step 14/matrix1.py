#to swap the upper matrix values with lower matrix values
def lowtoup(arr1,n):
    for i in range(0,n):
        for j in range(i+1,n):
            arr1[i][j],arr1[j][i]=arr1[j][i],arr1[i][j]
    return (printarr(arr1,n))
def printarr(arr1,n):
    for i in range(0,n):
        for j in range(0,n):
            print(arr1[i][j],end=" ")
        print()

    

row = int(input("enter the length of array"))
col = int(input("entet the length of each element"))
print("enter the elements of the array")
arr1=[]
for i in range (0,row):
    i=[]
    for j in  range(0,col):
        x=int(input("enter the elements"))
        i.append(x)
    arr1.append(i)
printarr(arr1,row)
print("---------------------------")
(lowtoup(arr1,row))