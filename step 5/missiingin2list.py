# We have 2 arrays, we have to print the numbers of the first array which are missing in the second array
def missingnum(list1,list2,len1,n):
    s ={}
    for i in range(n): 
        s[list2[i]] = 1
    for i in range(len1): 
        if list1[i] not in s.keys(): 
            print(list1[i]) 
num=int(input('how many element you in list'))
i=1
list1=[]
while i <= num:
    num1=int(input('enter the number'))
    list1.append(num1)
    i+=1
num2=int(input('how many element you want in second list'))
i=1
list2=[]
while i <= num2:
    num3=int(input('enter the number'))
    list2.append(num3)
    i+=1
len1=len(list1)
n=len(list2)
missingnum(list1,list2,len1,n)