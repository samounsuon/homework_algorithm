
text = "454639"
sum=0
for i in range(len(text)):
    if int(text[i])%2==0:
        sum+=int(text[i])
print(sum)