# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.

def lengthOfLastWord(A):
        x=A.split()
        if len(A)==0:
            return 0
        elif len(A)==1:
            return len(A[0])
        else:
            if len(x)==0:
                return 0
            i=len(x)-1
            while i>=0:
                if len(x[i])!=0 :
                    return len(x[i])
                i-=1
string1=input("enter the string")
print(lengthOfLastWord(string1))