# ncr=n!/r!(n-r)!
def ncr(n, r): 
    return (fact(n) / (fact(r)* fact(n - r))) 
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("ente the number n"))
r=int(input("ente the number r"))
print(ncr(n,r))