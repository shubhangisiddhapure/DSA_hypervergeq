# Write a function that takes an unsigned integer and returns the number of 1 bits it has
def numSetBits(A):
        s=[]
        j=1
        while j<=32:
            z=A%2
            s.append(z)
            A=A//2
            j+=1
        s.reverse()
        print(s)
        i=0
        counter=0
        counter1=0
        while i <len(s):
            if s[i]==1:
                counter+=1
            else:
                counter1+=1
            i+=1
        return counter
num=int(input("enter the number"))
print(numSetBits(num))  