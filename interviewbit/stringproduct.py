# Given two numbers represented as strings, return multiplication of the numbers as a string.


def multiply(num1, num2):
        if len(num1)==0 or len(num2)==0:
            return 0
        m=int(num1)
        n=int(num2)
        return m*n
num1=input("enter the no")
num2=input("enter the second no")
print(multiply(num1,num2))