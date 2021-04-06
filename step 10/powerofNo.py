def power(num,idx):
    if(idx==1):
       return(num)
    else:
       return(num*power(num,idx-1))
base=int(input("Enter number: "))
exp=int(input("Enter index: "))
print(power(base,exp))