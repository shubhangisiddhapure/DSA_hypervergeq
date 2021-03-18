# Finding Max and Min in a single Scan
def maxno(list1,m):
    maximum=0
    for i in range(m):
        if list1[i]>maximum:
            maximum=list1[i]
    return print("maximum no is ",maximum)

def minno(list1,m):
    minimum=list1[0]
    for i in range(m):
        if list1[i]<minimum:
            minimum=list1[i]
    return print("minimum no is ",minimum)

num=int (input("enter the size of list1"))
list1=[int(input(" enter the elements of list1")) for each in range(num)]
maxno(list1,len1)
minno(list1,len1)