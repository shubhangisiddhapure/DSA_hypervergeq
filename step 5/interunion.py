# Find the union and intersection of two sorted arrays.
def union(list1,list2,len1,len2):
    union1=[]
    for i in range(len1):
        if list1[i] not in union1:
            union1.append(list1[i])
    for j in range(len2):
        if list2[j] not in union1:
            union1.append(list2[j])
    print(union1)

def intersection(list1,list2,len1,len2):
    for i in range(len2):
        if list2[i] in list1:
            print(list2[i])

list1_size=int(input("enter the size of list"))
list1=[int(input("enter the elelen1ent ")) for each in range( list1_size)]
list2_size=int(input("enter the size of list"))
list2=[int(input("enter the elelen1ent ")) for each in range( list2_size)]
union(list1,list2,list1_size,list2_size)
intersection(list1,list2,list1_size,list2_size)