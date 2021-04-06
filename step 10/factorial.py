
def recur_factorial(n):
    fact = 1
    while(n > 1):
        fact *= n
        n -= 1
    return fact
 

num =int(input("enter the number"))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))