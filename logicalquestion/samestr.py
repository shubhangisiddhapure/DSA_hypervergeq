#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strStr(haystack,needle):
    match=haystack.find(needle)
    return match
haystack=input("enter the friset")
needle=input("enter the seconde")
print(strStr(haystack,needle))
  
