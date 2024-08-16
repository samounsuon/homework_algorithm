# Q1 - Count odd and even number in text
text = "454639"
countO=0
countE=0
for i in range(len(text)):
    if int(text[i])%2==0:
        countE+=1
    elif int(text[i])%2==1:
        countO+=1
print(countE,"\n",countO)