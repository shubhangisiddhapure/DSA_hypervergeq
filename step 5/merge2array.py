#  We have 2 sorted arrays and we need to merge those two arrays in a single array in a sorted manner
def merge(list1,list2,len1,n):
    merge1=[]
    i=0
    j=0
    while i<len1 and j<n:
        if list1[i]<list2[j]:
            merge1.append(list1[i])
            i+=1
        elif list1[i]>list2[j]:
            merge1.append(list2[j])
            j+=1
        else:

            merge1.append(list1[i])
            i+=1
            j+=1
    while i<len1:
        merge1.append(list1[i])
        i+=1
    while j<n:
        merge1.append(list2[j])
        j+=1

    print(list1)
    print(list2)
    print (merge1)
len1=int (input("enter the size of list 1"))
list1=[int(input(" enter the elements of list")) for each in range(len1)]
len2=int(input("enter the size of the array2"))
list2=[int(input(" enter the elements of list")) for each in range(len2)]

merge(list1,list2,len1,len2)
