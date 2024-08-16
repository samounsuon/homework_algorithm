min_number=0
max_number=0
for i in  range(5):
    i=int(input("please enter your text: "))
    if min_number==0 :
        min_number=i
    elif i<min_number:
        min_number=i
        
    if i>max_number:
        max_number=i
print("Max Number",max_number)
print("Min Number",min_number)