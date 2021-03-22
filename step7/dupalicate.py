name=input("enter the name")
c=""
i=0
j=1
while i <len(name):
    if name[i]==name[j]:
        c+=name[i]
    i+=1
    j+=1
    if j==len(name):
        break
print("duplicate letter in string",c)