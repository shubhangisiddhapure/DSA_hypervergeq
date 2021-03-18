#Finding Multiple Missing Elements in an Array
def missingelement(arr1, num): 
    b=[0]*((arr1[-1])+1)
    m=len(b)
    for i in range(num):
        b[arr1[i]]=1
    for i in range(m):
        if b[i]==0:
            print(i)
num=int (input("enter the size of array 1"))
arr1=[]
i=1
while i<=num:
    num2=int(input('enter the number'))
    arr1.append(num2)
    i+=1
missingelement(arr1, num)