# change the case of string

def uppercase(str1):
    str2=""
    for i in str1:
        if ord(i)>=97 and ord(i)<=122:
            str2+=chr(ord(i)-32)
        else:
            str2+=i
    return(str2)

def lowercase(str1):
    str2=""
    for i in str1:
        if ord(i)>=65 and ord(i)<=90:
            str2+=chr(ord(i)+32)
        else:
            str2+=i
    return(str2)
str1=input("enter the string")
print(uppercase(str1))
print(lowercase(str1))