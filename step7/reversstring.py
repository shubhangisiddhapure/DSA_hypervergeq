def reverse(string):
    if string=="":
        return 0 
    else:
        string = string[::-1] 
        return string 
  
s =input("enter the strinng")
print(reverse(s))

