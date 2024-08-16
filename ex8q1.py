# Q1 - How many number 8 in string
text = "9394884039"
count=0
for i in range(len(text)):
    if int(text[i])==8:
        count+=1
print(count)