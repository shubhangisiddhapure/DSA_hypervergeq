# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.





def checkPowersOfThree(n: int):
    i = 1
    while i < n:
        i = i*3        
    while (i>=1) & (n>=0):
        if i<=n:
            n = n - i
        i = i/3
        if n == 0:
            return True
    return False
print(checkPowersOfThree(91))
