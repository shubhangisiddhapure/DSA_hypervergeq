# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.


def restoreString(s,indices):
    n=len(indices)
    a=[0]*n
    string2=""
    for i in range(n):
        x=indices[i]
        alpha=s[i]
        a[x]=alpha
    for j in range(n):
        string2+=a[j]
    return(string2)
print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))
