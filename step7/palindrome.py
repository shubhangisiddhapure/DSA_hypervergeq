name=input("enter the name")
z=len(name)
i=0
while i <z/2:
    if name[i]!=name[z-i-1]:
        print("it is not a palindrome")
        break
    i+=1
else:
    print("it is palindrome")
    