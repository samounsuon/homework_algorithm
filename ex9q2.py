# Q2 - Multiple each letter by 2 result = "6 8 10 12"
string = "3 4 5 6"
result=""
for i in range(len(string)):
    if string[i]!=" ":
        result+= str(int((string[i]))*2)+" "
print(result)