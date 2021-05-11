

# all dupalicate in sorted array and return index
def allduplicate(arr,m):
    i=0
    while i<m-1:
        if arr[i]!=arr[i+1]:
            i+=1
        else :
            if arr[i-1]!=arr[i]:
                arr.remove.(arr[i])
                return len(arr)
                i+=1
            else:
                i+=1
num=int (input("enter the size of array "))
arr=[int(input(" enter the elements of array in ascending manner")) for each in range(num)]    
allduplicate(arr,num)
