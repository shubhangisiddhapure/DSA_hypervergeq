
def infix_2_postfix(Infix):
    Stack = []
    Postfix = []
    priority = {
        "^": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1,
        "(":0,
        ")":0
    }  
 
    for x in Infix:
        if x.isalpha() or x.isdigit():
            Postfix.append(x)  
        elif x == "(":
            Stack.append(x)  
        elif x == ")": 
            while Stack[-1] != "(":
                Postfix.append(Stack.pop())  
            Stack.pop()
        else:
            if len(Stack) == 0:
                Stack.append(x)  
            else:
                while (len(Stack) > 0 and priority[x] <= priority[Stack[-1]]): 
                    Postfix.append(Stack.pop())  
                Stack.append(x) 
 
    while len(Stack) > 0: 
        Postfix.append(Stack.pop()) 
    return"".join(Postfix) 
Infix = input("Enter an Infix Equation = ")
Infix = "".join(Infix.split())
print( Infix, "(Infix)", infix_2_postfix(Infix), "(Postfix)")