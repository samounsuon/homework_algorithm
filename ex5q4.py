text = "454639"
new_text=len(text)-1
result=""
for i in range(len(text)):
    result+=text[new_text-i]
print(result)