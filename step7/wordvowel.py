string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:",vowels)
i=0
c=1
while i <len(string):
    if string[i]==" ":
        c+=1
    i+=1
print("number of word",c)       