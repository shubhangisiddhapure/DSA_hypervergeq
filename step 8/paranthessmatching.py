def matching(list):
    count=0
    stack=[]
    i=0
    while i <len(list):
        if list[i]=='(':
            stack.append(list[i])
        if list[i]==')':
            if '('in stack:
                stack.pop()
            else:
                count+=1
        i+=1
    if len(stack)==0:
        return count
    else:
        return count+len(stack)
list=input("enter the string")
print(matching(list))
