#Python program to repeat M characters of a string N times

def mult_times(str, char, targetNo):
    front_len = char
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]

    result = ''
    for i in range(targetNo):
        result = result + front
    return result


print (mult_times('IncludeHelp', 7, 5))
print (mult_times('prem', 4, 3))
print (mult_times('Hello', 3, 7))
