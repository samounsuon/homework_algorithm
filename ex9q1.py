# Q1 - Remove space and keep result = "3456"
string = "3 4 5 6"
count=""
for i in range(len(string)):
    if string[i]!=" ":
        count+=str(string[i])
print(count)