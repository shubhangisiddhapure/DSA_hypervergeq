def prefix(list):
    if len(list)==0:
        return ''
    current=list[0]
    for i in range(1,len(list)):
        temp=""
        if len(current)==0:
            break
        for j in range(len(list[i])):
            if j<len(current) and current[j]==list[i][j]:
                temp+=current[j]
            else:
                break
        current = temp
    return current
list=["school","scam","scotland"]
print(prefix(list))
