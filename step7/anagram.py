def Anagram(str1, str2): 
 
    n1 = len(str1) 
    n2 = len(str2) 
  
    
    if n1 != n2: 
        z= ("it is not anagram")
        return z
 
    str1 = sorted(str1) 
    str2 = sorted(str2) 

    for i in range(0, n1): 
        if str1[i] != str2[i]: 
            
            z= ("it is not anagram")
            return z
    
    x=("it is anagram")
    return x
  
  
str1 =input("enter the string")
str2 = input("enter the strnig")
print(Anagram(str1,str2)